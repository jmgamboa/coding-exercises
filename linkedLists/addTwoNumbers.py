# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l_list = [l1.val]
        l2_list = [l2.val]
        while l1.next:
            l_list.append(l1.next.val)
            l1 = l1.next
        while l2.next:
            l2_list.append(l2.next.val)
            l2 = l2.next




        return l2_list





l3 = ListNode(3)
l2 = ListNode(4, next=l3)
l1 = ListNode(2, next=l2)

l23 = ListNode(4)
l22 = ListNode(6, next=l23)
l21 = ListNode(5, next=l22)
# result should be [8,0,7]

x = Solution().addTwoNumbers(l1, l21)

print(x)