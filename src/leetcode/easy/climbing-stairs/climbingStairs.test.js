const { climbStairs } = require("./climbingStairs.js");

describe("climbStairs", () => {
    it("returns 1 for a step of 1", () => {
        const result = climbStairs(1);
        expect(result).toBe(1);
    });

    it("returns 1 for a step of 0", () => {
        const result = climbStairs(0);
        expect(result).toBe(1);
    });

    it("returns the correct count of ways to reach a step", () => {
        const result = climbStairs(20);
        expect(result).toBe(10946);
    });
});
