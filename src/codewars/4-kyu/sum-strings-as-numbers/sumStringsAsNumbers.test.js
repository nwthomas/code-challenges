const sumStrings = require("./sumStringsAsNumbers.js");

describe("sumStrings", () => {
    test("adds two single character digits together", () => {
        const result = sumStrings("5", "8");
        expect(result).toBe("13");
    });

    test("adds two long number strings together", () => {
        const result = sumStrings("4876123", "8612879");
        expect(result).toBe("13489002");
    });

    test("adds two strings together that are of different lengths", () => {
        const result = sumStrings("34", "1111111");
        expect(result).toBe("1111145");
    });
});
