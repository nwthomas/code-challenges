const { plusOne } = require("./plusOne");

describe("plusOne", () => {
    it("returns the correct result for the example 1", () => {
        const result = plusOne([1, 2, 3]);
        expect(result).toEqual([1, 2, 4]);
    });

    it("returns the correct result for the example 2", () => {
        const result = plusOne([4, 3, 2, 1]);
        expect(result).toEqual([4, 3, 2, 2]);
    });

    it("returns the correct result for the example 3", () => {
        const result = plusOne([9]);
        expect(result).toEqual([1, 0]);
    });
});