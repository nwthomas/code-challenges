/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35
You can assume each node has a parent pointer.
*/

class Node {
    value: number | null;
    parent: Node | null;
    left: Node | null;
    right: Node | null;

    constructor(
        value: number | null = null,
        parent: Node | null = null,
        left: Node | null = null,
        right: Node | null = null,
    ) {
        this.value = value;
        this.parent = parent;
        this.left = left;
        this.right = right;
    }

    /** Adds a value to the binary search tree, placing duplicates on the right. */
    addValue(value: number | null = null, currentNode: Node = this): boolean {
        if (value === null || !(currentNode instanceof Node)) {
            return false;
        }

        if (currentNode.value === null) {
            currentNode.value = value;
            return true;
        }

        if (value >= currentNode.value) {
            if (currentNode.right) {
                return this.addValue(value, currentNode.right);
            }
            currentNode.right = new Node(value, currentNode);
            return true;
        }

        if (value < currentNode.value) {
            if (currentNode.left) {
                return this.addValue(value, currentNode.left);
            }
            currentNode.left = new Node(value, currentNode);
            return true;
        }

        return false;
    }

    /** Returns the inorder successor, or an empty object if none exists. */
    findNextBigger(
        baselineNode: Node | null = null,
    ): Node | Record<string, never> {
        if (baselineNode === null || baselineNode.value === null) {
            return {};
        }

        if (baselineNode.right) {
            let successor = baselineNode.right;
            while (successor.left) {
                successor = successor.left;
            }
            return successor;
        }

        let current = baselineNode;
        let parent = current.parent;
        while (parent && current === parent.right) {
            current = parent;
            parent = parent.parent;
        }

        return parent ?? {};
    }
}

export { Node };
