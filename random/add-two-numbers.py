"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
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
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(max(M, N)), where M and N are the lengths of the two linked lists.
        Space Complexity: O(1), no extra space is used.

        This function adds two numbers represented by linked lists and returns the sum as a linked list.
        """
        num1 = num2 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
            
        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        result = int(num1[::-1]) + int(num2[::-1])
        head, current = None, None
        for num in str(result)[::-1]:
            node = ListNode(int(num))
            if current:
                current.next = node
                current = current.next
            else:
                head = current = node
        return head
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(max(M, N)), where M and N are the lengths of the two linked lists.
        Space Complexity: O(1), no extra space is used.

        This function adds two numbers represented by linked lists and returns the sum as a linked list.
        """
        num1 = num2 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
            
        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        result = int(num1[::-1]) + int(num2[::-1])
        head, current = None, None
        for num in str(result)[::-1]:
            node = ListNode(int(num))
            if current:
                current.next = node
                current = current.next
            else:
                head = current = node
        return head


    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next
        

if __name__ == "__main__":
    # Example usage
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    
    solution = Solution()
    print(solution.addTwoNumbers(l1, l2)) # [7,0,8]

    l1 = ListNode(0)
    l2 = ListNode(0)
    print(solution.addTwoNumbers(l1, l2)) # [0]

    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    print(solution.addTwoNumbers(l1, l2)) # [8,9,9,9,0,0,0,1]

