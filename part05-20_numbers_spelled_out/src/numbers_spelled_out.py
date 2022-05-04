def dict_of_numbers():
    singles = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6:"six", 7: "seven", 8: "eight", 9: "nine"}
    specials = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

    numbers = {}

    for i in range(10):
        numbers[i] = singles[i]
    
    for i in range(10,20):
        numbers[i] = specials[i]
    
    for i in range(20,100):
        first_pt = i//10
        second_pt = i % 10
        if i % 10 == 0:
            numbers[i] = tens[first_pt]
        else:
            result = tens[first_pt] + "-" + singles[second_pt]
            numbers[i] = result
    
    return numbers