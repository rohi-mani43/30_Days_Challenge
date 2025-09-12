class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def height(node):
            if not node:
                return 0
            left_h = height(node.left)
            right_h = height(node.right)

            self.diameter = max(self.diameter, left_h + right_h)
            return 1 + max(left_h, right_h)

        height(root)
        return self.diameter
