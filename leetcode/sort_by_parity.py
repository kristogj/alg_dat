from time import time

def sortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    even = []
    odd = []
    for num in A:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even + odd


def mergesortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    if len(A) == 1:
        return A
    mid = len(A)//2
    left = mergesortArrayByParity(A[0:mid])
    right = mergesortArrayByParity(A[mid:])

    return merge(left,right)

def merge(left,right):
    res = []

    while left and right:
        l = left[0] % 2 == 0
        r = right[0] % 2 == 0
        if l and not r:
            res.append(left[0])
            left.pop(0)
        elif r and not l:
            res.append(right[0])
            right.pop(0)
        elif (not r and not l) or (r and l):
            if left[0] <= right[0]:
                res.append(left[0])
                left.pop(0)
            else:
                res.append(right[0])
                right.pop(0)
    if left:
        res += left
    else:
        res += right
    return res

A = [3,1,2,4]*10000
print(mergesortArrayByParity(A))



t1 = time()
print(sortArrayByParity(A))
print(time() - t1)
t2 = time()
print(mergesortArrayByParity(A))
print(time() - t2)