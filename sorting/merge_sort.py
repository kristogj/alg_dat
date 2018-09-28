from time import time

test = [x for x in range(100000,0,-1)]


def merge_sort(array):
    if len(array) == 1:
        return array
    left = merge_sort(array[0:len(array)//2])
    right = merge_sort(array[len(array)//2:])
    return merge(left,right)


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left):
        result += left
    else:
        result += right
    return result


t1 = time()
merge_sort(test)
print(time() - t1)


