from random import randint
from time import time

test = [x for x in range(100,0,-1)]


# inplace
def quicksort(array, low=0, high=None):
    high = len(array) - 1 if high is None else high
    if low >= high:
        return
    pivot = partiton(array, low, high)
    quicksort(array, low, pivot-1)
    quicksort(array, pivot+1, high)
    return array


def partiton(array, low, high):
    pivot = low
    for i in range(low+1, high+1):
        if array[i] <= array[low]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[low] = array[low], array[pivot]
    return pivot


# Not inplace
def quicksort_ish(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[randint(0,len(array) - 1)]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        return quicksort_ish(less) + equal + quicksort_ish(greater)
    else:
        return array # Base Case


t1 = time()
quicksort(test)
print(time() - t1)
t2 = time()
quicksort_ish(test)
print(time() - t2)