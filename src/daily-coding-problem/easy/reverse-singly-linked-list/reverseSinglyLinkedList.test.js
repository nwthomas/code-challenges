const Node = require("./reverseSinglyLinkedList.js");

const utils = {
  addToList: function(sll, limit) {
    for (let i = 1; i <= limit; i++) {
      sll.add(`${i}`);
    }
    return sll;
  }
};

describe("reverseSinglyLinkedList", () => {
  let sll;

  beforeEach(() => {
    sll = new Node("start");
  });

  describe("instantiates", () => {
    test("should successfully instantiate a new Node", () => {
      expect(sll instanceof Node).toBeTruthy();
    });
  });

  describe("add", () => {
    test("should add new nodes to the singly-linked list", () => {
      utils.addToList(sll, 100);
      expect(sll.get("100")).toBeTruthy();
    });

    test("should add any value type to the list", () => {
      const obj = { test: "test" };
      const arr = [1, 2, 3, 4];
      sll.add(obj);
      sll.add(arr);
      sll.add(null);
      sll.add("string");
      sll.add(true);
      expect(sll.get(obj)).toBeTruthy();
      expect(sll.get(arr)).toBeTruthy();
      expect(sll.get(null)).toBeTruthy();
      expect(sll.get("string")).toBeTruthy();
      expect(sll.get(true)).toBeTruthy();
    });
  });

  describe("get", () => {
    test("should retrieve a massive number from the list", () => {
      utils.addToList(sll, 10000);
      expect(sll.get("10000")).toBeTruthy();
    });

    test("should return false if the value is not present in the list", () => {
      utils.addToList(sll, 10000);
      expect(sll.get("-1")).toBeFalsy();
    });
  });

  describe("reverse", () => {
    test("should reverse the singly-linked list", () => {
      utils.addToList(sll, 100);
      const originalHead = sll.value;
      expect(originalHead).toBe("start");
      const newHead = sll.reverse();
      expect(newHead.value).toBe("100");
    });
  });
});
