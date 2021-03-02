from random import choice
from string import ascii_letters
from config import DATA_PATH


def generate_random_string(length):
    return ''.join(choice(ascii_letters) for _ in range(length))


def generate_file(rows_length, length):
    with open(DATA_PATH, 'w') as file:
        for _ in range(rows_length):
            file.write(f'{generate_random_string(length)}\n')
