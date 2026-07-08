# Definition for singly-linked list.
 
class Solution:
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head =ListNode()
        t1 ,t2 ,t3 = list1 ,list2 , head
        while t1 is not None and t2 is not None :
            if t1.val >= t2.val :
                t3.next = t2 
                t2 = t2.next
            else :
                t3.next = t1
                t1 = t1.next
            t3 = t3.next  
        if t1 is not None :
            t3.next = t1
        if t2 is not None :
            t3.next = t2   
        head = head.next  
        return head          

        