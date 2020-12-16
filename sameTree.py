# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        p_list = []
        q_list = []

        def traverse(node, arr):

            if node.left:
                arr.append(node.val)
                traverse(node.left)
            if node.right:
                arr.append(node.val)
                traverse(node.right)

        p_list = traverse(p)




t3 = TreeNode(3)
t2 = TreeNode(2)
t1 = TreeNode(1, t2, t3)


y3 = TreeNode(3)
y2 = TreeNode(2)
y1 = TreeNode(1, t2, t3)
