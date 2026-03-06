# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tortoise = head
        hare = head

        # detect if cycle exists
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                break
        else:
            return None

        # find cycle start
        hare = head
        while hare != tortoise:
            hare = hare.next
            tortoise = tortoise.next

        return hare
        