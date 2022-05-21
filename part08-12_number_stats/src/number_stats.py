# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        if len(self.numbers) > 0:
            return sum(self.numbers)
        return 0

    def average(self):
        if len(self.numbers) > 0:
            return self.get_sum()/self.count_numbers()
        return 0






stats = NumberStats()
even = NumberStats()
odd = NumberStats()

print("Please type in integer numbers:")
while True:
    number = int(input())
    
    if number == -1:
        break
    
    if number % 2 == 0:
        even.add_number(number)
    
    if number % 2 != 0:
        odd.add_number(number)
    

    stats.add_number(number)

print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even.get_sum())
print("Sum of odd numbers:", odd.get_sum())

        
    

        
