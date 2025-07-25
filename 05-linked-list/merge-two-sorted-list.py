"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:   
        return f"{self.val} -> {self.next}"

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1 is None: current.next = list2
        if list2 is None: current.next = list1
        return dummy.next



if __name__ == "__main__":
    # Example usage:
    # Create two linked lists to test the mergeTwoLists function
    node1 = ListNode(1, ListNode(2, ListNode(4)))
    node2 = ListNode(1, ListNode(3, ListNode(4)))
    
    solution = Solution()
    print(solution.mergeTwoLists(node1, node2))


    # Test with empty lists
    print(solution.mergeTwoLists(None, None))  # Should return None
    print(solution.mergeTwoLists(None, ListNode(0)))  # Should return ListNode(0)