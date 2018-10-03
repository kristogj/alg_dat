# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        In a Binary Search Tree values to the left are smaller and values to the right are bigger
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return []
        elif root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)