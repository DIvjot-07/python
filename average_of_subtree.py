# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.output = 0
        self.sumer(root)
        return self.output

    def sumer(self, node):
        if node is None:
            return (0, 0)

        left_val = self.sumer(node.left)
        right_val = self.sumer(node.right)

        totalsum = left_val[0] + right_val[0] + node.val
        totalcount = left_val[1] + right_val[1] + 1

        average = totalsum // totalcount

        if average == node.val:
            self.output += 1

        return (totalsum, totalcount)
