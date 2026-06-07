# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev_group_tail = dummy
        c = head

        while c:
            # Step 1: check if there are k nodes
            kth = c
            for i in range(k - 1):
                kth = kth.next
                if kth is None:
                    return dummy.next

            next_group_head = kth.next

            # Step 2: reverse k nodes
            p = next_group_head
            curr = c

            for i in range(k):
                temp = curr.next
                curr.next = p
                p = curr
                curr = temp

            # Step 3: reconnect
            old_group_head = c
            prev_group_tail.next = kth
            prev_group_tail = old_group_head

            # Step 4: move to next group
            c = next_group_head

        return dummy.next