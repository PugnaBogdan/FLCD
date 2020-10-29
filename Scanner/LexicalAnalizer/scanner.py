
import Tables.ProgramInternalFile as p
import Tables.SymbolTable as s
import re as regex


class Scanner:

    reservedWords = []
    separators = []
    operators = []
    constantCode = ""
    identifierCode = ""
    ex = ""

    def __init__(self,stc,sti,pif,filename):
        self.__pif = pif
        self.__stC = stc
        self.__stI = sti
        self.__fileName = filename
        self.__ok = 0

    def get_stC(self):
        return self.__stC

    def get_stI(self):
        return self.__stI

    def set_st(self, a):
        self.__st = a

    def get_pif(self):
        return self.__pif

    def set_pif(self, a):
        self.__pif= a

    def TokenizeTokenFile(self):
        TokenFile = open('D:/anul3/semestrul1/FLCD/Scanner/InputFiles/token.in','r')
        Lines = TokenFile.readlines()
        count = 0
        for line in Lines:
            count+=1
            if count<=10:
                self.operators.append(line.strip())
            elif count>10 and count <=22:
                self.reservedWords.append(line.strip())
            elif count>22 and count<=34:
                self.separators.append(line.strip())
            elif count == 35:
                self.identifierCode = line.strip()
            else:
                self.constantCode = line.strip()
        self.separators.append(" ")


    def detect(self):
        pass

    def identifier(self, word):

        return regex.search(r'^_([a-z]|[A-Z]|[0-9])*$', word)

    def constant(self, word):

        return regex.search(r'^(0|[-]?[1-9][0-9]*)$|^"([a-z]|[A-Z]|[0-9]|-)*"$', word)

    def scann(self):
        self.TokenizeTokenFile()
        problemFile = open(self.__fileName,'r')
        Lines = problemFile.readlines()
        count = 0
        for line in Lines:
            count+= 1;
            for word in line.split():

                if word.strip() in self.operators or word.strip() in self.reservedWords:
                    self.__pif.add(word,-1)
                    continue
                myW = ""

                for i in range(len(word)):
                    myW= myW+word[i]
                    if i == len(word)-1:
                        if myW in self.operators or myW in self.reservedWords or myW in self.separators:
                            self.__pif.add(myW, -1)
                            continue
                        elif self.identifier(myW):
                            x = self.__stI.get_st_pos(myW)
                            self.__pif.add("iden_1",x)
                        elif self.constant(myW):
                            x = self.__stC.get_st_pos(myW)
                            self.__pif.add("cons_1", x)
                        else:
                            self.ex += 'Error ' + myW + ' - line ' + str(count) + "\n"

                        myW=""
                        continue
                    if word[i + 1] in self.separators:
                        if myW in self.operators or myW in self.reservedWords  or myW in self.separators:
                            self.__pif.add(myW, -1)
                            myW=""
                            continue

                        elif self.identifier(myW):
                            x = self.__stI.get_st_pos(myW)
                            self.__pif.add("iden_1", x)
                        elif self.constant(myW):
                            x = self.__stC.get_st_pos(myW)
                            self.__pif.add("cons_1", x)
                        else:
                            self.ex += 'Error ' + myW + ' - line ' + str(count) + "\n"

                        myW=""
                        continue
                            #constant or identifier
                    if word[i] in self.separators:
                        self.__pif.add(word[i],-1)
                        myW = ""



        if self.ex == '':
            print("good")
        else:
            print(self.ex)
