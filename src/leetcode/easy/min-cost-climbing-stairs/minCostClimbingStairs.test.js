const { minCostClimbingStairs } = require('./minCostClimbingStairs.js');

describe('minCostClimbingStairs', () => {
    test("returns minimum cost for small staircase", () => {
        const result = minCostClimbingStairs([0, 3, 10, 8, 2, 1, 7]);
        expect(result).toBe(12);
    });

    test("returns minimum cost for large staircase", () => {
        const result = minCostClimbingStairs([10, 1, 30, 4, 8, 26, 7, 45, 81, 10, 0, 4, 67, 10, 9, 7, 3, 1]);
        expect(result).toBe(97);
    });

    test("returns 0 for empty staircase", () => {
        const result = minCostClimbingStairs([]);
        expect(result).toBe(0);
    });
    
    test("returns minimum cost for staircase of length 1", () => {
        const result = minCostClimbingStairs([10]);
        expect(result).toBe(0);
    });
});