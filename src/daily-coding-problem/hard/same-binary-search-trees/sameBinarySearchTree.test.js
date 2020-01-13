const Node = require("./sameBinarySearchTrees.js");

const utils = {
  xSmallNumArray: [4, 16, 1],
  smallNumArray: [10, 345, 1, 23, 4, 8, 6, 123, 65, 8, 5],
  createBinarySearchTree: function createBinarySearchTree(numArray) {
    const headNode = new Node(numArray[0]);
    numArray.forEach((num, i) => {
      if (i) {
        headNode.addValue(num);
      }
    });
    return headNode;
  }
};

describe("Node", () => {
  describe("instantiates", () => {
    test("instantiates a new version of the Node class", () => {
      const node = new Node();
      expect(node instanceof Node).toBeTruthy();
    });

    test("instantiates with null as the default value if none is given", () => {
      const node = new Node();
      const result = node.value;
      expect(result).toBeNull();
    });

    test("instantiates with null as the default left/right Node values if none are given", () => {
      const node = new Node();
      const leftResult = node.left;
      const rightResult = node.right;
      expect(leftResult).toBeNull();
      expect(rightResult).toBeNull();
    });

    test("instantiates with a value if one is passed as the first argument", () => {
      const node = new Node("test");
      const result = node.value;
      expect(result).toBe("test");
    });
  });

  describe("addValue()", () => {
    test("adds a value to the current Node if the value is currently null", () => {
      const node = new Node();
      node.addValue("test");
      const result = node.value;
      expect(result).toBe("test");
    });

    test("adds a value to the Binary Search Tree recursively", () => {
      const headNode = new Node(6);
      headNode.addValue(10);
      headNode.addValue(1);
      headNode.addValue(9);
      const rightResult = headNode.right.left.value;
      const leftResult = headNode.left.value;
      expect(rightResult).toBe(9);
      expect(leftResult).toBe(1);
    });

    test("creates a small BinarySearchTree correctly", () => {
      const headNode = utils.createBinarySearchTree(utils.smallNumArray);
      const result = headNode.right.left.right.left.value;
      expect(result).toBe(65);
    });
  });

  describe("verifyTreesAreSame()", () => {
    test("returns true if both Binary Search Trees are identical", () => {
      const tree1 = utils.createBinarySearchTree(utils.smallNumArray);
      const tree2 = utils.createBinarySearchTree(utils.smallNumArray);
      const result = tree1.verifyTreesAreSame(tree2);
      expect(result).toBeTruthy();
    });

    test("returns false if two BinarySearchTrees are not identical", () => {
      const tree1 = utils.createBinarySearchTree(utils.smallNumArray);
      const tree2 = utils.createBinarySearchTree(utils.xSmallNumArray);
      const result = tree1.verifyTreesAreSame(tree2);
      expect(result).toBeFalsy();
    });

    test("returns false if the argument passed in is not an instance of Node", () => {
      const tree1 = utils.createBinarySearchTree(utils.xSmallNumArray);
      const result = tree1.verifyTreesAreSame("test");
      expect(result).toBeFalsy();
    });
  });
});
