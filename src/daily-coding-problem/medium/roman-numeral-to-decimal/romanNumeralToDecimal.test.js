const convertRomanNumeralToDecimal = require("./romanNumeralToDecimal.js");

describe("Roman Numeral to Decimal", () => {
    test("throws an error if the type of argument is not a string", () => {
        const result = () => convertRomanNumeralToDecimal({});
        expect(result).toThrow(
            TypeError(
                "The argument for convertRomanNumeralToDecimal must be a string"
            )
        );
    });

    test("throws an error if one of the characters is not a Roman numeral", () => {
        const result = () => convertRomanNumeralToDecimal("ABKGHAKHJDG");
        expect(result).toThrow(
            Error(
                "All characters input into convertRomanNumeralToDecimal must be valid Roman numerals"
            )
        );
    });

    test("returns the correct answer for a single Roman numeral", () => {
        const result = convertRomanNumeralToDecimal("L");
        expect(result).toBe(50);
    });
});
