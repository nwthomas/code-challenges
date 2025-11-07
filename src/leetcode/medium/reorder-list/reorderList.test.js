const { reorderList, ListNode } = require('./reorderList');

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

describe('reorderList', () => {
    it('should reorder the list', () => {
        const head = createList([1, 2, 3, 4]);
        const result = reorderList(head);
        const resultValues = getListValues(result);
        expect(resultValues).toEqual([1, 4, 2, 3]);
    });

    it('should reorder the list with an odd number of nodes', () => {
        const head = createList([1, 2, 3, 4, 5]);
        const result = reorderList(head);
        const resultValues = getListValues(result);
        expect(resultValues).toEqual([1, 5, 2, 4, 3]);
    });

    it('should reorder the list with a single node', () => {
        const head = createList([1]);
        const result = reorderList(head);
        const resultValues = getListValues(result);
        expect(resultValues).toEqual([1]);
    });

    it('should reorder the list with a two nodes', () => {
        const head = createList([1, 2]);
        const result = reorderList(head);
        const resultValues = getListValues(result);
        expect(resultValues).toEqual([1, 2]);
    });
});