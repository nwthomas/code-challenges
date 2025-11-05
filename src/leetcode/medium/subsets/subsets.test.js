const { subsets } = require('./subsets');

describe('subsets', () => {
    it('should return all possible subsets', () => {
        const result = subsets([1, 2, 3]);
        expect(result).toEqual([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]);
    });

    it('should return all possible subsets for an array of length 1', () => {
        const result = subsets([1]);
        expect(result).toEqual([[], [1]]);
    });

    it('should return all possible subsets for an array of length 0', () => {
        const result = subsets([]);
        expect(result).toEqual([[]]);
    });
});