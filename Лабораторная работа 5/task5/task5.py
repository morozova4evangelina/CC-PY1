import random


def get_random_password() -> str:
    symbols = '123456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
    n = 8
    return random.sample(symbols, n)

print(get_random_password())
