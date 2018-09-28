from time import time

test = [x for x in range(10000,0,-1)]

def bubble_sort(array):
    for y in range(len(array) - 1):
        for x in range(len(array) - 1):
            if array[x] > array[x + 1]:
                array[x], array[x + 1] = array[x + 1], array[x]
    return array


# Faster if you stop comparing the last part which we know is sorted
def bubble_sort2(array):
    high = len(array) - 1
    x = 0
    while high != 0:
        if array[x] > array[x + 1]:
            array[x], array[x + 1] = array[x + 1], array[x]
        x += 1
        if x == high:
            x = x % high
            high -= 1
    return array

t1 = time()
bubble_sort(test)
print(time() - t1)
t1 = time()
bubble_sort2(test)
print(time() - t1)
