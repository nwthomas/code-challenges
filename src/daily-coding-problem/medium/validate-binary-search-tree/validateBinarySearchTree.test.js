const Node = require("./validateBinarySearchTree.js");

const utils = {
  smallNumArray: [4, 6, 2, 7, 8, 3, 1, 34, 12, 78, 69, 100],
  largeNumArray: [
    6,
    123,
    4,
    67,
    3,
    989,
    7,
    1,
    34,
    2,
    78,
    345,
    23,
    789,
    8,
    19,
    91,
    10,
    11,
    42,
    125378,
    790,
    1752376,
    31,
    83,
    65,
    20
  ],
  createBST: function createBST(numArray) {
    const head = new Node(5);
    numArray.forEach(num => head.addValue(num));
    return head;
  },
  numericSort: function numericSort(arr) {
    return arr.sort((a, b) => a - b);
  }
};

describe("validateBinarySearchTree", () => {
  describe("Node", () => {
    describe("instantiates", () => {
      test("instantiates a new instance of Node", () => {
        const node = new Node(1);
        expect(node instanceof Node).toBeTruthy();
      });

      test("instantiates with null as the node._value if no value is passed in", () => {
        const node = new Node();
        expect(node._value).toBeNull();
      });

      test("instantiates with null as the default value for node._left and node._right", () => {
        const node = new Node();
        expect(node._left).toBeNull();
        expect(node._right).toBeNull();
      });
    });

    describe("getValue()", () => {
      test("retrieves the value of a single Node instance", () => {
        const node = new Node(1);
        expect(node.getValue()).toBe(1);
      });

      test("returns null if node._value is null", () => {
        const node = new Node();
        expect(node.getValue()).toBeNull();
      });
    });

    describe("getAllTreeValues()", () => {
      test("returns null if no instance of Node is passed as the second argument", () => {
        const node = new Node(1);
        const result = node.addValue(4, {});
        expect(result).toBeNull();
      });

      test("returns the values of a small Binary Search Tree", () => {
        const headNode = utils.createBST(utils.smallNumArray);
        const result = headNode.getAllTreeValues();
        expect(result).toEqual(utils.numericSort([...utils.smallNumArray, 5]));
      });

      test("returns the values of a large Binary Search Tree", () => {
        const headNode = utils.createBST(utils.largeNumArray);
        const result = headNode.getAllTreeValues();
        expect(result).toEqual(utils.numericSort([...utils.largeNumArray, 5]));
      });
    });

    describe("addValue()", () => {
      test("adds a single new value to the Binary Search Tree", () => {
        const headNode = new Node(1);
        headNode.addValue(2);
        expect(headNode._right.getValue()).toBe(2);
      });

      test("returns null if the value argument is undefined", () => {
        const headNode = new Node(1);
        const result = headNode.addValue(undefined);
        expect(result).toBeNull();
      });
    });

    describe("validateTree()", () => {
      test("returns null if the node argument passed in is not an instance of Node", () => {
        const node = new Node("test");
        const result = node.validateTree({});
        expect(result).toBeNull();
      });

      test("returns true for a valid small Binary Search Tree", () => {
        const headNode = utils.createBST(utils.smallNumArray);
        const result = headNode.validateTree();
        expect(result).toBeTruthy();
      });

      test("returns true for a valid large Binary Search Tree", () => {
        const headNode = utils.createBST(utils.smallNumArray);
        const result = headNode.validateTree();
        expect(result).toBeTruthy();
      });

      test("return false for an invalid Binary Search Tree", () => {
        const node = new Node(5);
        node._left = new Node(10);
        node._left._right = new Node(1);
        node._right = new Node(-1);
        const result = node.validateTree();
        expect(result).toBeFalsy();
      });
    });
  });
});
