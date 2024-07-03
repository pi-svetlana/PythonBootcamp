# Python Bootcamp Day02

### Exercise 00

В скрипте ex00/key.py описан класс Key с использованием магических методов, экземпляр которого проходит следующие проверки:

```
AssertionError: len(key) == 1337
AssertionError: key[404] == 3
AssertionError: key > 9000
AssertionError: key.passphrase == "zax2rulez"
AssertionError: str(key) == "GeneralTsoKeycard"

```

### Exercise 01

Реализация игры Эволюция доверия.
https://ncase.me/trust/

Описаны классы игроков Cheater, Cooperator, Copycat, Grudger, Grudger с различными типами поведения.

Класс Game содержит методы play() и top3().
По умолчанию код при запуске моделирует 10 игр (один вызов play()) между каждой парой игроков с разными типами поведения (всего 10 раундов по 10 игр в каждом) и распечатывает тройку победителей (top3()) после всей игры.
