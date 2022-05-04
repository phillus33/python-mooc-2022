# Copy here code of line function from previous exercise and use it in your solution
def line(length, word):
    if word == '':
        word = "*"
    
    print(word[0]*length)

def shape(width, character, height, filler_char):
    rows = 0

    while rows < width:
        rows += 1
        line(rows, character)
    while height > 0:
        line(width, filler_char)
        height -= 1


if __name__ == "__main__":
    shape(5, "x", 2, "o")