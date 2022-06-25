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
        
        
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        print(slow.val, fast.val)
        
        prev, curr = None, slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        slow.next  = None
        
        head1, head2 = head, prev
        while head2:
            temp = head1.next
            head1.next = head2
            head1 = head2
            head2 = temp
            
            
            
        # using a array
        
        # if not head.next:
        #     return head
        # lst = []
        # fast = modi = head
        # while fast:
        #     lst.append(fast.val)
        #     fast = fast.next
        # fs=1
        # i, j, l = 1, len(lst)-1, 1
        # while i<=j:
        #     if fs==0:
        #         modi.next =  ListNode(lst[i])
        #         modi = modi.next
        #         fs = 1
        #         i+=1
        #     elif fs==1:
        #         modi.next =  ListNode(lst[j])
        #         modi = modi.next
        #         fs = 0
        #         j-=1