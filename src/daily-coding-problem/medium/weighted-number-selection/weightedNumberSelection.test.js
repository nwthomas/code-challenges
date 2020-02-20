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
        // finish
    });

    describe("generateWeightedNumberArray()", () => {
        // finish
    });

    describe("generateWeightedRandomNumber", () => {
        // finish
    });
});
