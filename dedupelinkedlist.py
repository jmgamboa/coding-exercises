# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        curr_node = head
        while curr_node.next:
            if curr_node.val == curr_node.next.val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
        return head


l3 = ListNode(2)
l2 = ListNode(1, next=l3)
l1 = ListNode(1, next=l2)


x = Solution().deleteDuplicates(l1)

print('here')