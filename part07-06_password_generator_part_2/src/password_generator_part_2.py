from string import ascii_lowercase, digits
from random import randint, choice

def generate_strong_password(length: int, numbers: bool, special: bool):
    
    pool = ascii_lowercase
    result = []
    output = ""

    if numbers == True:
        pool += digits
    if special == True:
        pool += "!?=+-()#"
    # print(pool)
    
    for i in range(length):
        result.append(choice(pool))
    
    if numbers == True and digits not in result:
        result[randint(0, len(result)-1)] = choice(digits)
    if special == True and "!?=+-()#" not in result:
        result[randint(0, len(result)-1)] = choice("!?=+-()#")

    for item in result:
        output += item
    return output

# print(generate_strong_password(5, True, True))

for i in range(10):
    print(generate_strong_password(8, True, True))
