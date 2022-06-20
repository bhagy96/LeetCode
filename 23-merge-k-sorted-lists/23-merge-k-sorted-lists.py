# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst = []
        for ll in lists:
            while ll:
                lst.append(ll.val)
                ll = ll.next
        lst = sorted(lst)
        # print(lst)
        head = temp = ListNode()
        for n in lst:
            temp.next = ListNode(n)
            temp = temp.next
        return head.next