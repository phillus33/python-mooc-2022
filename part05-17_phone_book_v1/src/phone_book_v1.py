# book = {}
# while True:
#     command = int(input("command (1 search, 2 add, 3 quit): "))

#     if command == 1:
#         name = input("name: ")

#         if name not in book:
#             # print(book)
#             print("no number")
#         else:
#             print(book[name])

#     if command == 2:
        
#         name = input("name: ")
#         number = input("number: ")
#         book[name] = number
#         print("ok!")

#     if command == 3:
#         print("quitting...")
#         break

def add_person(book: list):
    name = input("name: ")
    number = input("number: ")
    book[name] = number
    print("ok!")

def search(book:list):
    name = input("name: ")
    if name not in book:
        print("no number")
    else:
        print(book[name])

def main():
    book = {}

    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))

        if command == 1:
            search(book)

        if command == 2:
            add_person(book)

        if command == 3:
            print("quitting...")
            break

main()