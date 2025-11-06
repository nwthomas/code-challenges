const { coinChange } = require('./coinChange');

describe('coinChange', () => {
    it('should return min number of coins needed from small coin list', () => {
        expect(coinChange([1, 2], 6)).toBe(3);
    });

    it("should return min number of coins needed from large coin list", () => {
        expect(coinChange([1, 2, 5, 10], 101)).toBe(11);
    });

    it("should return -1 if no coins can be used to make up the amount", () => {
        expect(coinChange([2], 3)).toBe(-1);
    });

    it("should return 0 if the amount is 0", () => {
        expect(coinChange([1, 2, 5], 0)).toBe(0);
    });
});