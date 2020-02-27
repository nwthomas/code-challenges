const isPermutationPalindromePossible = require("./permutationPalindrome.js");

describe("isPermutationPalindrome", () => {
    test("throws a new TypeError if the argument is not a string", () => {
        const result = () => isPermutationPalindromePossible([]);
        expect(result).toThrow(
            TypeError(
                "The argument for isPermutationPalindromePossible must be a string"
            )
        );
    });

    test("returns false if a permutation palindrome is not possible", () => {
        const result = isPermutationPalindromePossible("test");
        expect(result).toBeFalsy();
    });
});
