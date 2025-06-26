

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"

def find_length(head):
    current = head
    length = 0

    while current:
        length += 1
        current = current.next
    return length

def delete_node(head, target):
    if head.val == target:
        return head.next
    
    prev = None
    current = head
    while current:
        if current.val == target:
            prev.next = current.next
            break

        prev = current
        current = current.next
    return head

def fast_slow(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print(head)
print(find_length(head))
# print(delete_node(head, 1))
print(fast_slow(head))

