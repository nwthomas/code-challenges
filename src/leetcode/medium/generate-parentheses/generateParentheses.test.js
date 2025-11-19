const { generateParenthesis } = require("./generateParentheses");

const compareUnsortedArrays = (results, expected) => {
    return results.sort().every((value, index) => value === expected.sort()[index]);
}

describe("generateParenthesis", () => {
    it("should return all possible combinations of well-formed parentheses", () => {
        const results = generateParenthesis(3);
        const expected = ["((()))", "(()())", "(())()", "()(())", "()()()"];
        expect(compareUnsortedArrays(results, expected)).toBeTruthy();
    });

    it("should return all possible combinations of well-formed parentheses for n = 1", () => {  
        const results = generateParenthesis(1);
        const expected = ["()"];
        expect(compareUnsortedArrays(results, expected)).toBeTruthy();
    });

    it("should return all possible combinations of well-formed parentheses for n = 0", () => {  
        const results = generateParenthesis(0);
        const expected = [""];
        expect(compareUnsortedArrays(results, expected)).toBeTruthy();
    });
});