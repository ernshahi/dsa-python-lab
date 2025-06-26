"""
141. Linked List Cycle 
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Example 4:
Input: head = [1,2], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Time: O(n)
        Space: O(1)
        Idea:
        - Use two pointers, slow and fast
        - Slow pointer moves one step at a time
        - Fast pointer moves two steps at a time
        - If there is a cycle, slow and fast will meet at some point
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        """
        Time: O(n)
        Space: O(n)
        Idea:
        - Use a set to track the nodes we have visited
        - If we visit a node that we have already visited, we have a cycle
        - If we reach the end of the list, we don't have a cycle
        """
        visited_nodes = set()
        current = head
        while current and current.next:
            if current in visited_nodes:
                return True
            visited_nodes.add(current)
            current = current.next
        return False
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.hasCycle([3,2,0,-4], 1)) # True
    print(sol.hasCycle([1,2], 0)) # True
    print(sol.hasCycle([1], -1)) # False
    print(sol.hasCycle([1,2], -1)) # False