
from string import ascii_letters, digits


def change_case(orig_string: str):
    result = ""
    for char in orig_string:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char
    return result

def split_in_half(orig_string:str):
    midpoint = len(orig_string)//2
    return orig_string[:midpoint], orig_string[midpoint:]

def remove_special_characters(orig_string: str):
    allowed = ascii_letters + digits + " "
    res = ""
    for char in orig_string:
        if char in allowed:
            res += char
    return res

# print(remove_special_characters("Thi§ is a test: test?"))