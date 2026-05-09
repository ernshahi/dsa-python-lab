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
        
        This solution uses two pointers with a dummy node.
        First, we move the right pointer n steps ahead.
        Then, we move both pointers until the right pointer reaches the end(None) of the list.
        The left pointer will be at the (n+1)th node from the end of the list.
        We then remove the nth node from the list by setting the next pointer of the left pointer to the next pointer of the left pointer's next pointer.
        Finally, we return the dummy.next node which is the head of the linked list.
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move right n steps ahead
        for _ in range(n):
            right = right.next

        # Move both pointers
        while right:
            left = left.next
            right = right.next

        # Remove node
        left.next = left.next.next

        return dummy.next
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Time Complexity: O(L), where L is the length of the linked list.
        Space Complexity: O(1), no extra space is used.
        This function removes the nth node from the end of the linked list.
        
        First, we calculate the length of the linked list.
        Then, we find the target node to remove by subtracting n from the length.
        If the target node is the head(target == 0), we return the head.next node.
        Otherwise, we iterate through the list until we reach the just before the target node(target-1) and set the next pointer of the target node to the next pointer of the target node's next pointer.
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