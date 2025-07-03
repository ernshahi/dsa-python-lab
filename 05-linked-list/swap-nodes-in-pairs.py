"""
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
 

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
Explanation:


Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Example 4:
Input: head = [1,2,3]
Output: [2,1,3]
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f"{self.val} -> {self.next}"
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            # Swap the nodes
            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next
        return dummy.next
    

if __name__ == "__main__":
    # Example usage:
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    solution = Solution()
    print(solution.swapPairs(head)) # Expected output: 2 -> 1 -> 4 -> 3 -> None

    # 
