/*
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
*/

class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}

const reorderList = (head) => {
    if (head.next === null) {
        return head;
    }

    // Get pointer for start of second half of linked list
    let slow = head;
    let fast = head.next;
    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // Reverse the order of the second half of the linked list
    let second = slow.next;
    let prev = (slow.next = null);
    while (second !== null) {
        const temp = second.next;
        second.next = prev;
        prev = second;
        second = temp;
    }

    console.log(head, second);

    // Finally, weave two lists (first half normal, second half reversed) together
    let first = head;
    second = prev;
    while (second !== null) {
        const firstNext = first.next;
        const secondNext = second.next;
        first.next = second;
        second.next = firstNext;
        first = firstNext;
        second = secondNext;
    }

    return head;
}

module.exports = { reorderList, ListNode };