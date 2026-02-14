# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        pointer=dummy 
        while list1 and list2: #if list 1 and list 2 are not empty 
            if list1.val<=list2.val:
                pointer.next=list1
                list1=list1.next
                pointer=pointer.next
            else:
                pointer.next=list2
                list2=list2.next
                pointer=pointer.next

        if not list1: #if list 1 is empty, we attach list 2 
            pointer.next=list2
        elif not list2: #if list 2 is empty, we attach list 1 
            pointer.next=list1
        
        return dummy.next