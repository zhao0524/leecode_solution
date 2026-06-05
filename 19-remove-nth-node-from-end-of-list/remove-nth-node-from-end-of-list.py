# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = head
        arr = []
        while c:
            arr.append(c)
            c = c.next 

        index = len(arr)-n
        if(index == 0):
            return head.next
        elif(index == len(arr)-1):
            arr[index-1].next = None
        else:
            arr[index-1].next = arr[index+1]
            arr[index].next = None
            
        return head
        