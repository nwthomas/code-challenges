const { incrementString, addOneToString } = require("./stringIncrementer.js");

const stringIncremenerError = "The argument for addOneToString must be of type number.";
const incrementStringError = "The argument for incrementString must be of type string.";

describe("stringIncremener", () => {
    describe("addOneToString", () => {
        test("throws new TypeError if argument is not a string", () => {
            const result = () => addOneToString({});
             expect(result).toThrow(TypeError(stringIncremenerError))
        })

        test("throws new TypeError if argument is not a number inside a string", () => {
            const result = () => addOneToString("test");
            expect(result).toThrow(TypeError(stringIncremenerError))
        });

        test("takes in the number 1 as as a string and adds 1 to it", () => {
            const result = addOneToString("1");
            expect(result).toBe("2");
        });

        test("takes in a large number as a string and adds 1 to it", () => {
            const result = addOneToString("3699");
            expect(result).toBe("3700")
        });

        test("returns a number with zeros in front of it", () => {
            const result = addOneToString("000005099");
            expect(result).toBe("000005100");
        });
    });
    
    describe("incrementString", () => {
        test("throws a new TypeError if argument is not of type string", () => {
            const result = () => incrementString({});
            expect(result).toThrow(incrementStringError);
        });

        test("returns an empty string if the argument is an empty string", () => {
            const result = incrementString("");
            expect(result).toBe("");
        });

        test("returns the original string if it does not have a number at the end", () => {
            const result = incrementString("testing");
            expect(result).toBe("testing");
        });

        test("returns a string with a zero at the end that has 1 added to it", () => {
            const result = incrementString("testing0");
            expect(result).toBe("testing1");
        });

        test("returns a full string with a number at the end incremented by 1", () => {
            const result = incrementString("testing000619237");
            expect(result).toBe("testing000619238");
        });
    });
});