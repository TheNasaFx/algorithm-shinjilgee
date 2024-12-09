class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}

function hasCycle(head) {
    if (!head || !head.next) {
        return false;
    }

    let slow = head;
    let fast = head.next;
    while (slow !== fast) {
        if (!fast || !fast.next) {
            return false;
        }
        slow = slow.next;
        fast = fast.next.next;
    }

    return true;
}

// Example usage
const head = new ListNode(3);
const second = new ListNode(2);
const third = new ListNode(0);
const fourth = new ListNode(-4);
head.next = second;
second.next = third;
third.next = fourth;
fourth.next = second;  // Creates a cycle

console.log(hasCycle(head));  // Output: true

const head2 = new ListNode(1);
const second2 = new ListNode(2);
head2.next = second2;
second2.next = head2;  // Creates a cycle

console.log(hasCycle(head2));  // Output: true

const head3 = new ListNode(1);

console.log(hasCycle(head3));  // Output: false
