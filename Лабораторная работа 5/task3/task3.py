import random
from random import sample

def get_unique_list_numbers() -> list[int]:

    random_list = range(-10, 10)

    return random.sample(random_list, 15)

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
