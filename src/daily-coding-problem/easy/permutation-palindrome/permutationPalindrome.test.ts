import { describe, test, expect } from "vitest";

import isPermutationPalindromePossible from "./permutationPalindrome.ts";

describe("isPermutationPalindrome", () => {
    test("throws a new TypeError if the argument is not a string", () => {
        // @ts-expect-error Exercise legacy runtime behavior with an input outside the typed API.
        const result = () => isPermutationPalindromePossible([]);
        expect(result).toThrow(
            TypeError(
                "The argument for isPermutationPalindromePossible must be a string",
            ),
        );
    });

    test("returns false if a permutation palindrome is not possible", () => {
        const result = isPermutationPalindromePossible("test");
        expect(result).toBeFalsy();
    });

    test("returns true if a permutation palindrome is possible", () => {
        const result = isPermutationPalindromePossible("carrace");
        expect(result).toBeTruthy();
    });
});
