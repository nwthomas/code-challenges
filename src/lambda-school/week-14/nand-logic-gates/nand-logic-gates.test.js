const { NAND, AND, NOT, OR, XOR } = require("./nand-logic-gates");

describe("the NAND gate library", () => {
    describe("NAND() method", () => {
        test("returns 0 if both inputs are truthy and 1 otherwise", () => {
            expect(NAND(1, 1)).toBe(0);
            expect(NAND(1, 0)).toBe(1);
        });
    });

    describe("AND() method", () => {
        expect(AND(1, 0)).toBe(0);
        expect(AND(0, 0)).toBe(0);
        expect(AND(1, 1)).toBe(1);
    });

    describe("NOT() method", () => {
        expect(NOT(1)).toBe(0);
    });

    describe("OR() method", () => {
        expect(OR(1, 0)).toBe(1);
        expect(OR(1, 1)).toBe(1);
        expect(OR(0, 0)).toBe(0);
    });

    describe("XOR() method", () => {
        expect(XOR(1, 1)).toBe(0);
        expect(XOR(0, 0)).toBe(0);
        expect(XOR(1, 0)).toBe(1);
    });
});
