# Write your solution here
# You can test your function by calling it within the following block
def line(length, word):
    if word == '':
        word = "*"
    
    print(word[0]*length)

if __name__ == "__main__":
    line(3, "")