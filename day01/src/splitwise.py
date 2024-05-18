from functional_purse import add_ingot


def split_booty(*args):
    total = 0
    for i in args:
        if "gold_ingots" in i:
            total += i["gold_ingots"]
    pur1, pur2, pur3, = {}, {}, {}
    pur1["gold_ingots"] = total // 3
    pur2["gold_ingots"] = total // 3
    pur3["gold_ingots"] = total // 3
    if total % 3 == 0:
        pass
    if total % 3 == 1:
        add_ingot(pur1)
    if total % 3 == 2:
        add_ingot(pur1)
        add_ingot(pur2)
    return pur1, pur2, pur3


if __name__ == "__main__":
    purse_1 = {"gold_ingots": 3}
    purse_2 = {"gold_ingots": 2, "apples": 3}
    purse_3 = {"apples": 3}
    booty = split_booty(purse_1, purse_2, purse_3)
    print(booty)  # ({'gold_ingots': 2}, {'gold_ingots': 2}, {'gold_ingots': 1})

    p1 = {"gold_ingots": 3}
    p2 = {"gold_ingots": 10, "cucumber": 5}
    p3 = {"gold_ingots": 1, "cat": 1}
    p4 = {"egg": 8, "gold_ingots": 2}
    p5 = {"gold_ingots": 4}
    p6 = {"cake": 4, "gold_ingots": 5}
    booty = split_booty(p1, p2, p3, p4, p5, p6)
    print(booty)  # ({'gold_ingots': 9}, {'gold_ingots': 8}, {'gold_ingots': 8})
