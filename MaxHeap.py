import random
import sys


class MaxHeap:
    def __init__(self, max_len):

        self.max_len = max_len
        self.size = 0
        self.H = [-1] * self.max_len
        self.P = [-1] * self.max_len
        self.D = [-1] * self.max_len

    def parentIndex(self, pos):
        return max((pos - 1) // 2, 0)

    def leftIndex(self, pos):
        return (2 * pos) + 1

    def rightIndex(self, pos):
        return (2 * pos) + 2

    def isLeaf(self, pos):
        if (self.size // 2) <= pos <= (self.size - 1):
            return True
        return False

    def swap(self, fpos, spos):
        self.P[self.H[fpos]], self.P[self.H[spos]] = (self.P[self.H[spos]], self.P[self.H[fpos]])
        self.H[fpos], self.H[spos] = (self.H[spos], self.H[fpos])

    def pushDown(self, pos):
        if not self.isLeaf(pos):
            leftHighest = None
            if self.leftIndex(pos) < self.size:
                if self.value(pos) < self.value(self.leftIndex(pos)):
                    leftHighest = True
            if self.rightIndex(pos) < self.size:
                if self.value(pos) < self.value(self.rightIndex(pos)) and self.value(self.leftIndex(pos)) < self.value(
                        self.rightIndex(pos)):
                    leftHighest = False
            if leftHighest is not None:
                if leftHighest:
                    self.swap(pos, self.leftIndex(pos))
                    self.pushDown(self.leftIndex(pos))
                else:
                    self.swap(pos, self.rightIndex(pos))
                    self.pushDown(self.rightIndex(pos))

    def insert(self, vertex, value):

        current = self.P[vertex]
        if current != -1:
            return
        if self.size >= self.max_len:
            return
        self.size += 1
        self.H[self.size - 1] = vertex
        self.D[vertex] = value
        current = self.size - 1
        self.P[vertex] = current

        while self.value(current) > self.value(self.parentIndex(current)):
            self.swap(current, self.parentIndex(current))
            current = self.parentIndex(current)

    def assertHeapProperty(self):
        for i in range((self.size) // 2):
            if 2 * i + 1 < self.size:
                assert self.value(2 * i + 1) <= self.value(i)
                if 2 * i + 2 < self.size:
                    assert self.value(2 * i + 2) <= self.value(i)

    def printHeap(self):
        for i in range((self.size) // 2):
            print(str(self.H[i]),end=" -> ")
            if 2 * i + 1 < self.size:
                print(str(self.H[2 * i + 1]),end=" , ")
                if 2 * i + 2 < self.size:
                    print(str(self.H[2 * i + 2]))
                else:
                    print("-")

    def maximum(self):
        return self.H[0] if self.size > 0 else None

    def value(self, index):
        # print("pos:", index)
        return self.D[self.H[index]]

    def valueByVertex(self, vertex):
        # print("pos:", index)
        return self.D[vertex]

    def delete(self, vertex):
        current = self.P[vertex]
        if current == -1:
            return
        self.D[vertex] = -1
        self.P[vertex] = -1
        self.size -= 1
        if current == self.size:
            return
        self.H[current] = self.H[self.size]
        self.P[self.H[current]] = current
        # self.H[self.size] = -1
        if self.value(current) > self.value(self.parentIndex(current)):
            while self.value(current) > self.value(self.parentIndex(current)):
                self.swap(current, self.parentIndex(current))
                current = self.parentIndex(current)
        else:
            self.pushDown(current)


if __name__ == "__main__":

    n = 5000
    vertices = list(range(n))
    random.shuffle(vertices)
    maxHeap = MaxHeap(n)
    for i in vertices:
        maxHeap.insert(i, random.randint(0, 100000))
    maxHeap.assertHeapProperty()
    for i in range(n):
        a = random.randint(0, n-1)
        maxHeap.delete(a)
        # print(maxHeap.P)
        maxHeap.assertHeapProperty()
        # maxHeap.insert(random.randint(0, n-1))
    # maxHeap.printHeap()

    print("The Max val is " + str(maxHeap.maximum())+ ","+str(maxHeap.valueByVertex(maxHeap.maximum())))
