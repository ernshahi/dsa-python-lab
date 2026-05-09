"""
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome2(self, head: ListNode) -> bool:
        """
        Idea:
        - Convert the linked list to a list
        - Check if the list is a palindrome
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        items = []
        curr = head
        while curr:
            items.append(curr.val)
            curr = curr.next
        # items == items[::-1]
        left, right = 0, len(items) - 1
        while left < right:
            if items[left] != items[right]:
                return False
            left, right = left + 1, right - 1
        return True
    
    def isPalindrome3(self, head: Optional[ListNode]) -> bool:
        # find middle-slow
        fast = slow = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # reverse second half
        curr, prev = slow, None
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
        
        
if __name__ == "__main__":
    
    sol = Solution()
    print(sol.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
    print(sol.isPalindrome(ListNode(1, ListNode(2))))
    print(sol.isPalindrome(None))
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # items = []
        # curr = head 
        # while curr:
        #     items.append(curr.val)
        #     curr = curr.next
        # # return items == items[::-1]
        # left, right = 0, len(items) - 1
        # while left < right:
        #     if items[left] != items[right]:
        #         return False
        #     left, right = left + 1, right - 1
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr, prev = slow, None
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
