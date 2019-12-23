const Node = require("./sumBinaryTree.js");

const utils = {
  smallNumArray: [5, 3, 8, 1, 2, 10, 9, 6, 7, 4],
  largeNumArray: [
    67,
    2,
    891,
    123,
    65,
    32,
    1,
    890,
    6473,
    17,
    478,
    345,
    4,
    8,
    5,
    129367,
    5,
    23,
    789,
    56,
    7
  ],
  makeBinarySearchTree: function makeBST(numArray) {
    const headNode = new Node(numArray[0]);
    numArray.forEach((num, i) => {
      if (i > 0) {
        headNode.addValue(num);
      }
    });
    return headNode;
  }
};

describe("sumBinaryTree", () => {
  describe("Node", () => {
    let largeBST;
    let smallBST;

    beforeEach(() => {
      largeBST = utils.makeBinarySearchTree(utils.largeNumArray);
      smallBST = utils.makeBinarySearchTree(utils.smallNumArray);
    });

    describe("instantiates", () => {
      test("instantiates a new version of the Node class", () => {
        const node = new Node("test");
        expect(node instanceof Node).toBeTruthy();
      });

      test("instantiates with null default value for _value, _left, and _right", () => {
        const result = new Node();
        expect(result._value).toBeNull();
        expect(result._left).toBeNull();
        expect(result._right).toBeNull();
      });
    });

    describe("getValue()", () => {
      test("returns null if the default value was used when instantiating", () => {
        const node = new Node();
        expect(node.getValue()).toBeNull();
      });

      test("returns the value of the node", () => {
        const node = new Node("test");
        expect(node.getValue()).toBe("test");
      });
    });

    describe("addValue()", () => {
      test("adds a single value to the Binary Search Tree", () => {
        const headNode = new Node(1);
        headNode.addValue(2);
        expect(headNode._right._value).toBe(2);
      });

      test("builds a correct large Binary Search Tree", () => {
        const result = largeBST._left._right._left.getValue();
        expect(result).toBe(32);
      });

      test("builds a correct small Binary Search Tree", () => {
        const result = JSON.stringify(smallBST);
        expect(result).toBe(
          '{"_value":5,"_left":{"_value":3,"_left":{"_value":1,"_left":null,"_right":{"_value":2,"_left":null,"_right":null}},"_right":{"_value":4,"_left":null,"_right":null}},"_right":{"_value":8,"_left":{"_value":6,"_left":null,"_right":{"_value":7,"_left":null,"_right":null}},"_right":{"_value":10,"_left":{"_value":9,"_left":null,"_right":null},"_right":null}}}'
        );
      });
    });

    describe("getValuesBetweenNodes()", () => {
      test("should return an empty array when there is no possibility of finding the search value", () => {
        const headNode = new Node(1);
        const result = headNode.getValuesBetweenNodes(5);
        expect(result).toEqual([]);
      });

      test("returns null if no value is passed in to be searched for", () => {
        const headNode = new Node(1);
        const result = headNode.getValuesBetweenNodes();
        expect(result).toBeNull();
      });

      test("returns a small array path of integers from head Node value to search value", () => {
        const result = smallBST.getValuesBetweenNodes(2);
        expect(result).toEqual([5, 3, 1, 2]);
      });

      test("returns a large array path of integers from head Node value to search value", () => {
        const result = largeBST.getValuesBetweenNodes(789);
        expect(result).toEqual([67, 891, 123, 890, 478, 789]);
      });

      test("should return an array path of integers no matter what node it's called on", () => {
        const result = largeBST._left._right.getValuesBetweenNodes(32);
        expect(result).toEqual([65, 32]);
      });
    });

    describe("sumValuesBetweenNodes()", () => {
      test("should return the sum of the node path values from the first node to found value", () => {
        const largeResult = largeBST.sumValuesBetweenNodes(32);
        const smallResult = smallBST.sumValuesBetweenNodes(9);
        expect(largeResult).toBe(166);
        expect(smallResult).toBe(32);
      });

      test("should return null if an empty array of no value is passede in", () => {
        const result = largeBST.sumValuesBetweenNodes();
        expect(result).toBeNull();
      });
    });
  });
});
