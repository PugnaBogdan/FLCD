import HashTable


class STT:

    def __init__(self, size):

        self.__container = HashTable.HashTable(size)

    def __str__(self):

        return str(self.__container)

    def add(self, key):

        self.__container.add(key)

    def contains(self, key):

        return self.__container.contains(key)

    def remove(self, key):

        self.__container.remove(key)

    def get_st_pos(self, key):

        if self.contains(key):
            return self.__container.get_pos(key)
        else:
            self.add(key)

        return self.__container.get_pos(key)

