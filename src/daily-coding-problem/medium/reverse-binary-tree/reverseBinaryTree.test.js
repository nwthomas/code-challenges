const {
  ReverseBinaryTreeHelper: RBT,
  Node
} = require("./reverseBinaryTree.js");
const jsonTree = require("./data.json");

const utils = {
  numArray: [4, 6, 2, 7, 8, 3, 1, 34, 12, 78, 69, 100],
  createBST: function createBST() {
    const head = new Node(5);
    utils.numArray.forEach(num => head.addValue(num));
    return head;
  },
  numericSort: function numericSort(arr) {
    return arr.sort((a, b) => a - b);
  }
};

describe("reverseBinaryTree", () => {
  describe("Node", () => {
    let head;

    beforeEach(() => {
      head = utils.createBST();
    });

    describe("instantiates", () => {
      test("should instantiate a new Node class", () => {
        const node = new Node();
        expect(node instanceof Node).toBeTruthy();
      });

      test("should instantiate with a null default value if none is passed in as an argument", () => {
        const node = new Node();
        expect(node._value).toBeNull();
      });

      test("should instantiate with a value if one is passed in as an argument", () => {
        const node = new Node("test");
        expect(node._value).toBe("test");
      });
    });

    describe("getTree()", () => {
      test("should return a small Binary Search Tree in stringified form", () => {
        const headNode = new Node(10);
        headNode.addValue(5);
        headNode.addValue(21);
        const result = headNode.getTree();
        expect(result).toEqual(
          JSON.stringify({
            _value: 10,
            _left: { _value: 5, _left: null, _right: null },
            _right: {
              _value: 21,
              _left: null,
              _right: null
            }
          })
        );
      });

      test("should return a large Binary Search Tree in stringified form", () => {
        expect(head.getTree()).toEqual(jsonTree);
      });
    });

    describe("getValue()", () => {
      test("should return the Node's value when the getValue() method is invoked", () => {
        const node = new Node("test");
        expect(node.getValue()).toBe("test");
      });

      test("should return null when no value has been passed into the constructor function", () => {
        const node = new Node();
        expect(node.getValue()).toBeNull();
      });
    });

    describe("getAllValues()", () => {
      test("should get all the values from a Binary Search Tree", () => {
        const values = head.getAllValues();
        expect(utils.numericSort(values)).toEqual(
          utils.numericSort([...utils.numArray, 5])
        );
      });

      test("should return empty array if no values have been added to BST yet", () => {
        const headNode = new Node();
        const result = headNode.getAllValues();
        expect(result).toEqual([]);
      });

      test("should return null if a non-Node is passed as second argument", () => {
        const headNode = new Node(1);
        expect(headNode.getAllValues("test1", "test2")).toBeNull();
      });
    });

    describe("findValue()", () => {
      test("should return true if a value is present in the Binary Search Tree", () => {
        const isTwoPresent = head.findValue(2);
        const isFivePresent = head.findValue(5);
        expect(isTwoPresent).toBeTruthy();
        expect(isFivePresent).toBeTruthy();
      });

      test("should return false if a value is not present in the Binary Search Tree", () => {
        const isTwentyPresent = head.findValue(20);
        expect(isTwentyPresent).toBeFalsy();
      });

      test("should return null if the value passed into the findValue method is not an instance of Node", () => {
        const headNode = new Node("test");
        // these two lines run as truthy but fail the if statement in findValue() since they !== new Node()
        headNode._left = ["test"];
        headNode._right = { test: "test" };
        const result = headNode.findValue("this value cannot be found");
        expect(result).toBeNull();
      });

      test("should return null if the search value passed into findValue is undefined", () => {
        const result = head.findValue();
        expect(result).toBeNull();
      });
    });

    describe("addValue()", () => {
      test("should successfully add a value to a Binary Search Tree", () => {
        const num = 61278396128736;
        head.addValue(num);
        const result = head.findValue(num);
        expect(result).toBeTruthy();
      });

      test("should successfully find every value created in the utils.createBST helper function", () => {
        utils.numArray.forEach(num => {
          const result = head.findValue(num);
          expect(result).toBeTruthy();
        });
      });

      test("should return null if the value passed in as the node is not an instance of Node", () => {
        // these two lines run as truthy but fail the if statement in findValue() since they !== new Node()
        const headNode = new Node(1);
        headNode._left = { test: "test" };
        headNode._right = ["test"];
        const result = headNode.addValue(58);
        expect(result).toBeNull();
      });

      test("should return null if the value to be added passed into the addValue function is undefined", () => {
        const result = head.addValue();
        expect(result).toBeNull();
      });
    });
  });
});
