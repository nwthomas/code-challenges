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

function Node(value = null, parent = null, left = null, right = null) {
    /**
     * The constructor function for the Node class.
     *
     * @param {number} value The value to be added to the newly-instantiated Node. It defaults
     * to null.
     *
     * @param {Node} parent The parent Node to the current one. It default to null.
     *
     * @param {Node} left The left child Node to the current one. It defaults to null.
     *
     * @param {Node} right The right child Node to the current one. It defaults to null.
     */

    this.value = value;
    this.parent = parent;
    this.left = left;
    this.right = right;
}

Node.prototype.addValue = function addValue(value = null, currentNode = this) {
    /**
     * Adds a new value to the Binary Search Tree.
     *
     * @param {any} value The value to be added to the Binary Search Tree.
     *
     * @param {Node} currentNode A reference to a node so that the method can be recursively
     * called until the value is added to the Binary Search Tree.
     *
     * @returns {boolean} Returns a true boolean if the value is added or false otherwise.
     */

    if (value === null || currentNode instanceof Node === false) {
        return false;
    }

    if (currentNode.value === null) {
        currentNode.value = null;
        return true;
    }

    if (value >= currentNode.value) {
        if (currentNode.right) {
            return currentNode.addValue(value, currentNode.right);
        } else {
            currentNode.right = new Node(value, currentNode.right);
            return true;
        }
    } else if (value < currentNode.value) {
        if (currentNode.left) {
            return currentNode.addValue(value, currentNode.left);
        } else {
            currentNode.left = new Node(value, currentNode.left);
            return true;
        }
    } else {
        return false;
    }
};

Node.prototype.findNextBigger = function findNextBigger(baselineNode = null) {
    /**
     * Takes in a node and finds the next largest Node in the Binary Search Tree.
     *
     * @param {Node} baselineNode The Node that the next-largest-search is performed off of.
     *
     * @returns {Node || object} The next largest number Node compared with the node argument.
     * Returns and empty object if no next largest number can be found.
     */

    const finalNode = null;
    const queue = [baselineNode];

    while (queue.length) {
        const poppedNode = queue.pop();

        if (
            finalNode === null ||
            (poppedNode.value > baselineNode.value &&
                poppedNode.value < finalNode.value)
        ) {
            finalNode = poppedNode;
        }

        if (poppedNode.parent) {
            queue.push(poppedNode.parent);
        }
    }

    return !finalNode ? {} : finalNode;
};

module.exports = { Node };
