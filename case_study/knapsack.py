from random import randint
class Object:

    def __init__(self,weight,value):
        self.weight = weight
        self.value = value

    def __str__(self):
        return f"(w:{self.weight},v:{self.value})"

    def __repr__(self):
        return f"(w:{self.weight},v:{self.value})"


# Runtime O(nW)
def knapsack(items,max_weight):
    n = len(items)
    m = [[0 for _ in range(max_weight+1)] for _ in range(n)]
    for row in range(n):
        for col in range(1, max_weight+1):
            if col >= items[row].weight:
                # max(current item + the item you can fit to max weight, value from last item check)
                # in the first iteration it compares with row -1, but all those values are 0
                # so it gives the right values anyways
                m[row][col] = max(items[row].value + m[row-1][col - items[row].weight], m[row-1][col])
            else:
                m[row][col] = m[row-1][col]

    # Find the items that gives the highest value
    # TODO: Some error here that adds items even when its over the weight limit
    goal_items = []
    row = n-1
    col = max_weight
    while row > 1 and col > 0:
        current = m[row][col]
        if m[row-1][col] == current:
            row -= 1
        else:
            goal_items.append(items[row])
            row -= 1
            col -= items[row].weight
    return m[n-1][max_weight], goal_items

def small_test():
    o1 = Object(1, 1)
    o2 = Object(3, 4)
    o3 = Object(4, 5)
    o4 = Object(5, 7)
    value, items = knapsack([o1,o2,o3,o4], 7)
    print(value, sum(map(lambda o: o.weight, items)), items)

def big_test(n,W):
    obj = [Object(x,randint(1,1000)) for x in range(n)]
    value,items = knapsack(obj,W)
    print(value,sum(map(lambda o: o.weight,items)),items)


for x in range(100):
    big_test(100,10)

