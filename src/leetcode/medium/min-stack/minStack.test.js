const { MinStack } = require('./minStack.js');

describe('MinStack', () => {
    it('should Infinity for min on empty stack', () => {
        const minStack = new MinStack();
        expect(minStack.getMin()).toBe(Infinity);
    });

    it("should return Infinity for the top on empty stack", () => {
        const minStack = new MinStack();
        expect(minStack.top()).toBe(Infinity);
    });

    it("should correctly return the min value after a variety of numbers pushed to it", () => {
        const minStack = new MinStack();
        minStack.push(1);
        minStack.push(2);
        minStack.push(0);
        minStack.pop();
        minStack.push(-10);
        minStack.push(10);
        minStack.pop();
        expect(minStack.getMin()).toBe(-10);
    });

    it("should correctly return the top after a variety of numbers pushed to it", () => {
        const minStack = new MinStack();
        minStack.push(1);
        minStack.push(2);
        minStack.push(0);
        minStack.push(-100);
        minStack.pop();
        minStack.push(-5);
        minStack.push(100);
        minStack.pop();
        expect(minStack.top()).toBe(-5); 
    });
});