# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        prev_val = head.val
        prev_node = head
        while head.next:
            if prev_val == head.val:
                prev_node.next = head.next

            prev_node = head
            head = head.next
            prev_val = head.val
        return head


l3 = ListNode(2)
l2 = ListNode(1, next=l3)
l1 = ListNode(1, next=l2)


x = Solution().deleteDuplicates(l1)

print('here')