def add_ingot(purse):
    if "gold_ingots" in purse:
        purse["gold_ingots"] += 1
    else:
        purse["gold_ingots"] = 1
    return purse


def get_ingot(purse):
    if "gold_ingots" in purse and purse["gold_ingots"] > 1:
        purse["gold_ingots"] -= 1
    else:
        empty(purse)
    return purse


def empty(purse):
    purse.clear()
    return purse


if __name__ == "__main__":
    my_purse = {"gold_ingots": 3}
    add_ingot(get_ingot(add_ingot(empty(my_purse))))
    print(my_purse)  # 1
    add_ingot(add_ingot(add_ingot(my_purse)))
    print(my_purse)  # 4
    get_ingot(empty(my_purse))
    print(my_purse)  # {}
