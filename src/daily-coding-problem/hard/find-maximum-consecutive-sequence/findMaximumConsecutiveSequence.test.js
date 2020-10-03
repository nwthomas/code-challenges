const findMaximumConsecutiveSequence = require("./findMaximumConsecutiveSequence.js");

describe("findMaximumConsecutiveSequence", () => {
    test("returns the maximum for a short sequence", () => {
        const result = findMaximumConsecutiveSequence([8, 3, 7, 12, 10]);
        expect(result).toBe(2);
    });

    test("returns the maximum for a long sequence", () => {
        const result = findMaximumConsecutiveSequence([
            8,
            3,
            7,
            12,
            10,
            4,
            11,
            9,
            7,
        ]);
        expect(result).toBe(6);
    });
});
