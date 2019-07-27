/*

Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints
0 <= input.length <= 100

*/

function validParentheses(parens) {
  if (typeof parens !== "string") return false;
  const queue = new Queue();
  parens.split("").forEach(function(paren) {
    if (paren === ")" && queue.stack[queue.stack.length - 1] === "(") {
      queue.dequeue();
    } else {
      queue.enqueue(paren);
    }
  });
  return queue.stack.length ? false : true;
}

class Queue {
  constructor() {
    this.stack = [];
  }
  enqueue(item) {
    this.stack.push(item);
  }
  dequeue() {
    this.stack.pop();
  }
}

module.exports = validParentheses;
