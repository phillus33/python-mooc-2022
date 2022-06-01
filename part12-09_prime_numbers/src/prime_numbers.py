def prime_numbers():
    i = 1

    while True:
        if check_prime(i):
            yield i
        i += 1

def check_prime(number: int):
    if number < 2:
        return False
    # if number == 2, for loop will be skipped and therefore return as True -> 2 is a prime number after all
    for n in range(2, number):
        if number % n == 0:
            return False
    return True






# Ghetto version without helper function
# def prime_numbers():
#     i = 2

#     while i > 1:
#         is_prime = True
#         for n in range(2, i):
#             if i % n == 0:
#                 is_prime = False
#                 break
#         if is_prime == True:
#             yield i
#         i += 1

