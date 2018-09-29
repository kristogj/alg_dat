class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        current = self.root
        while current:
            if new_val < current.value:
                if not current.left:
                    current.left = Node(new_val)
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = Node(new_val)
                    return
                current = current.right

    def search(self, find_val):
        current = self.root
        while current:
            if current.value == find_val:
                return True
            elif find_val < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def preorder_print(self):
        stack = [self.root]
        while stack:
            current = stack.pop()
            print(current)
            if current.right: stack.append(current.right)
            if current.left: stack.append(current.left)



# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

tree.preorder_print()

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))


class BST_recursive(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False