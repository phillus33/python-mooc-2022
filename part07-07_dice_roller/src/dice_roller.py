from secrets import choice

from random import choice

def roll(die: str):
    if die == "A":
        return choice([3,3,3,3,3,6])
    if die == "B":
        return choice([2,2,2,5,5,5])
    if die == "C":
        return choice([1,4,4,4,4,4])

def play(die1: str, die2: str, times: int):

    first_won = 0
    second_won = 0
    ties = 0

    for i in range(times):
        res1 = roll(die1)
        res2 = roll(die2)
        if res1 > res2:
            first_won += 1
        elif res2 > res1:
            second_won += 1
        elif res1 == res2:
            ties += 1
        else:
            print(res1, res2)
            
    
    return (first_won, second_won, ties)

# result = play("A", "B", 100)
# print(result)


