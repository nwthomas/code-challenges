const {
    NAND,
    AND,
    NOT,
    OR,
    NOR,
    XOR,
    XNOR,
    MUX,
    DEMUX,
} = require("./nand-logic-gates");

describe("the NAND gate library", () => {
    test("NAND() method", () => {
        expect(NAND(1, 1)).toBe(0);
        expect(NAND(1, 0)).toBe(1);
    });

    test("AND() method", () => {
        expect(AND(1, 0)).toBe(0);
        expect(AND(0, 0)).toBe(0);
        expect(AND(1, 1)).toBe(1);
    });

    test("NOT() method", () => {
        expect(NOT(1)).toBe(0);
    });

    test("OR() method", () => {
        expect(OR(1, 0)).toBe(1);
        expect(OR(1, 1)).toBe(1);
        expect(OR(0, 0)).toBe(0);
    });

    test("NOR() method", () => {
        expect(NOR(0, 0)).toBe(1);
        expect(NOR(1, 0)).toBe(0);
        expect(NOR(1, 1)).toBe(0);
    });

    test("XOR() method", () => {
        expect(XOR(1, 1)).toBe(0);
        expect(XOR(0, 0)).toBe(0);
        expect(XOR(1, 0)).toBe(1);
    });

    test("XNOR() method", () => {
        expect(XNOR(0, 0)).toBe(1);
        expect(XNOR(0, 1)).toBe(0);
        expect(XNOR(1, 0)).toBe(0);
        expect(XNOR(1, 1)).toBe(1);
    });

    test("MUX() method", () => {
        expect(MUX(0, 0, 0)).toBe(0);
        expect(MUX(0, 1, 0)).toBe(0);
        expect(MUX(1, 0, 0)).toBe(1);
        expect(MUX(1, 1, 0)).toBe(1);
        expect(MUX(0, 0, 1)).toBe(0);
        expect(MUX(0, 1, 1)).toBe(1);
        expect(MUX(1, 0, 1)).toBe(0);
        expect(MUX(1, 1, 1)).toBe(1);
    });
});
