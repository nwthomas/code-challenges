const getNumberOf1Bits = require("./numberOf1Bits");

describe(getNumberOf1Bits.name, () => {
    test("handles number 0", () => {
        const result = getNumberOf1Bits(0);
        expect(result).toBe(0);
    });

    test("handles larger numbers", () => {
        const result = getNumberOf1Bits(1034510);
        expect(result).toBe(11);
    });
});
