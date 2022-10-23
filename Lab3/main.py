MAX_LENGTH = 5


# Press the green button in the gutter to run the script.


class SymbolInfo:
    def __init__(self, symbol):
        self.symbol = symbol
        self.nextSymbolInfo = None


class SymbolTable:
    symbolArray = [None] * MAX_LENGTH

    def __init__(self):
        for x in range(MAX_LENGTH):
            self.symbolArray[x] = None

    def hashFunction(self, symbol):
        sum = 0
        for index in range(len(symbol)):
            sum += ord(symbol[index])

        return sum % MAX_LENGTH

    def insert(self, symbol):
        position = self.hashFunction(symbol)
        symbolInfo = SymbolInfo(symbol)

        if self.symbolArray[position] is None:
            self.symbolArray[position] = symbolInfo
        else:
            start = self.symbolArray[position]
            while start.nextSymbolInfo is not None:
                start = start.nextSymbolInfo
            start.nextSymbolInfo = symbolInfo

    def printAll(self):
        for index in range(MAX_LENGTH):
            start = self.symbolArray[index]
            if start is None:
                print('\n')
            while start is not None:
                print('index: ' + str(index) + ' -> ' + start.symbol)
                start = start.nextSymbolInfo

    def search(self, symbol):
        position = self.hashFunction(symbol)
        found = False
        temporarySymbol = self.symbolArray[position]
        while temporarySymbol is not None:
            if temporarySymbol.symbol == symbol:
                found = True
                break
            temporarySymbol = temporarySymbol.nextSymbolInfo

        if found is True:
            print('Found the symbol at position ' + str(position))
            return True
        else:
            print('Could not find the symbol in the table')
            return False

    def erase_symbol(self, symbol):

        if self.search(symbol) is False:
            return False

        position = self.hashFunction(symbol)

        tempSymbolToParseLinks = self.symbolArray[position]
        tempSymbolToRememberPrevLink = self.symbolArray[position]

        if self.symbolArray[position] is None:
            return False

        # if the bucket has a single element
        else:
            if self.symbolArray[position].nextSymbolInfo is None and self.symbolArray[position].symbol == symbol:
                self.symbolArray[position] = None
                return True

        # if the bucket has more elements
        while tempSymbolToParseLinks.nextSymbolInfo is not None and tempSymbolToParseLinks.symbol != symbol:
            tempSymbolToRememberPrevLink = tempSymbolToParseLinks
            tempSymbolToParseLinks = tempSymbolToParseLinks.nextSymbolInfo

        if tempSymbolToParseLinks.symbol == symbol and tempSymbolToParseLinks.nextSymbolInfo is not None:
            if tempSymbolToRememberPrevLink.symbol == tempSymbolToParseLinks.symbol:
                self.symbolArray[position] = tempSymbolToParseLinks.nextSymbolInfo
            else:
                tempSymbolToRememberPrevLink.nextSymbolInfo = tempSymbolToParseLinks.nextSymbolInfo
                tempSymbolToParseLinks.nextSymbolInfo = None
            return True
        else:
            tempSymbolToRememberPrevLink.nextSymbolInfo = None
            tempSymbolToParseLinks.nextSymbolInfo = None
            return True

        return False


if __name__ == '__main__':
    constantsSymbolTable = SymbolTable()
    identifiersSymbolTable = SymbolTable()
    constantsSymbolTable.insert('3')
    constantsSymbolTable.insert('hello world')
    constantsSymbolTable.insert('4')
    assert len(constantsSymbolTable.symbolArray) is MAX_LENGTH
    constantsSymbolTable.insert('5')
    constantsSymbolTable.insert('8')
    constantsSymbolTable.insert('benvenuti')
    constantsSymbolTable.insert('11')
    constantsSymbolTable.insert('7')
    constantsSymbolTable.insert('6')
    assert len(constantsSymbolTable.symbolArray) is MAX_LENGTH

    assert constantsSymbolTable.search('benvenuti') is True
    assert constantsSymbolTable.search('bine ai venit') is False
    assert constantsSymbolTable.erase_symbol('3') is True
    assert constantsSymbolTable.erase_symbol('33') is False

    constantsSymbolTable.printAll()
