"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Time Complexity: O(L), where L is the length of the linked list.
        Space Complexity: O(1), no extra space is used.
        This function removes the nth node from the end of the linked list.
        """
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        target = length - n
        if target == 0:
            return head.next
        curr = head
        for _ in range(target-1):
            curr = curr.next
        curr.next = curr.next.next
        return head
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)) # [1,2,3,5]
    print(sol.removeNthFromEnd(ListNode(1), 1)) # []
    print(sol.removeNthFromEnd(ListNode(1, ListNode(2)), 1)) # [1]