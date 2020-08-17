const flipChars = require("./flipCharacters.js");

describe("flipChars function", () => {
    test("returns 0 if any of the arguments is of length 0", () => {
        const arg1 = flipChars("", "x", "y");
        const arg2 = flipChars("xyz", "", "y");
        const arg3 = flipChars("xyz", "y", "");
        expect(arg1).toBe(0);
        expect(arg2).toBe(0);
        expect(arg3).toBe(0);
    });

    test("throws a new TypeError when the arguments are not of type string", () => {
        const arg1 = () => flipChars({}, "x", "y");
        const arg2 = () => flipChars("xyz", {}, "y");
        const arg3 = () => flipChars("xyz", "y", {});
        expect(arg1).toThrow(TypeError);
        expect(arg2).toThrow(TypeError);
        expect(arg3).toThrow(TypeError);
    });

    test("returns the correct number of swaps for a short string", () => {
        const result = flipChars("xyxxyxyx", "x", "y");
        expect(result).toBe(4);
    });

    test("returns the correct number of swaps for a long string", () => {
        const result = flipChars("xyxyxyxyxyxyxyxy", "x", "y");
        expect(result).toBe(8);
    });
});
