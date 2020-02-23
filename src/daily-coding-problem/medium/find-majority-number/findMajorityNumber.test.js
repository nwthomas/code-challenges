const {
    getArrayLength,
    trackNewNumber,
    checkForHalfNumber,
    findMoreThanHalfNumber
} = require("./findMajorityNumber.js");

describe("Find Majority Number", () => {
    describe("getArrayLength()", () => {
        test("returns the length of an even array", () => {
            const result = getArrayLength([1, 2, 3, 4]);
            expect(result).toBe(2);
        });

        test("returns the length of an odd array as even/2 + 1", () => {
            const result = getArrayLength([1, 2, 3, 4, 5]);
            expect(result).toBe(3);
        });
    });

    describe("trackNewNumber()", () => {
        test("adds a number to an empty tracker and returns the tracker", () => {
            const result = trackNewNumber(4, {});
            expect(result).toEqual({ "4": 1 });
        });

        test("increments the value of a key that already exists in the tracker and returns it", () => {
            const result = trackNewNumber(4, { "4": 3 });
            expect(result).toEqual({ "4": 4 });
        });
    });

    describe("checkForHalfNumber()", () => {
        test("returns false if the number does not have a value greater-than-or-equal-to more than half the length", () => {
            const result = checkForHalfNumber(4, { "4": 1 }, 5);
            expect(result).toBeFalsy();
        });

        test("returns true if the number has a value greater-than-or-equal-to more than half the length", () => {
            const result = checkForHalfNumber(10, { "10": 5 }, 4);
            expect(result).toBeTruthy();
        });
    });

    describe("findMoreThanHalfNumber()", () => {
        test("throws a new TypeError if the argument is not an array", () => {
            const result = () => findMoreThanHalfNumber("test");
            expect(result).toThrow(
                TypeError(
                    "You must pass an array of numbers into findMoreThanHalfNumber"
                )
            );
        });

        test("returns null if no number can be found that exists for at least half the length of the array", () => {
            const result = findMoreThanHalfNumber([1, 2, 3, 4, 5, 5, 1, 2, 9]);
            expect(result).toBeNull();
        });

        test("returns a number if it occurs at least half the time in an array", () => {
            const result = findMoreThanHalfNumber([
                1,
                3,
                4,
                1,
                1,
                1,
                2,
                1,
                3,
                1,
                4,
                1
            ]);
            expect(result).toBe(1);
        });
    });
});
