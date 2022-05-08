const { containsDuplicate } = require("./containsDuplicate.js");

describe("containsDuplicate", () => {
    test("returns false if there are no duplicates", () => {
        const result = containsDuplicate([1, 2, 3, 4, 5]);
        expect(result).toBe(false);
    });

    test("returns true if there are duplicates", () => {
        const result = containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]);
        expect(result).toBe(true);
    });
});
