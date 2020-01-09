const Node = require("./findTreePath.js");

const utils = {
  smallArray: [
    6,
    2,
    9,
    3,
    8,
    3,
    1,
    345,
    56,
    123,
    456,
    1234,
    68,
    234,
    435,
    12,
    31
  ],
  createBinarySearchTree: function createBST(arr) {
    const headNode = new Node(arr[0]);
    for (let i = 1; i < arr.length; i++) {
      headNode.addValue(arr[i]);
    }
    return headNode;
  }
};

describe("Node", () => {
  describe("instantiates", () => {
    test("instantiates a new version of Node", () => {
      const node = new Node();
      expect(node instanceof Node).toBeTruthy();
    });

    test("instantiates with a null value as default", () => {
      const node = new Node();
      const result = node._value;
      expect(result).toBeNull();
    });

    test("instantiates with null as the _left and _right Node values as default", () => {
      const node = new Node();
      const leftValue = node._left;
      const rightValue = node._right;
      expect(leftValue).toBeNull();
      expect(rightValue).toBeNull();
    });

    test("instantiates with a value if one is given", () => {
      const node = new Node("test");
      const result = node._value;
      expect(result).toBe("test");
    });

    test("instantiates with a left and right node if they are given as arguments", () => {
      const leftNode = new Node();
      const rightNode = new Node();
      const node = new Node(undefined, leftNode, rightNode);
      const leftResult = node._left === leftNode;
      const rightResult = node._right === rightNode;
      expect(leftResult).toBeTruthy();
      expect(rightResult).toBeTruthy();
    });
  });

  describe("getValue()", () => {
    test("returns null if no value has been passed", () => {
      const node = new Node();
      const result = node.getValue();
      expect(result).toBeNull();
    });

    test("returns the value added to the Node", () => {
      const node = new Node("test");
      const result = node.getValue();
      expect(result).toBe("test");
    });
  });

  describe("addValue()", () => {
    test("adds a value the current Node if value is null", () => {
      const node = new Node();
      const initialResult = node.getValue();
      expect(initialResult).toBeNull();
      node.addValue(4);
      const finalResult = node.getValue();
      expect(finalResult).toBe(4);
    });

    test("returns true if the value is added successfully", () => {
      const node = new Node(10);
      const result = node.addValue(4);
      expect(result).toBeTruthy();
    });

    test("returns false if no value is given", () => {
      const node = new Node(1);
      const result = node.addValue();
      expect(result).toBeFalsy();
    });

    test("returns false if the type of value given is not a number", () => {
      const node = new Node(10);
      const result = node.addValue("test");
      expect(result).toBeFalsy();
    });

    test("adds a series of values to the BinarySearchTree correctly", () => {
      const headNode = utils.createBinarySearchTree(utils.smallArray);
      const result = headNode._right._right._right._right.getValue();
      expect(result).toBe(1234);
    });
  });

  describe("getLeafPaths()", () => {
    test("returns an empty array if no paths can be found", () => {
      const node = new Node();
      const result = node.getLeafPaths();
      expect(result).toEqual([]);
    });

    test("returns the correct path for a miniscule Binary Search Tree", () => {
      const headNode = new Node(10);
      headNode.addValue(15);
      headNode.addValue(8);
      headNode.addValue(17);
      headNode.addValue(12);
      const result = headNode.getLeafPaths();
      expect(result).toEqual([
        [10, 8],
        [10, 15, 12],
        [10, 15, 17]
      ]);
    });

    test("returns an array of arrays of all possible paths to leaf paths in a small Binary Search Tree", () => {
      const headNode = utils.createBinarySearchTree(utils.smallArray);
      const result = headNode.getLeafPaths();
      expect(result).toEqual([
        [6, 2, 1],
        [6, 2, 3, 3],
        [6, 9, 8],
        [6, 9, 345, 56, 12, 31],
        [6, 9, 345, 56, 123, 68],
        [6, 9, 345, 56, 123, 234],
        [6, 9, 345, 456, 435],
        [6, 9, 345, 456, 1234]
      ]);
    });
  });
});
