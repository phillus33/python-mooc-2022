# Write your solution here
number = int(input("How many items: "))
list = []

while len(list) < number:
    value = int(input(f"Item {len(list)+1}: "))     
    list.append(value)
print(list)