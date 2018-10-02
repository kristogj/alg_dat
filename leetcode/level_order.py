class Node(object):
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children


def levelOrder(root):
    """
    This method is doing a bfs search. Through the algorithm i do the while loop as im used to with bfs
    but instead of popping one element, I iterate over the whole queue. No I have access to the values in all the nodes
    on the same level an are able to organize their children in a new queue.
    :param root: Node
    :return: List[List[int]]
    """
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        temp = []
        next_queue = []
        for node in queue:
            temp.append(node.val)  # For the result list
            for child in node.children:
                next_queue.append(child)  # For the next level of nodes
        res.append(temp)
        queue = next_queue
    return res

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n1.children = [n2,n3,n4]
n2.children = [n5,n6]
n4.children = [n7]

root = n1

print(levelOrder(root))