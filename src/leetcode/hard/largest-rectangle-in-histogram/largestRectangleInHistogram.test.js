const { largestRectangleArea } = require("./largestRectangleInHistogram");

describe(largestRectangleArea.name, () => {
    test("returns a large combined area", () => {
        const heights = [2, 1, 5, 6, 7, 2, 3];
        const result = largestRectangleArea(heights);
        expect(result).toEqual(15);
    });

    test("returns for a small combined area", () => {
        const heights = [2, 4];
        const result = largestRectangleArea(heights);
        expect(result).toEqual(4);
    });

    test("returns 0 for no values", () => {
        const heights = [];
        const result = largestRectangleArea(heights);
        expect(result).toEqual(0);
    });

    test("returns 0 for heights of 0", () => {
        const heights = [0, 0, 0, 0, 0, 0];
        const result = largestRectangleArea(heights);
        expect(result).toEqual(0);
    });
});
