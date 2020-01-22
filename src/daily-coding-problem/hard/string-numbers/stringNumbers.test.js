const isStringANumber = require("./stringNumbers.js");

describe("isStringANumber()", () => {
    test("returns false if no argument is given", () => {
        const result = isStringANumber();
        expect(result).toBeFalsy();
    });

    test("returns false if an empty string is given as an argument", () => {
        const result = isStringANumber("");
        expect(result).toBeFalsy();
    });

    test("returns false if a string of letter chars is given as an argument", () => {
        const result = isStringANumber("asdfasdfasdf");
        expect(result).toBeFalsy();
    });

    test("returns false if a negative char is passed by itself as an argument", () => {
        const result = isStringANumber("-");
        expect(result).toBeFalsy();
    });

    test("returns false when a non-e letter and number char are given in a single string argument", () => {
        const result = isStringANumber("a -123");
        expect(result).toBeFalsy();
    });

    test("returns true when a number is given as an argument inside a string", () => {
        const result = isStringANumber("1000");
        expect(result).toBeTruthy();
    });

    test("returns true when a negative char is given in front of a number in a string", () => {
        const result = isStringANumber("-11233");
        expect(result).toBeTruthy();
    });

    test("returns true when a number is given in the form of scientific notation", () => {
        const result = isStringANumber("123e123");
        expect(result).toBeTruthy();
    });

    test("returns true when a float number is given inside a string as an argument", () => {
        const result = isStringANumber("+10.364829");
        expect(result).toBeTruthy();
    });
});
