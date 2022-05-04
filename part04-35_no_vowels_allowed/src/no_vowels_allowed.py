def no_vowels(str: str):
    
    vowels = "aeiou"
    result = ""

    for char in str:
        if char not in vowels:
            result += char
    return result

# my_string = "this is an example"
# print(no_vowels(my_string))