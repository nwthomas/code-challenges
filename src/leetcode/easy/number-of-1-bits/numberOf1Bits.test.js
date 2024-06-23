const getNumberOf1Bits = require("./numberOf1Bits");

describe(getNumberOf1Bits.name, () => {
    test("Handles number 0", () => {
        const result = getNumberOf1Bits(0);
        expect(result).toBe(0);
    });
});
