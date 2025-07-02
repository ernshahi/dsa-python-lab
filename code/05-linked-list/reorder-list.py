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

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        val_only = []
        current = head
        while current:
            val_only.append(current.val)
            current = current.next

        is_even = len(val_only) % 2 == 0
        val_only = list(reversed(val_only))
        val_only = val_only[:len(val_only)//2]

        if is_even: val_only = val_only[:-1]
        current = head
        for val in val_only:
            temp = current.next
            last_node = ListNode(val, temp)
            current.next = last_node
            last_node.next = temp
            current = temp
        
        if is_even: current = current.next
        current.next = None
        return head

if __name__ == "__main__":
    # Example usage:
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    solution = Solution()
    solution.reorderList(head)

    # Print the reordered list
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

        