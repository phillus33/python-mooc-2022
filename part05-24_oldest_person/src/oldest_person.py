def oldest_person(people: list):
    # oldest = 2022
    # oldest_person = ""
    # for person in people:
    #     if person[1] < oldest:
    #         oldest_person = person[0]
    #         oldest = person[1]
    # return oldest_person

    oldest = people[0]
    for person in people:
        if person[1] < oldest[1]:
            oldest = person
    return oldest[0] 

# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]

# print(oldest_person(people))
