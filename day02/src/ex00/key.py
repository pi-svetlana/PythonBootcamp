class Key:
    def __init__(self):
        self.passphrase = "zax2rulez"
        self.value = 10000

    def __len__(self):
        return 1337

    def __getitem__(self, item):
        if item == 404:
            return 3
        else:
            return 0

    def __str__(self):
        return "GeneralTsoKeycard"

    def __gt__(self, other):
        return self.value > other


if __name__ == "__main__":
    key = Key()

    if len(key) == 1337:
        print('AssertionPassed: len(key) == 1337')
    else:
        print('AssertionError: len(key) == 1337')

    if key[404] == 3:
        print('AssertionPassed: key[404] == 3')
    else:
        print('AssertionError: key[404] == 3')

    if key > 9000:
        print('AssertionPassed: key > 9000')
    else:
        print('AssertionError: key > 9000')

    if key.passphrase == "zax2rulez":
        print('AssertionPassed: key.passphrase == "zax2rulez"')
    else:
        print('AssertionError: key.passphrase == "zax2rulez"')

    if str(key) == "GeneralTsoKeycard":
        print('AssertionPassed: str(key) == "GeneralTsoKeycard"')
    else:
        print('AssertionError: str(key) == "GeneralTsoKeycard"')
