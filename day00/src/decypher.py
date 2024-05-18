import sys

if len(sys.argv) == 2:
    phrase = sys.argv[1]
    words = phrase.split()
    for elem in words:
        print(elem[0], sep='', end='')
else:
    print("Ошибка: необходимо ввести один аргумент")


# python3 decypher.py "Have you delivered eggplant pizza at restored keep?"
# python3 decypher.py "The only way everyone reaches Brenda rapidly is delivering groceries explicitly"
# python3 decypher.py "Britain is Great because everyone necessitates"
