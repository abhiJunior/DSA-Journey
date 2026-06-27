# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head 
        slow = head 
        if fast == None:
            return False 

        while (fast != None and fast.next != None):
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast:
                return True 
        return False 

        