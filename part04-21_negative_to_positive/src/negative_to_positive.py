number = int(input("Please type in a positive integer: "))

for num in range(number*(-1),number+1):
    if num == 0:
        continue
    print(num)