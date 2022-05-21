def smallest_average(person1: dict, person2: dict, person3: dict):
    
    if calc_avg(person1) < calc_avg(person2) and calc_avg(person1) < calc_avg(person3):
        return person1

    if calc_avg(person2) < calc_avg(person1) and calc_avg(person2) < calc_avg(person3):
        return person2
    
    return person3

def calc_avg(person1: dict):
    return (person1["result1"] + person1["result2"] + person1["result3"]) / 3


# person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
# person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
# person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

# print(smallest_average(person1, person2, person3))

