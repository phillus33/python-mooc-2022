from string import ascii_lowercase
from random import sample, choice

def generate_password(length: int):
    result = ""

    for i in range(length):
        result += choice(ascii_lowercase)

    return result
