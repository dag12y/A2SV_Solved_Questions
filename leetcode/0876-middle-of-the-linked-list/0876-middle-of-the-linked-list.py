# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        start = head
        end = head
        length = 0
        while end:
            length+=1
            end = end.next
        
        for i in range(length // 2):
            start = start.next
        head = start
        return head

        