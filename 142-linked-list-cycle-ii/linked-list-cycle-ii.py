# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return None 

        slow = head ; fast = head  ; temp = None 
        while fast != None and fast.next != None:
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast:
                temp = fast 
                break 
        if temp == None:
            return None

        slow = head  

        while slow != temp:
            slow = slow.next 
            temp = temp.next 
        return temp

        