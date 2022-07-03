# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = temp = ListNode()
        carry = 0        
        while l1 and l2:
            no = l1.val + l2.val + carry            
            if no>=10:                         
                carry = int(no/10)
                no = no%10
            else:
                carry = 0
            temp.next = ListNode(no)
            temp = temp.next
            l1, l2 = l1.next, l2.next
            
        lst = l1 if l1 else l2
        
        while lst:
            no = lst.val + carry
            if no>=10:          
                carry = int(no/10)
                no = no%10
            else:
                carry = 0
            temp.next = ListNode(no)
            temp = temp.next
            lst = lst.next
        if carry!=0:
            temp.next = ListNode(carry)
            
        return head.next
            
            
        # Using Strings
        
        # sl1,sl2 = '',''
        # while l1:
        #     sl1 += str(l1.val)
        #     l1 = l1.next
        # while l2:
        #     sl2 += str(l2.val)
        #     l2 = l2.next
        # sl1, sl2 = sl1[::-1], sl2[::-1]
        # total = str(int(sl1) + int(sl2))
        # total = total[::-1]
        # head = temp = ListNode()
        # for c in total:
        #     temp.next = ListNode(int(c))
        #     temp = temp.next
        # return head.next
            
            
        