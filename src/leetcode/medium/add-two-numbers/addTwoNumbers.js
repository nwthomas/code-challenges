/*
https://leetcode.com/problems/add-two-numbers

You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

Example 1:
Input: l1 = [1,2,3], l2 = [4,5,6]
Output: [5,7,9]
Explanation: 321 + 654 = 975.

Example 2:
Input: l1 = [9], l2 = [9]
Output: [8,1]

Constraints:
1 <= l1.length, l2.length <= 100.
0 <= Node.val <= 9
*/

class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}

const addTwoNumbers = (l1, l2) => {
    let carriedOne = false;
    let dummy = new ListNode(-Infinity);
    let current = dummy;

    while (l1 || l2) {
        const l1Value = l1 ? l1.val : 0;
        const l2Value = l2 ? l2.val : 0;
        let sum = l1Value + l2Value;

        if (carriedOne) {
            sum += 1;
            carriedOne = false;
        }

        carriedOne = sum >= 10;
        
        if (carriedOne) {
            const leftover = sum % 10;
            current.next = new ListNode(leftover)
        } else {
            current.next = new ListNode(sum);
        }
        
        current = current.next;
        if (l1) {
            l1 = l1.next;
        }
        if (l2) {
            l2 = l2.next;
        }
    }

    if (carriedOne) {
        current.next = new ListNode(1);
    }

    return dummy.next;
}

module.exports = { addTwoNumbers, ListNode };