def row_sums():
    with open("matrix.txt") as new_file:
        list_sums = []

        for line in new_file:
            sumnum = 0
            line = line.replace("\n", "")
            parts = line.split(",")
            for part in parts:
                sumnum += int(part) 
            list_sums.append(sumnum)
    return list_sums

def matrix_sum():
    with open("matrix.txt") as new_file:
        total_sum = 0
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            for part in parts:
                total_sum += int(part)
    return total_sum

def matrix_max():
    with open("matrix.txt") as new_file:
        total_max = 0
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")

            for part in parts:
                if int(part) > total_max:
                    total_max = int(part)
    return total_max


# row_sums()