from functional_purse import add_ingot
from functional_purse import empty
from functional_purse import get_ingot


def decorator(func):
    def wrapper(purse):
        print("SQUEAK")
        # return func(purse)

    return wrapper


add_ingot = decorator(add_ingot)
get_ingot = decorator(get_ingot)
empty = decorator(empty)

if __name__ == "__main__":
    my_purse = {"gold_ingots": 3}
    add_ingot(my_purse)
    print(my_purse)
    get_ingot(my_purse)
    print(my_purse)
    empty(my_purse)
    print(my_purse)
