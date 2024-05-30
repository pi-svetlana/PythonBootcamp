import json
import logging
import random

import redis

logging.basicConfig(level=logging.INFO)

redis_client = redis.Redis(host='localhost', port=6379, db=0)


def generate_message():
    from_id = str(random.randint(0, 9)) * 10
    to_id = str(random.randint(0, 9)) * 10
    # from_id = ''.join(str(random.randint(0, 9)) for _ in range(10))
    # to_id = ''.join(str(random.randint(0, 9)) for _ in range(10))
    amount = random.randint(-1000000, 1000000)

    message = {
        "metadata": {
            "from": from_id,
            "to": to_id
        },
        "amount": amount
    }
    return json.dumps(message)


if __name__ == "__main__":
    for _ in range(5):
        message = generate_message()
        redis_client.publish('transactions', message)
        logging.info(message)
