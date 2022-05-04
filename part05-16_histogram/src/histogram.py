def histogram(word: str):
    hist = {}
    for char in word:
        if char not in hist:
            hist[char] = 0
        hist[char] += 1
    for key, val in hist.items():
        print(f"{key} {'*'*val}")

# histogram("abba")
