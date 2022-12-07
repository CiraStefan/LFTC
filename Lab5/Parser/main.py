from Grammar import Grammar

class UI:
    def __int__(self):
        self.grammar = None

    def evaluateG1(self):
        self.g1 = Grammar.fromFile("g1.txt")

    def evaluateG2(self):
        self.g2 = Grammar.fromFile("g2.txt")

    def printG1(self):
        print(self.g1)

    def printG2(self):
        print(self.g2)

if __name__ == '__main__':
    ui = UI()
    ui.evaluateG1()
    print(ui.g1.getProductionsFor('A'))
    # ui.evaluateG2()

    # ui.printG1()
    # ui.printG2()