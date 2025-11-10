const { eraseOverlapIntervals } = require("./nonOverlappingIntervals");

describe("eraseOverlapIntervals", () => {
    it("returns 0 if there are no overlapping intervals", () => {
        const result = eraseOverlapIntervals([[1, 2], [3, 4]]);
        expect(result).toEqual(0);
    });

    it("returns 1 if there is one overlapping interval", () => {
        const result = eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]);
        expect(result).toEqual(1);
    });

    it("returns 2 if there are two overlapping intervals", () => {
        const result = eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]);
        expect(result).toEqual(2);
    });

    it("return 1 if there are overlapping intervals, one that spans most of the array", () => {
        const result = eraseOverlapIntervals([[1, 100], [3, 4], [7, 100]]);
        expect(result).toEqual(1);
    });
});