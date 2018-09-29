from math import ceil


class MaxBinaryHeap:

    def __init__(self, A=[]):
        self.heap = A
        self.lengde = len(A)
        self.heap_size = len(A) - 1

    def max_heapify(self, i):
        l = left(i)
        r = right(i)
        if l <= self.heap_size and self.heap[l] > self.heap[i]:
            largest = l
        else:
            largest = i
        if r <= self.heap_size and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def heapsort(self):
        # Build Max-Heap
        self.build_max_heap()
        print("Start:" + str(self.heap))
        c = 1
        for i in range(len(self.heap) - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.heap_size -= 1
            self.max_heapify(0)
            print("Iterasjon " + str(c) + ": " + str(self.heap))
            c += 1
        return self.heap

    def build_max_heap(self):
        for i in range(self.lengde // 2, -1, -1):
            self.max_heapify(i)

    def extract(self):
        l = self.lengde - 1
        self.heap[0], self.heap[l] = self.heap[l], self.heap[0]
        res = self.heap.pop()
        self.max_heapify(0)
        return res

    def insert(self, value):
        i = self.lengde
        self.heap.append(value)
        while i > 0 and self.heap[i] > self.heap[parent(i)]:
            self.heap[i], self.heap[parent(i)] = self.heap[parent(i)], self.heap[i]
            i = parent(i)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return int(ceil(i/2))-1


liste = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heap = MaxBinaryHeap(liste)
heap.build_max_heap()
print(heap.heap)
