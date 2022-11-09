import re

from HashTable import *
from ProgramInternalForm import ProgramInternalForm
from Scanner import Scanner
from domain.LanguageSymbols import *

MAX_LENGTH = 20

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    constantsSymbolTable = SymbolTable(MAX_LENGTH)
    identifiersSymbolTable = SymbolTable(MAX_LENGTH)
    programInternalForm = ProgramInternalForm()
    scanner = Scanner()

    readFile()
    fileName = "resources/p3.boa.txt"
    exception = ""

    with open(fileName, 'r') as file:
        lineCnt = 0
        for line in file:
            lineCnt += 1
            tokens = scanner.tokenize(line.strip())
            for index in range(len(tokens)):
                if tokens[index] in reservedWords + separators + operators:
                    if tokens[index] == ' ':
                        continue
                    programInternalForm.add_token(tokens[index], (-1, -1))
                elif tokens[index] in scanner.cases and index < len(tokens) - 1:
                    if re.match("[1-9]", tokens[index + 1]):
                        programInternalForm.add_token((tokens[index][:-1]), (-1, -1))
                        continue
                    else:
                        exception += "Wrong input token: " + tokens[index] + " at line " + str(lineCnt) + '\n'
                elif scanner.isIdentifier(tokens[index]):
                    id = identifiersSymbolTable.insert(tokens[index])
                    programInternalForm.add_token("ID", id)
                elif scanner.isConstant(tokens[index]):
                    const = identifiersSymbolTable.insert(tokens[index])
                    programInternalForm.add_token("const", const)
                else:
                    exception += "Lexical error in token: " + tokens[index] + " at line " + str(lineCnt) + '\n'



    with open("st.out", 'w') as writer:
        idenfiers_toString = identifiersSymbolTable.toString()
        identifiersSymbolTable.printAll()
        writer.write(idenfiers_toString)
        # writer.write(constantsSymbolTable.printAll())

    with open("pif.out", 'w') as writer:
        writer.write(str(programInternalForm))

    if not exception:
        print("No errors")
    else:
        print(exception)
