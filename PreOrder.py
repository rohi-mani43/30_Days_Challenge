# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        res = []
        
        def preorder(node):
            if not node:
                return
            res.append(node.val)    # visit root
            preorder(node.left)     # visit left
            preorder(node.right)    # visit right
        
        preorder(root)
        return res
