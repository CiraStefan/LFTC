
class ProgramInternalForm:
    def __init__(self):
        self._contents = []

    def add_token(self, token, pos):
        self._contents.append((token, pos))

    def __str__(self):
        result = ""
        for element in self._contents:
            result += element[0] + " --> " + str(element[1]) + "\n"
        return result
