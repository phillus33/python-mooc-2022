def spruce(height):
    whites = height -1
    stars = 1
    max_stars = ((height-1) * 2) + 1
    print("a spruce!")

    while height > 0:
        print(" "*whites + "*"*stars )
        whites -= 1
        stars += 2
        height -= 1
    
    whites = int(max_stars/2)
    print(" "*whites + "*")


if __name__ == "__main__":
    spruce(3)