"""
143. Reorder List
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        curr, prev = slow.next, None
        slow.next = None 
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        left, right = head, prev
        while right:
            l_next, r_next = left.next, right.next
            left.next = right
            right.next = l_next
            right, left = r_next, l_next
        return head
        

if __name__ == "__main__":
    # Example usage:
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    solution = Solution()
    print(solution.reorderList(head))