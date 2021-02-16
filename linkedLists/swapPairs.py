# https://leetcode.com/problems/swap-nodes-in-pairs/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head

        swap = True
        curr_val = head.val
        temp_head = head
        while head:
            curr_val = head.val
            if head.next:
                next_val = head.next.val
            if swap:
                head.val = next_val
                head.next.val = curr_val

            swap = not swap
            head = head.next

        return temp_head



l4 = ListNode(4)
l3 = ListNode(3, next=l4)
l2 = ListNode(2, next=l3)
l1 = ListNode(1, next=l2)

Solution().swapPairs(l1)