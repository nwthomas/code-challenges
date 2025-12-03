const { palindromePartitioning } = require("./palindromePartitioning.js");

describe("palindromePartitioning", () => {
    it("returns all possible palindrome partitioning of a string", () => {
        const result = palindromePartitioning("aab");
        expect(result).toEqual([
            ["a", "a", "b"],
            ["aa", "b"],
        ]);
    });

    it("returns all possible palindrome partitioning of a string with a single character", () => {
        const result = palindromePartitioning("a");
        expect(result).toEqual([["a"]]);
    });

    it("returns an empty array if the string is empty", () => {
        const result = palindromePartitioning("");
        expect(result).toEqual([[]]);
    });

    it("returns only an array of single chars if no other substrings are a palindrome", () => {
        const result = palindromePartitioning("abc");
        expect(result).toEqual([["a", "b", "c"]]);
    });
});
