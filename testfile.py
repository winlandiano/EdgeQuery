import time
import queue


class CQueue:
    """
    An scalable circulate queue. Provide four basic options: put, get, is_empty and rescale.
    """
    def __init__(self):
        self.__q = [0]
        self.__f = 0
        self.__r = 0
        self.__size = 1
        self.__is_empty = True

    def put(self, data):
        """
        Put *data* into the Queue
        """
        if self.__r == self.__f and not self.__is_empty:
            self.__q.extend([0 for i in range(0, self.__size + 1)])
            self.__q[self.__size: self.__size + self.__r] = self.__q[0: self.__r]
            self.__r += self.__size
            self.__size += self.__size + 1

        self.__q[self.__r] = data
        self.__r = (self.__r + 1) % self.__size
        self.__is_empty = False

    def get(self):
        """
        Pop the first element in the list, pop *None* if the list is empty.
        """
        if self.__is_empty:
            return None
        tmp = self.__q[self.__f]
        self.__f = (self.__f + 1) % self.__size
        if self.__f == self.__r:
            self.__is_empty = True
        return tmp

    def is_empty(self):
        """
        Return whether the list is empty.
        """
        return self.__is_empty

    def rescale(self):
        """
        Resize the inner list acording to number of current elements in list. If there is *N* elements, the list then
        would be *N+1* long
        """
        if self.__is_empty:
            self.__q = [0]
            self.__size = 1
            self.__r = 0
            self.__f = 0
            return
        if self.__r > self.__f:
            tmp = self.__q[self.__f, self.__r]
            tmp.append(0)
        else:
            tmp = [0 for i in range(0, self.__size - self.__f + self.__r + 1)]
            tmp[0: self.__size - self.__f] = self.__q[self.__f: self.__size]
            tmp[self.__size - self.__f: self.__size - self.__f + self.__r] = self.__q[0: self.__r]
        self.__q = tmp
        self.__size = len(tmp)
        self.__f = 0
        self.__r = len(tmp) - 1


def main():
    q = CQueue()
    for i in range(0, 2):
        q.put(i)
    q.get()
    q.get()
    q.rescale()
    q.put(6)
    q.put(7)

    q.put(100)
    q.rescale()
    q.put(123)
    q.rescale()
    i = 2

if __name__ == "__main__":
    main()
