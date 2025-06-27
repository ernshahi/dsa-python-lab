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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # li_list = []
        # while head:
        #     li_list.append(head.val)
        #     head = head.next

        # first solution
        # length = len(li_list)
        # if length < 2: return True
        # mid = math.ceil(len(li_list) // 2)
        # if length % 2:
        #     if li_list[:mid] == list(reversed(li_list[mid+1:])):
        #         return True
        #     return False
        # if li_list[:mid] == list(reversed(li_list[mid:])):
        #     return True
        # return False

        # second solution
        # return li_list == li_list[::-1]

        # third solution
        # l, r = 0, len(li_list) - 1
        # while l <= r:
        #     if li_list[l] != li_list[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True

        # find middle-slow
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True





        