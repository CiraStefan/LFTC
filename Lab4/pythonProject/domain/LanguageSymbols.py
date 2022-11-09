reservedWords = []
separators = []
operators = []


def readFile():
    with open('resources/tokens.in.txt', 'r') as f:
        f.readline()
        for i in range(11):
            separator = f.readline().strip()
            if separator == "<space>":
                separator = " "
            if separator == "<newline>":
                separator = "\n"
            separators.append(separator)
        for i in range(15):
            operators.append(f.readline().strip())
        for i in range(11):
            reservedWords.append(f.readline().strip())
