const { merge } = require("./mergeIntervals");

describe("merge", () => {
    it("returns the original list if there are no overlaps", () => {
        const result = merge([[1, 2], [3, 4]]);
        expect(result).toEqual([[1, 2], [3, 4]]);
    });

    it("merges intervals that overlap", () => {
        const result = merge([[1, 3], [2, 6], [10, 11]]);
        expect(result).toEqual([[1, 6], [10, 11]]);
    });

    it("merges intervals that overlap as same number", () => {
        const result = merge([[1, 3], [3, 6]]);
        expect(result).toEqual([[1, 6]]);
    });

    it("returns merged intervals that were originally unsorted", () => {
        const result = merge([[15, 18], [1, 3], [2, 6], [8, 10]]);
        expect(result).toEqual([[1, 6], [8, 10], [15, 18]]);
    });
});