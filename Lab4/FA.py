class FA:

    def __init__(self):
        self.__Q = []
        self.__E = []
        self.__S = {}
        self.__P = ""
        self.__F = []

    def readFile(self):

        finiteFile = open('D:\\anul3\\semestrul1\\FLCD\Lab4\\input','r')
        lines = finiteFile.readlines()
        count=0
        for line in lines:
            if count == 0:
                self.__Q = line.strip(' ').split()
                count+=1
                continue
            if count == 1:
                self.__E = line.strip(' ').split()
                count+=1
                continue
            if count == 2:
                self.__P = line.strip(' ').split()[0]
                count+=1
                continue
            if count == 3:
                self.__F = line.strip(' ').split()
                count+=1
                continue
            if count > 3:
                x = line.strip(' ').split()
                k = (x[0], x[1])
                v =[]
                for c in range(2,len(x)):
                    v.append(x[c])
                self.__S[k] = v
                count+=1

    def DFACheck(self):
        for prod in self.__S.keys():
            if len(self.__S[prod]) >1:
                return False
        return True

    def __str__(self):
        rS ="S = {"
        c =0

        for line in self.__S:
            rV = ""

            for vals in self.__S[line]:
                if len(self.__S[line]) ==1:
                    rV =rV + str(vals)
                else:
                    rV = rV + str(vals)+", "



            c+=1
            if rS == "S = {":
                rS = rS+ "("+str(line[0])  +","+str(line[1])+") -> "+rV+"\n"
            else:
                rS = rS + "     (" + str(line[0]) + "," + str(line[1]) + ") -> " + rV
                if c == len(self.__S.keys()):
                    rS = rS+"}"
                else:
                    rS = rS +"\n"

        rQ = "Q = {"
        for x in range(0, len(self.__Q)):
            rQ = rQ + str(self.__Q[x])
            if(x == len(self.__Q)-1):
                rQ = rQ + "}\n"
            else:
                rQ = rQ+", "

        rE = "E = {"
        for x in range(0, len(self.__E)):
            rE = rE + str(self.__E[x])
            if (x == len(self.__E) - 1):
                rE = rE + "}\n"
            else:
                rE = rE + ", "

        rF = "F = {"
        for x in range(0, len(self.__F)):
            rF = rF + str(self.__F[x])
            if (x == len(self.__F) - 1):
                rF = rF + "}\n"
            else:
                rF = rF + ", "

        return rQ +rE+"q0 = "+self.__P +"\n"+rF+rS