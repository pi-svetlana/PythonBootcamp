import random
import time


def emit_gel(step):
    pressure = 50
    sign = 1
    while True:
        random_step = random.randint(0, step)
        i = yield pressure
        if i is not None:
            sign *= i
            continue
        pressure += random_step * sign


def valve():
    gen = emit_gel(20)
    sign = 1
    while True:
        pressure = next(gen)
        yield pressure
        if pressure > 80 and sign == 1:
            sign = -1
            gen.send(-1)
        if pressure < 20 and sign == -1:
            sign = 1
            gen.send(-1)
        if pressure < 10 or pressure > 90:
            gen.close()
            print("Emergency break")
            break


if __name__ == "__main__":
    v = valve()
    for i in v:
        print(i)
        time.sleep(0.5)
