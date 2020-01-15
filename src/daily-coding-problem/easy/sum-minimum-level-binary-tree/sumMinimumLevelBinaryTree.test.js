const Node = require("./sumMinimumLevelBinaryTree.js");

const utils = {
  smallNumberArray: [10, 9, 2, 6, 4, 10, 11, 3, 7, 8, 1, 2],
  createBinarySearchTree: function createBinarySearchTree(numberArray) {
    const headNode = new Node(numberArray[0]);
    for (let i = 1; i < numberArray.length; i++) {
      headNode.addValue(numberArray[i]);
    }
    return headNode;
  }
};

describe("sumMinimumLevelBinaryTree", () => {
  describe("instantiates", () => {
    test("instantiates a new version of the Binary Search Tree Node", () => {
      const node = new Node();
      expect(node instanceof Node).toBeTruthy();
    });

    test("instantiates with null as the default value", () => {
      const node = new Node();
      expect(node.value).toBeNull();
    });

    test("instantiates with a value if one is given", () => {
      const node = new Node(1);
      const result = node.value;
      expect(result).toBe(1);
    });

    test("instantiates with null as the default values for left and right", () => {
      const node = new Node();
      const leftValue = node.left;
      const rightValue = node.right;
      expect(leftValue).toBeNull();
      expect(rightValue).toBeNull();
    });
  });

  describe("addValue()", () => {
    test("adds a value to the Binary Search Tree", () => {
      const node = new Node(1);
      node.addValue(2);
      const result = node.right.value;
      expect(result).toBe(2);
    });

    test("adds a large number of integers to the Binary Search Tree", () => {
      const headNode = utils.createBinarySearchTree(utils.smallNumberArray);
      const result = headNode.right.right.value;
      expect(result).toBe(11);
    });
  });

  describe("findMinimumSumTreeLevel()", () => {
    test("returns the correct level and sum of that level for a small Binary Search Tree", () => {
      const headNode = new Node(5);
      headNode.addValue(1);
      headNode.addValue(9);
      const result = headNode.findMinimumSumTreeLevel();
      expect(result).toEqual([0, 5]);
    });

    test("returns the correct level and sum of that level for a larger Binary Search Tree", () => {
      const headNode = utils.createBinarySearchTree(utils.smallNumberArray);
      const result = headNode.findMinimumSumTreeLevel();
      expect(result).toEqual([6, 2]);
    });
  });
});
