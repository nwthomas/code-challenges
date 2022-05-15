const { isPalindrome } = require("./validPalindrome.js");

describe("isPalindrome", () => {
    it("returns true if a palindrome", () => {
        const result = isPalindrome("A man, a plan, a canal: Panama");
        expect(result).toBe(true);
    });

    it("returns false if not a palindrome", () => {
        const result = isPalindrome("lkajsdfyugkahjsdf");
        expect(result).toBe(false);
    });

    it("returns true for a string filled with space chars", () => {
        const result = isPalindrome("     ");
        expect(result).toBe(true);
    });

    it("returns true for an empty string", () => {
        const result = isPalindrome("");
        expect(result).toBe(true);
    });
});
