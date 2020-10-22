class HashTable:

    def __init__(self, size):

        self.__items = []

        for i in range(size):
            self.__items.append([])

        self.__size = size

    def hash_function(self, string):

        summ = 0

        for char in string:
            summ += ord(char)

        return summ % self.__size

    def add(self, key):

        self.__items[self.hash_function(key)].append(key)

    def remove(self, key):

        self.__items[self.hash_function(key)].remove(key)

    def contains(self, key):

        if key in self.__items[self.hash_function(key)]:
            return True
        return False

    def get_pos(self, key):

        list_pos = self.hash_function(key)

        count = 0
        check = False
        for item in self.__items[list_pos]:
            count += 1

            if item == key:
                check = True
                break
        return count

    def __str__(self) -> str:

        res = ""

        for i in range(self.__size):
            res = res + str(self.__items[i]) + "\n"

        return res
