const countBits = require("./countingBits");

describe(countBits.name, () => {
    test("handles small n", () => {
        const result = countBits(4);
        expect(result).toEqual([0, 1, 1, 2, 1]);
    });

    test("handles large n", () => {
        const result = countBits(50);
        expect(result).toEqual([
            0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3,
            4, 2, 3, 3, 4, 3, 4, 4, 5, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4,
            4, 5, 2, 3, 3,
        ]);
    });
});
