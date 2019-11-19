const { Queue, Stack } = require("./twoStackQueue.js");

describe("Queue()", () => {
  describe("should instantiate a new Queue with two Stacks inside it", () => {
    it("tests that a new Queue has been instantiated", () => {
      const q = new Queue();
      expect(q instanceof Queue).toBeTruthy();
    });

    it("tests that the new Queue has two Stack classes inside it", () => {
      const q = new Queue();
      expect(q.stack1 instanceof Stack).toBeTruthy();
      expect(q.stack2 instanceof Stack).toBeTruthy();
    });
  });

  describe("should enqueue, dequeue, and return the length of the stack", () => {
    it("tests that values have been added to the Queue", () => {
      const q = new Queue();
      q.enqueue(1);
      q.enqueue(2);
      q.enqueue(3);
      expect(q.stack1.stack).toEqual([1, 2, 3]);
    });

    it("tests that values have been removed from the Queue in the correct order", () => {
      const q = new Queue();
      q.enqueue(1);
      q.enqueue(2);
      q.enqueue(3);
      q.enqueue(4);
      q.enqueue(5);
      const val = q.dequeue();
      expect(q.len()).toBe(4);
      expect(val).toBe(1);
      expect(q.getQueue()).toEqual([2, 3, 4, 5]);
    });
  });
});
