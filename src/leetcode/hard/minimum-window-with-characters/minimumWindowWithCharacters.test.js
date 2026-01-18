const { minWindow } = require("./minimumWindowWithCharacters");

describe("minWindow", () => {
    it("should return the minimum window substring", () => {
        expect(minWindow("ADOBECODEBANC", "ABC")).toBe("BANC");
    });

    it("should return an empty string if the second string is longer than the first", () => {
        expect(minWindow("ADOBECODEBANC", "ABCDEF")).toBe("");
    });

    it("should return an empty string if the second string is empty", () => {
        expect(minWindow("ADOBECODEBANC", "")).toBe("");
    });

    it("should return an empty string if the first string is empty", () => {
        expect(minWindow("", "ABC")).toBe("");
    });

    it("should return the minimum window substring if the second string is a single character", () => {
        expect(minWindow("ADOBECODEBANC", "A")).toBe("A");
    });

    it("should return the minimum window substring if there's multiple options for the minimum window", () => {
        expect(minWindow("XYABNACYAXUIAYX", "AYAX")).toBe("ACYAX");
    });
});