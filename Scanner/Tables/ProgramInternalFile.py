class PIF:
    def __init__(self):
        self.__pif = []

    def add(self, token, position):
        pairTuple = (token, position)
        self.__pif.append(pairTuple)

    def __str__(self):
        result = ""
        for tupleCouple in self.__pif:
            result += tupleCouple[0] + "->" + str(tupleCouple[1]) + "\n"
        return result