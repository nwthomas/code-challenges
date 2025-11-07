const { addTwoNumbers, ListNode } = require("./addTwoNumbers");

function createList(values) {
    const head = new ListNode(values[0]);
    let current = head;
    for (let i = 1; i < values.length; i++) {
        current.next = new ListNode(values[i]);
        current = current.next;
    }
    return head;
}

function getListValues(head) {
    const values = [];
    let current = head;
    while (current) {
        values.push(current.val);
        current = current.next;
    }
    return values;
}

describe("addTwoNumbers", () => {
    it("returns the correct result for same length lists", () => {
        const l1 = createList([1, 2, 3]);
        const l2 = createList([4, 5, 6]);
        const result = addTwoNumbers(l1, l2);
        const resultValues = getListValues(result);
        expect(resultValues).toEqual([5, 7, 9]);
    });

    it("returns the correct result for different length lists", () => {
        const l1 = createList([1, 2, 3]);
        const l2 = createList([4, 5, 6, 7]);
        const result = addTwoNumbers(l1, l2);
        const resultValues = getListValues(result);
        expect(resultValues).toEqual([5, 7, 9, 7]);
    });

    it("returns the correct result for lists with a carry at end", () => {
        const l1 = createList([1, 2, 4]);
        const l2 = createList([4, 5, 6]);
        const result = addTwoNumbers(l1, l2);
        const resultValues = getListValues(result);
        expect(resultValues).toEqual([5, 7, 0, 1]);
    });

    it("returns the correct result for lists with long carry", () => {
        const l1 = createList([8, 9, 9, 9, 9, 9, 1]);
        const l2 = createList([4, 3, 9, 9]);
        const result = addTwoNumbers(l1, l2);
        const resultValues = getListValues(result);
        expect(resultValues).toEqual([2, 3, 9, 9, 0, 0, 2]);
    });
});