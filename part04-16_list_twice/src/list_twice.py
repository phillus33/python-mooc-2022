list = []

while True:
    value = int(input("New item: "))
    if value == 0:
        break
    list.append(value)
    print(f"The list now: {list}")
    print(f"The list in order: {sorted(list)}")
print("Bye!")