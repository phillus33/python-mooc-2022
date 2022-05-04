def most_common_character(str: str):
    result = str[0]
    for char in str:
        if str.count(char) > str.count(result):
            result = char
            
    return result

# second_string = "exemplaryelementary"
# print(most_common_character(second_string))