# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        res = []
        
        def postorder(node):
            if not node:
                return
            postorder(node.left)     # visit left
            postorder(node.right)    # visit right
            res.append(node.val)     # visit root
        
        postorder(root)
        return res
