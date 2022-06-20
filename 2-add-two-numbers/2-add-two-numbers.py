# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sl1,sl2 = '',''
        # while list1 and list2:
        #     sl1 += list1.val
        #     sl2 += list2.val
        # if list1:
        while l1:
            sl1 += str(l1.val)
            l1 = l1.next
        while l2:
            sl2 += str(l2.val)
            l2 = l2.next
        sl1, sl2 = sl1[::-1], sl2[::-1]
        total = str(int(sl1) + int(sl2))
        total = total[::-1]
        # print(total[0])
        head = temp = ListNode()
        # temp = ListNode()
        # head  = ListNode(total[0], temp)
        for c in total:
            temp.next = ListNode(int(c))
            temp = temp.next
        return head.next
            
            
        