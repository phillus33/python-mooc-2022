def greatest_number(x, y, z):
    if x >= y and x >= z:
        return x
    if y >= x and y >= z:
        return y
    return z


if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)