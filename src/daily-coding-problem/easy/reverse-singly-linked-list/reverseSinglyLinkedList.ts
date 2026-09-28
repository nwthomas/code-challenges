/*

Good morning! Here's your coding interview problem for today.

The problem was asked by Google.

Given the head of a singly-linked list, reverse it in-place.

*/

class Node<T = unknown> {
    value: T | null;
    next: Node<T> | null;

    constructor(value: T | null = null) {
        this.value = value;
        this.next = null;
    }
    add(value: T) {
        let current: Node<T> | null = this;
        while (current.next) {
            current = current.next;
        }
        current.next = new Node<T>(value);
        return value;
    }

    get(value: T) {
        let current: Node<T> | null = this;
        while (current) {
            if (current.value === value) {
                return true;
            } else {
                current = current.next;
            }
        }
        return false;
    }

    reverse() {
        if (!this.next) {
            return this;
        }
        let previous: Node<T> | null = null;
        let current: Node<T> | null = this;
        let next: Node<T> | null = this.next;
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
}

export default Node;
