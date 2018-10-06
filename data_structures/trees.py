class Node:

    def __init__(self,value):
        self.value = value
        self.children = []

    def add_child(self,children):
        for child in children:
            if child not in self.children:
                self.children.append(child)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


def init():
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n0.add_child([n1, n2])
    n1.add_child([n3, n4])
    n2.add_child([n5, n6])
    return n0


root = init()


def bfs(root, value):
    queue, path = [root], []
    while queue:
        current = queue.pop(0)
        path.append(current)
        for child in current.children:
            queue.append(child)
    return path


def dfs(root, value):
    stack,path = [root], []
    while stack:
        current = stack.pop()
        path.append(current)
        for child in current.children[::-1]:
            stack.append(child)
    return path


print(bfs(root,2))
print()
print(dfs(root,6))



