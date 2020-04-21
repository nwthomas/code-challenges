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

    test("handles lowercase Roman numerals being a part of the string", () => {
        const result = convertRomanNumeralToDecimal("MdlxViii");
        expect(result).toBe(1568);
    });

    test("returns the correct answer for a single Roman numeral", () => {
        const result = convertRomanNumeralToDecimal("L");
        expect(result).toBe(50);
    });

    test("returns the correct answer for a medium string of Roman numerals", () => {
        const result = convertRomanNumeralToDecimal("LIIIIX");
        expect(result).toBe(56);
    });

    test("returns the correct answer for a large string of Roman numerals", () => {
        const result = convertRomanNumeralToDecimal("MDMCLCXXXIIIIV");
        expect(result).toBe(1681);
    });
});
