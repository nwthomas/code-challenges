const {
    createWordCloud,
    splitWords,
    isAlphaChar,
} = require("./wordCloudData.js");

describe("wordCloudData", () => {
    describe("isAlphaChar", () => {
        test("throws new TypeError if the argument is not of type string", () => {
            const result = () => isAlphaChar({});
            expect(result).toThrow(
                TypeError(
                    "The argument for isAlphaChar must be of type string."
                )
            );
        });

        test("returns true boolean if the argument passed in is an alphabet character", () => {
            const result = isAlphaChar("a");
            expect(result).toBe(true);
        });

        test("returns false boolean if the argument passed in is not an alphabet character", () => {
            const result = isAlphaChar("5");
            expect(result).toBe(false);
        });

        test("returns true if an alphabet character is capitalized", () => {
            const result = isAlphaChar("G");
            expect(result).toBe(true);
        });
    });

    describe("splitWords", () => {
        test("throws new TypeError if the argument is not of type string", () => {
            const result = () => splitWords([]);
            expect(result).toThrow(
                TypeError("The argument for splitWords must be of type string.")
            );
        });

        test("splits words in string with lots of punctuation in between", () => {
            const result = splitWords(
                "this is, a test-test! Squirrels are. Devil creatures { lol }."
            );
            expect(result).toEqual([
                "this",
                "is",
                "a",
                "test",
                "test",
                "Squirrels",
                "are",
                "Devil",
                "creatures",
                "lol",
            ]);
        });

        test("returns an empty array if the input argument is an empty string", () => {
            const result = splitWords("");
            expect(result).toEqual([]);
        });
    });

    describe("createWordCloud", () => {
        test("throws new TypeError if the argument is not of type string", () => {
            const result = () => createWordCloud({});
            expect(result).toThrow(
                TypeError(
                    "The argument for createWordCloud must be of type string."
                )
            );
        });

        test("returns an empty object when the string has no length", () => {
            const result = createWordCloud("");
            expect(result).toEqual({});
        });

        test("returns the correct word cloud when a short string is passed in", () => {
            const result = createWordCloud(
                "This is a test string. This is a test!"
            );
            expect(result).toEqual({
                this: 2,
                is: 2,
                a: 2,
                test: 2,
                string: 1,
            });
        });

        test("returns the correct word cloud when a long string is passed in", () => {
            const result = createWordCloud(
                "This is a really long test string to test the functionality of this code. However, there should be lots of punctuation; crazy, right?"
            );
            expect(result).toEqual({
                a: 1,
                be: 1,
                code: 1,
                crazy: 1,
                functionality: 1,
                however: 1,
                is: 1,
                long: 1,
                lots: 1,
                of: 2,
                punctuation: 1,
                really: 1,
                right: 1,
                should: 1,
                string: 1,
                test: 2,
                the: 1,
                there: 1,
                this: 2,
                to: 1,
            });
        });
    });
});
