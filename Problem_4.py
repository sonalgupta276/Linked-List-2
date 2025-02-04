# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = 0
        lenB = 0
        curr = headA
        while curr != None:
            lenA += 1
            curr = curr.next
        curr = headB
        while curr != None:
            lenB += 1
            curr = curr.next
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA

    # Time Complexity : O(n)
    # Space Complexity : O(1)