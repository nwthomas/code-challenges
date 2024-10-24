const getLongestCommonSubsequence = require("./longest-common-subsequence");

describe(getLongestCommonSubsequence.name, () => {
    it("returns the longest common subsequence for similar words", () => {
        const result = getLongestCommonSubsequence("testing", "testtest");
        expect(result).toBe(4);
    });

    it("returns the longest common subsequence for dissimilar words", () => {
        const result = getLongestCommonSubsequence(
            "nathanthomas",
            "anotherstring",
        );
        expect(result).toBe(5);
    });
});
