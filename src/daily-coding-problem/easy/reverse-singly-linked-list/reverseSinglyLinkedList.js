/*

Good morning! Here's your coding interview problem for today.

The problem was asked by Google.

Given the head of a singly-linked list, reverse it in-place.

*/

function Node(value) {
  this.value = value;
  this.next = null;
}

Node.prototype.add = function(value) {
  let current = this;
  while (current.next) {
    current = current.next;
  }
  current.next = new Node(value);
  return value;
}

Node.prototype.get = function(value) {
  let current = this;
  while (current) {
    if (current.value === value) {
      return true;
    } else {
      current = current.next
    }
  }
  return false;
}

Node.prototype.reverse = function() {
  if (!this.next) {
    return this;
  }
  let previous = null;
  let current = this;
  let next = this.next;
  while (current) {
    current.next = previous;
    previous = current;
    current = next;
    if (current) {
      next = current.next;
    }
  }
  return previous;
}

module.exports = Node;
