class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return False

        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

# Example usage
head = ListNode(3)
second = ListNode(2)
third = ListNode(0)
fourth = ListNode(-4)
head.next = second
second.next = third
third.next = fourth
fourth.next = second  

solution = Solution()
print(solution.hasCycle(head)) 

head = ListNode(1)
second = ListNode(2)
head.next = second
second.next = head  

print(solution.hasCycle(head))  

head = ListNode(1)

print(solution.hasCycle(head))  
