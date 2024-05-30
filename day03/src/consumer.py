import argparse
import json
import logging

import redis

logging.basicConfig(level=logging.INFO)

redis_client = redis.Redis(host='localhost', port=6379, db=0)


def process_message(message, evil_id):
    transaction = json.loads(message)
    from_id = transaction['metadata']['from']
    to_id = transaction['metadata']['to']
    amount = transaction['amount']

    if to_id in evil_id and amount >= 0:
        print("\t*** Evil detected and punished!!! ***")
        transaction['metadata']['from'], transaction['metadata']['to'] = to_id, from_id

    return json.dumps(transaction)


def main(evil_id):
    pubsub = redis_client.pubsub()
    pubsub.subscribe('transactions')
    message_count = 0
    for message in pubsub.listen():
        if message['type'] == 'message':
            processed_message = process_message(message['data'], evil_id)
            logging.info("Message processed: %s", processed_message)
            message_count += 1
        if message_count == 5:
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', required=True)
    args = parser.parse_args()
    evil_accounts = [account for account in args.e.split(',')]
    main(evil_accounts)
