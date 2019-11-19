/*

Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.

*/

class Stack {
  constructor() {
    this.stack = [];
    this.length = 0;
  }
  push(value) {
    this.stack.push(value);
    this.length += 1;
  }
  pop() {
    const temp = this.stack.pop();
    this.length -= 1;
    return temp;
  }
  getStack() {
    return this.stack;
  }
  len() {
    return this.length;
  }
}

class Queue {
  constructor() {
    this.stack1 = new Stack();
    this.stack2 = new Stack();
  }
  enqueue(value) {
    this.stack1.push(value);
  }
  dequeue() {
    while (this.stack1.len()) {
      this.stack2.push(this.stack1.pop());
    }
    const temp = this.stack2.pop();
    while (this.stack2.len()) {
      this.stack1.push(this.stack2.pop());
    }
    return temp;
  }
  getQueue() {
    return this.stack1.getStack();
  }
  len() {
    return this.stack1.len();
  }
}

module.exports = { Queue, Stack };
