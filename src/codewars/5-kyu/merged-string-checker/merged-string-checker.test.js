const isMerge = require("./merged-string-checker.js");

describe("Merged String Checker CodeWars 8kyu code challenge", () => {
    describe("tests that two strings passed as an argument can combine to make the first string argument", () => {
        it("should return true for two short strings arguments a-z and A-Z that form the first string argument", () => {
            expect(isMerge("nathan", "nan", "ath")).toBeTruthy();
        });

        it("should return true for two long strings of characters of all char types that form the first string argument", () => {
            expect(
                isMerge("567SHklAY _*&^", "567lAY *^", "SHk_&"),
            ).toBeTruthy();
        });

        it("should return false for two short strings of characters that do not form the first string argument", () => {
            expect(
                isMerge("abcdefg", "yiosf&^", "98068797IJLHAKG"),
            ).toBeFalsy();
        });

        it("should return false for two long strings of character that do not form the first string argument", () => {
            expect(
                isMerge(
                    "iuAHOGKGAJHHDOGHPOIJPJFN",
                    "^*&FUHPIUYuoHOIGFOPA*(&)&^",
                    "FUiolajhdsof_+*&A906f",
                ),
            ).toBeFalsy();
        });
    });
});
