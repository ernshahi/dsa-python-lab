"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
"""

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"


class Solution:
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = None
        for lst in lists:
            dummy = ListNode()
            current = dummy
            while lst and result:
                if lst.val <= result.val:
                    current.next = lst
                    lst = lst.next
                else:
                    current.next = result
                    result = result.next
                current = current.next
            if result: current.next = result
            if lst: current.next = lst
            result = dummy.next
        return result
    
    def mergeLists(self, l1, l2):
        dummy = ListNode()
        current = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l2: current.next = l2
        if l1: current.next = l1
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) < 1: return None
        
        while len(lists) > 1:
            result = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                result.append(self.mergeLists(l1, l2))
            lists = result
        return lists[0]


if __name__ == "__main__":
    # Example usage:
    # Create a list of ListNode objects to test the mergeKLists function
    node1 = ListNode(1, ListNode(4, ListNode(5)))
    node2 = ListNode(1, ListNode(3, ListNode(4)))
    node3 = ListNode(2, ListNode(6))
    lists = [node1, node2, node3]
    solution = Solution()
    print(solution.mergeKLists(lists))

    print(solution.mergeKLists([]))
    print(solution.mergeKLists([[]]))