def largest():
    with open("numbers.txt") as new_file:
        largest = 0
        first = True
        for line in new_file:
            if int(line) > largest or first:
                largest = int(line)
                first = False
    return largest

# largest()