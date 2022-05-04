def filter_incorrect():
    with open("lottery_numbers.csv") as new_file, open("correct_numbers.csv", "w") as correct_file:
        for line in new_file:
            saved_nums = []
            line = line.replace("\n", "")
            first_split = line.split(";")
            
            weeknum = first_split[0]
            week_and_num = weeknum.split(" ")

            numbers = first_split[1]
            split_numbers = numbers.split(",")

            correct = True

            try:
                int(week_and_num[1])
            except:
                continue
                print("That week number aint no int!")

            try:
                for number in split_numbers:
                    number = int(number)
                    if number < 1 or number > 39:
                        correct = False
                        break
                        raise Exception("That number ain't in the right range son")
                    if number in saved_nums:
                        correct = False
                        break
                        raise Exception("EETS A DUPLICATE")
                    saved_nums.append(number)
                    
            except ValueError:
                continue
                print("That number is corrupted son")

            if len(split_numbers) != 7:
                continue
                raise Exception("There ain't 7 numbers as is supposed")
            
            if correct:
                correct_file.write(f"{line}\n")
                        



# filter_incorrect()
