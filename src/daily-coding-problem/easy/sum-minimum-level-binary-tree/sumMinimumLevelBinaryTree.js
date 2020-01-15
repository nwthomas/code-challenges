/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a binary tree, return the level of the tree with minimum sum.
*/

function Node(value = null, left = null, right = null) {
  /**
   * Instantiates a new Node for a Binary Search Tree
   *
   * @param {number} value The value to be stored in the Node instance. It defaults to null.
   *
   * @param {Node} left The left value Node of the Binary Search Tree. It defaults to null.
   *
   * @param {Node} right The right value Node of the Binary Search Tree. It defaults to null.
   */

  if (typeof value !== "number" && value !== null) {
    throw new TypeError("The value being added must be a number.");
  }
  this.value = value;
  this.left = left;
  this.right = right;
}

Node.prototype.addValue = function addValue(value = null, currentNode = this) {
  /**
   * Inserts a new value into the Binary Search Tree
   *
   * @param {number} value The value to be stored in the Binary Search Tree. It defaults to null.
   *
   * @param {Node} currentNode The current node being referenced by the addValue method. This
   * parameter is used to recursively call the method until the value can be added to the Binary
   * Search Tree.
   *
   * @returns {boolean} Returns true if the value is added or else false.
   */

  if (typeof value !== "number" && value !== null) {
    throw new TypeError("The value being added must be a number.");
  }
  if (currentNode.value === null) {
    currentNode.value = value;
    return true;
  } else if (value >= currentNode.value) {
    if (currentNode.right) {
      return currentNode.addValue(value, currentNode.right);
    } else {
      currentNode.right = new Node(value);
      return true;
    }
  } else if (value < currentNode.value) {
    if (currentNode.left) {
      return currentNode.addValue(value, currentNode.left);
    } else {
      currentNode.left = new Node(value);
      return true;
    }
  } else {
    return false;
  }
};

Node.prototype.findMinimumSumTreeLevel = function findMinimumSumTreeLevel() {
  /**
   * Returns the level and the sum of the numbers of the minimum sum Binary Search Tree level
   *
   * @returns {array} Returns an array with two indexed positions; the first is the
   * sum of all numbers from that level, and the second is the level that the
   * minimum sum was found in (0 indexed from the root Node level)
   */

  const queue = [[this, 0]];
  const tracker = {};
  let maxLevels = 0;
  while (queue.length) {
    const currentNode = queue.shift();
    const newLevel = currentNode[1] + 1;
    tracker[currentNode[1]]
      ? (tracker[currentNode[1]] += currentNode[0].value)
      : (tracker[currentNode[1]] = currentNode[0].value);
    if (currentNode[0].left) {
      queue.push([currentNode[0].left, newLevel]);
    }
    if (currentNode[0].right) {
      queue.push([currentNode[0].right, newLevel]);
    }
    if (currentNode.left || currentNode.right) {
      newLevel > maxLevels && maxLevels++;
    }
  }
  const trackerArray = Object.entries(tracker);
  const minimumLevelSum = trackerArray.reduce((accum, current) => {
    const levelSumRecord = [Number(current[0]), current[1]];
    if (!accum.length) {
      return levelSumRecord;
    } else {
      return current[1] < accum[1] ? levelSumRecord : accum;
    }
  }, []);
  return minimumLevelSum;
};

module.exports = Node;
