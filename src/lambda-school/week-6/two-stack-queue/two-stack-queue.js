/*

Good morning! Write a "First In, Last Out" Stack class. Do not modify the Stack class's constructor, or it's length "getter" method.

Once you're done with the F.I.L.O. Stack class, implement a "First In, First Out" Queue class using two of your stacks.

The "queue" data structure is like customers waiting in line at the grocery store. Each customer gets in line, or "enqueue"s. Customers are served in the order they joined the line - "first come, first serve." When they are done paying for their groceries they "dequeue" from the cashier's line.

Here's how you can check if your code works:
const stack = new Stack();
console.log(stack.length);  // <--- 0
stack.add('first'); stack.add('second'); stack.add('third');
console.log(stack.length);  // <--- 3
console.log(stack.storage); // <--- [ 'first', 'second', 'third' ]
console.log('FILO Stack:', stack.remove(), stack.remove(), stack.remove()); // <--- FILO: third second first

const queue = new Queue();
queue.enqueue(1); queue.enqueue(2); queue.enqueue(3);
const val1 = queue.dequeue();
const val2 = queue.dequeue();
const val3 = queue.dequeue();
console.log('FIFO Queue:', val1, val2, val3); // <--- FIFO: 1 2 3

*/

class Stack {
  constructor() {
    this.storage = [];
  }

  add(item) {
    return this.storage.push(item);
  }

  remove() {
    return this.storage.pop();
  }

  get length() {
    return this.storage.length;
  }
}

class Queue {
  constructor() {
    this.stack1 = new Stack();
    this.stack2 = new Stack();
  }

  enqueue(item) {
    return this.stack1.add(item);
  }

  dequeue() {
    if (this.stack2.length === 0) {
      const length = this.stack1.length;
      for (let i = 0; i < length; i++) {
        this.stack2.add(this.stack1.remove());
      }
    }
    return this.stack2.remove();
  }
}

module.exports = { Stack, Queue };
