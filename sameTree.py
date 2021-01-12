# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p_tree: TreeNode, q_tree: TreeNode) -> bool:

        p_list = []
        q_list = []

        def traverse(node, node2):
            if node.left.val != node2.left.val:
                return False

            if node.left and node2.left:
                traverse(node.left, node2.left)

            if node.right.val != node2.right.val:
                return False

            if node.right and node2.right:
                traverse(node.right, node2.right)

            return True



        res = traverse(p_tree, q_tree)
        return res


t3 = TreeNode(1)
t2 = TreeNode(2)
t1 = TreeNode(1, left=t2, right=t3)
import pdb; pdb.set_trace()

y3 = TreeNode(2)
y2 = TreeNode(1)
y1 = TreeNode(1, t2, t3)

Solution().isSameTree(t1, y1)
