const getPascalTriangleRow = require("./pascalsTriangle.js");

describe("getPascalTriangleRow", () => {
    test("can return correct row for k = 0", () => {
        const result = getPascalTriangleRow(0);
        expect(result).toEqual([]);
    });

    test("can return correct row for k = 1", () => {
        const result = getPascalTriangleRow(1);
        expect(result).toEqual([1]);
    });

    test("can return correct row for k = 2", () => {
        const result = getPascalTriangleRow(2);
        expect(result).toEqual([1, 1]);
    });

    test("can return correct row for k = 3", () => {
        const result = getPascalTriangleRow(3);
        expect(result).toEqual([1, 2, 1]);
    });

    test("can return correct row for k = 4", () => {
        const result = getPascalTriangleRow(4);
        expect(result).toEqual([1, 3, 3, 1]);
    });

    test("can returns correct row for k = 10", () => {
        const result = getPascalTriangleRow(10);
        expect(result).toEqual([1, 9, 36, 84, 126, 126, 84, 36, 9, 1]);
    });
});
