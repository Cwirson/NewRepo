def wycieraczka(N, M):
    notext = N - 1
    fsthalf = int(notext/2)
    sechalf = int(notext/2)
    pattern = ".|."
    welcomespaces = M - 7
    index1 = 1
    for _ in range(fsthalf):
        numberofspaces = M - index1*3
        print(int(numberofspaces/2) * "-" + index1 * pattern + int(numberofspaces/2)*"-")
        index1 += 2
    print(int(welcomespaces/2) * "-" + "WELCOME" + int(welcomespaces/2) * "-")
    index2 = index1 - 2
    for _ in range(sechalf):
        numberofspaces = M - index2*3
        print(int(numberofspaces/2) * "-" + index2 * pattern + int(numberofspaces/2)*"-")
        index2 -= 2
        

if __name__ == "__main__":
    print("//second number must be 3 times bigger than first one//")
    values = input("Input two numbers (lenght height) : ").split()
    N = int(values[0])          
    M = int(values[1])          
    wycieraczka(N, M) 