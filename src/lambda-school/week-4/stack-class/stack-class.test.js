const Stack = require("./stack-class");

const myStack = new Stack();

test("instantiates a new Stack from class and manipulates the storage and methods", () => {
  expect(myStack.numOfItems()).toBe("There are no items in your stack.");
  myStack.add("first");
  myStack.add("second");
  myStack.add("third");
  expect(myStack.numOfItems()).toBe(3);
  expect(myStack.storage).toEqual(["first", "second", "third"]);
  myStack.remove();
  expect(myStack.storage).toEqual(["first", "second"]);
  myStack.remove();
  expect(myStack.storage).toEqual(["first"]);
  myStack.remove();
  expect(myStack.storage).toEqual([]);
  expect(myStack.numOfItems()).toBe("There are no items in your stack.");
});
