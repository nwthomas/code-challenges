const { combinationSum } = require('./combinationSum');

describe('combinationSum', () => {
    it('should return all unique combinations sums', () => {
        const result = combinationSum([2,5,6,9], 9);
        expect(result).toEqual([[2, 2, 5], [9]]);
    });

    it("should return a larger array of unique combination sums", () => {
        const result = combinationSum([3,4,5], 16);
        expect(result).toEqual([[3, 3, 3, 3, 4], [3, 3, 5, 5], [3, 4, 4, 5], [4, 4, 4, 4]]);
    });

    it("should return an empty array if no combination sums are possible", () => {
        const result = combinationSum([2,3,5], 1);
        expect(result).toEqual([]);
    });
});