const { evalRPN } = require("./reversePolishNotation");

describe("evalRPN", () => {
    it("should return the result of a short expression", () => {
        expect(evalRPN(["2", "1", "+", "3", "*"])).toBe(9);
    });

    it("should return the result of a long expression", () => {
        expect(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])).toBe(22);
    });
});