const { Stack, Queue } = require("./two-stack-queue");

const stack = new Stack();
const queue = new Queue();

test("creates a stack and then adds/removes items from it using FILO method", () => {
  expect(stack.length).toBe(0);
  stack.add("first");
  stack.add("second");
  stack.add("third");
  expect(stack.length).toBe(3);
  expect(stack.storage).toEqual(["first", "second", "third"]);
  expect(stack.remove()).toBe("third");
  expect(stack.remove()).toBe("second");
  expect(stack.remove()).toBe("first");
  queue.enqueue(1);
  queue.enqueue(2);
  queue.enqueue(3);
  expect(queue.dequeue()).toBe(1);
  expect(queue.dequeue()).toBe(2);
  expect(queue.dequeue()).toBe(3);
});
