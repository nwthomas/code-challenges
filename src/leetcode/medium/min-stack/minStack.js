/*
https://leetcode.com/problems/min-stack/

Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.

Example 1:
Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1

Constraints:
-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks.
*/


class MinStack {
    constructor() {
        this.min = Infinity;
        this.stack = [];
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        if (this.stack.length === 0) {
            this.stack.push(0);
            this.min = val;
        } else {
            this.stack.push(val - this.min);
            if (val < this.min) {
                this.min = val;
            }
        }
    }

    /**
     * @return {void}
     */
    pop() {
        if (this.stack.length === 0) {
            return;
        }
        const top = this.stack.pop();

        if (top < 0) {
            this.min = this.min - top;
        }
    }

    /**
     * @return {number}
     */
    top() {
        const top = this.stack[this.stack.length - 1];
        if (top !== undefined && top > 0) {
            return top + this.min;
        } else {
            return this.min;
        }
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.min;
    }
}

module.exports = { MinStack };