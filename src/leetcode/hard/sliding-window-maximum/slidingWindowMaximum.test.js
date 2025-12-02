const { slidingWindowMaximum } = require("./slidingWindowMaximum");

describe("slidingWindowMaximum", () => {
    test("returns the correct value for a list of length 1", () => {
        const result = slidingWindowMaximum([10], 1);
        expect(result).toEqual([10]);
    });

    test("returns the correct value for a list of length 3", () => {
        const result = slidingWindowMaximum([1, 3, -1, -3, 5, 3, 6, 7], 3);
        expect(result).toEqual([3, 3, 5, 5, 6, 7]);
    });

    test("returns the correct value for a list of length 4", () => {
        const result = slidingWindowMaximum([1, 3, -1, -3, 5, 3, 6, 7], 4);
        expect(result).toEqual([3, 5, 5, 6, 7]);
    });
});
