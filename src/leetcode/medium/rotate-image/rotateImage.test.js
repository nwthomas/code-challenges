const { rotate } = require("./rotateImage");

describe("rotate", () => {
    it("returns the rotated matrix odd numbers", () => {
        const result = rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);
        expect(result).toEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]]);
    });

    it("returns the rotated matrix even numbers", () => {
        const result = rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]);
        expect(result).toEqual([[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]);
    });
});