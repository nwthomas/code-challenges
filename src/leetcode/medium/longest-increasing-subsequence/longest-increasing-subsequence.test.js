const getLongestIncreasingSubsequence = require("./longest-increasing-subsequence");

describe(getLongestIncreasingSubsequence.name, () => {
    it("should return 1 for all same integers", () => {
        const nums = [8, 8, 8, 8, 8, 8, 8];
        const result = getLongestIncreasingSubsequence(nums);
        expect(result).toBe(1);
    });

    it("should return 4 for increasing subsequence of 4", () => {
        const nums = [1, 4, 3, 5, 8, 2, 1];
        const result = getLongestIncreasingSubsequence(nums);
        expect(result).toBe(4);
    });

    it("should return 1 for only decreasing subsequence", () => {
        const nums = [9, 8, 7, 6, 5, 4, 3, 2, 1];
        const result = getLongestIncreasingSubsequence(nums);
        expect(result).toBe(1);
    });

    it("should return 2 for subsequence only increasing on first and last numbers", () => {
        const nums = [5, 4, 4, 3, 2, 1, 6];
        const result = getLongestIncreasingSubsequence(nums);
        expect(result).toBe(2);
    });
});
