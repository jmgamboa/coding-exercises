# https://leetcode.com/problems/range-sum-of-bst/

class Solution1:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        targets = []

        def recurse(root):
            if root:
                if root.val >= low and root.val <= high:
                    targets.append(root.val)
                if root.val > low:
                    recurse(root.left)
                if root.val < high:
                    recurse(root.right)

        recurse(root)


        return sum(targets)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# optimized iterative
class Solution2:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        ans = 0
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans

# optimized dfs
class Solution3(object):
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans


t9 = TreeNode(val=6)
t8 = TreeNode(val=1)
t7 = TreeNode(val=7, left=t9)
t6 = TreeNode(val=3, left=t8)
t5 = TreeNode(val=5, left=t6, right=t7)
t4 = TreeNode(val=13)
t3 = TreeNode(val=18)
t2 = TreeNode(val=15, left=t4, right=t3)
t1 = TreeNode(val=10, left=t5, right=t2)

print(Solution1().rangeSumBST(t1, 6, 10))