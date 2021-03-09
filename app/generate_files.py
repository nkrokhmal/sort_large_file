from random import choice, randint
from string import ascii_letters
from config import DATA_PATH


def generate_random_string(max_length):
    str_length = randint(1, max_length)
    return ''.join(choice(ascii_letters) for _ in range(str_length))


def generate_file(rows_length, length):
    with open(DATA_PATH, 'w') as file:
        for _ in range(rows_length):
            file.write(f'{generate_random_string(length)}\n')
