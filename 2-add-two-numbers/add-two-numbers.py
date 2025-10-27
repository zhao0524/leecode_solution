# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0 
        result = ListNode(0)
        curr = result
        while l1 or l2 or carry:
            if l1:
                num1 = l1.val
            else:
                num1 = 0 
            if l2:
                num2 = l2.val
            else:
                num2 = 0

            total = num1 + num2 + carry 
            carry = total // 10
# carry will be added the next cycle
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result.next
        