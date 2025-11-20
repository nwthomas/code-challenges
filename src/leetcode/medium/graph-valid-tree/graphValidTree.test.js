const { validTree } = require('./graphValidTree.js');

describe('Graph Valid Tree', () => {
    it('returns true if the edges make up a small valid tree', () => {
        expect(validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])).toBe(true);
    });

    it('returns true if the edges make up a large valid tree', () => {
        expect(validTree(20, [[0, 1], [1, 2], [2, 3], [3, 4], [0, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19]])).toBe(true);
    });

    it("returns false if all nodes are not connected", () => {
        expect(validTree(3, [])).toBe(false);
    })

    it('returns false if the edges do not make up a valid tree', () => {
        expect(validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])).toBe(false);
    });

    it("returns false when the edges form a loop", () => {
        expect(validTree(5, [[0, 1], [1, 0]])).toBe(false);
    });
});