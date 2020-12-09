# https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        tmp  = ListNode()
        while l1 and l2 :
            if l1.val > l2.val :
                cntr = l2
                l2 = l2.next
            else :
                cntr = l1
                l1 = l1.next

            if not head :
                head = cntr
                tmp = head
            else:
                tmp.next = cntr
                tmp = tmp.next
        if head :
            if l1 :
                tmp.next = l1
            if l2 :
                tmp.next = l2
        else:
            # head is not init
            if l1 :
                head = l1
            else:
                head = l2
        return head



# l2 = ListNode(val=4, next=None)
# l1 = ListNode(val=2, next=l2)
# l0 = ListNode(val=1, next=l1)

# l5 = ListNode(val=4, next=None)
# l4 = ListNode(val=3, next=l5)
# l3 = ListNode(val=1, next=l4)
# ll2 = [l3, l4, l5]

l1 = [1,2,4]
l2 = [1,3,4]

print(Solution().mergeTwoLists(l1, l2))