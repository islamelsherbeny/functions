from time import time


def speedtest(func):
    def weapper():
        start = time()
        func()
        end = time()
        print(f"function time is {end - start}")
    return weapper


@speedtest
def bigloob():
    for number in range(1, 10000):
        print(number)


bigloob()
