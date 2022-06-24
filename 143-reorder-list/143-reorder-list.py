# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head.next:
            return head
        lst = []
        fast = modi = head
        while fast:
            lst.append(fast.val)
            fast = fast.next
        fs=1
        i, j, l = 1, len(lst)-1, 1
        while i<=j:
            if fs==0:
                modi.next =  ListNode(lst[i])
                modi = modi.next
                fs = 1
                i+=1
            elif fs==1:
                modi.next =  ListNode(lst[j])
                modi = modi.next
                fs = 0
                j-=1
        # return modi
            
            
            
#         lst = []
#         fast = og = modi = head
#         while fast:
#             lst.append(fast.val)
#             fast = fast.next
#         fs=0
#         j, l = len(lst)-1, 1
#         while l!=len(lst):
#             if fs==0:
#                 og = modi.next
#                 modi.next =  ListNode(lst[j])
#                 modi = modi.next
#                 fs = 1
#                 j-=1
#                 print(l,og.val)    
#             elif fs==1 and og:
#                 modi.next = ListNode(og.val)
#                 modi = modi.next
#                 fs = 0
#             l+=1
        
        
#         lst = []
#         fast = modi = head
#         while fast:
#             lst.append(fast.val)
#             fast = fast.next
#         print(lst)
#         # for i in range(len(lst)-1, -1, -1):
#             # print(lst[i])
#         L = len(lst)
#         i,j  = 0, L-1
#         l = 1
#         while i<j:
#             print(i,j,modi.val, lst[j])
#             l-=1
#             temp = modi.next
#             modi.next = ListNode(lst[j])
#             l+=3
#             print(l)
#             if l>=L:
#                 break
#             modi.next.next  = temp
            
#             modi = temp
#             i+=1
#             j-=1
    
#         # old_modi.next = None
#         # old_modi.next = ListNode(modi.val)
#         # print(old_modi.next.val)
        # return head
        