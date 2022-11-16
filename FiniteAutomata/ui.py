from FiniteAutomata import FiniteAutomata


class Console:
    def readFiniteAutomata(self):
        self.fa = FiniteAutomata.read('FiniteAutomata.in')

    def displayFiniteAutomata(self):
        print(self.fa)

    def displayStates(self):
        print(self.fa.Q)

    def displayAlphabet(self):
        print(self.fa.E)

    def displayTransitions(self):
        print(self.fa.S)

    def displayFinalState(self):
        print(self.fa.F)

    def checkDFA(self):
        print(self.fa.isDfa())

    def checkAccepted(self):
        seq = input()
        print(self.fa.isAccepted(seq))


    def __displayMenu(self):
        print("1.Read FA from file")
        print("2.Display FA")
        print("3.Display FA States")
        print("4.Display FA Alphabet")
        print("5.Display FA transitions")
        print("6.Display FA final states")
        print("7.Check DFA")
        print("8.Check accepted sequence")
        print("0. Exit")

    def run(self):
        cmds = {'1':self.readFiniteAutomata,'2':self.displayFiniteAutomata,'3':self.displayStates,'4':self.displayAlphabet,
                '5':self.displayTransitions, '6':self.displayFinalState, '7':self.checkDFA,
                '8':self.checkAccepted}
        exit = False
        while not exit:
            self.__displayMenu()
            print(">>")
            cmd = input()
            if cmd in cmds.keys():
                cmds[cmd]()
            elif cmd=="0":
                exit = True
            else:
                continue