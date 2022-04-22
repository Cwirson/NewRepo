def print_rangoli(size):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letters = alphabet[0: size]
    reversedletters = reversed(letters)
    flors = (size-1) * 2
    for _ in range(size - 1):
        print(flors * "-" + letters[-1] + flors * "-")
    for x in letters:
        print(letters[-1] + "-", end="")    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)