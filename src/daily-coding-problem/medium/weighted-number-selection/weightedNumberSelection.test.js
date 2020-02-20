const {
    addZeros,
    findRandomArrayLength,
    generateWeightedNumberArray,
    generateWeightedRandomNumber
} = require("./weightedNumberSelection.js");

describe("Weighted Number Selection", () => {
    describe("addZeros()", () => {
        test("returns the number stripped of '0.' if the length of it is the same as the length argument", () => {
            const result = addZeros(0.4, 1);
            expect(result).toBe(4);
        });

        test("returns extra zeros added to the end of the number if it's shorter than the length argument after being stripped of '0.'", () => {
            const result = addZeros(0.456, 5);
            expect(result).toBe(45600);
        });
    });

    describe("findRandomArrayLength()", () => {
        test("returns the correct length of a future array when an array of float numbers is passed in", () => {
            const result = findRandomArrayLength([0.5, 0.444, 0.9]);
            expect(result).toBe(3);
        });
    });

    describe("generateWeightedNumberArray()", () => {
        test("returns a complete list of numbers weighted by whole integer probabilities", () => {
            const result = generateWeightedNumberArray(
                [1, 2, 3, 4],
                [3, 4, 1, 2]
            );
            expect(result).toEqual([1, 1, 1, 2, 2, 2, 2, 3, 4, 4]);
        });
    });

    describe("generateWeightedRandomNumber", () => {
        test("throws a TypeError when the first argument is not an array", () => {
            const result = () =>
                generateWeightedRandomNumber("test", [0.1, 0.2]);
            expect(result).toThrow(
                TypeError("The first argument must be an array of numbers")
            );
        });

        test("throws a TypeError when the second argument is not an array", () => {
            const result = () =>
                generateWeightedRandomNumber([1, 2, 3], "test");
            expect(result).toThrow(
                TypeError("The second argument must be an array of numbers")
            );
        });

        test("returns a random number chosen from the array passed as the first argument", () => {
            const result = generateWeightedRandomNumber(
                [1, 2, 3, 4],
                [0.02, 0.9, 0.05, 0.03]
            );
            expect(result).toBeOneOf([1, 2, 3, 4]);
        });
    });
});
