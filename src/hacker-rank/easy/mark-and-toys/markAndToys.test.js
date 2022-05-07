const { maximumToys } = require("./markAndToys.js");

describe("markAndToys", () => {
    test("correctly counts a small number of purchases", () => {
        const result = maximumToys([5, 10, 4, 50], 40);
        expect(result).toBe(3);
    });

    test("correctly counts a large number of  purchases", () => {
        const result = maximumToys(
            [90, 1000, 4, 18, 49, 37, 64, 23, 58, 19, 89, 3, 1, 10],
            500,
        );
        expect(result).toBe(13);
    });
});
