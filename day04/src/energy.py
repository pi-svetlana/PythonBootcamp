from itertools import zip_longest


def fix_wiring(cables, sockets, plugs):
    return (
        f"plug {cable} into {socket} using {plug}" if plug and socket and cable else (
            f"weld {cable} to {socket} without plug" if cable and socket else "")
        for cable, socket, plug in
        zip_longest([item for item in cables if isinstance(item, str)],
                    [item for item in sockets if isinstance(item, str)],
                    [item for item in plugs if isinstance(item, str)]))


if __name__ == "__main__":
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']

    for c in fix_wiring(cables, sockets, plugs):
        print(c)

    print()

    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False]

    for e in fix_wiring(cables, sockets, plugs):
        print(e)
