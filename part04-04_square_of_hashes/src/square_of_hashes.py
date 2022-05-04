# Copy here code of line function from previous exercise
def line(length, word):
    if word == '':
        word = "*"
    print(word[0]*length)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    rows = size
    while rows > 0:
        line(size, "#")
        rows -= 1
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
