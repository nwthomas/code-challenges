const {
    minimumOperations,
} = require("./findMinimumOperationsToMakeAllElementsDivideByThree");

describe("minimumOperations()", () => {
    test("returns the minimum number of operations to make all elements divisible by 3", () => {
        expect(minimumOperations([1, 2, 3, 4])).toBe(3);
    });

    test("returns the minimum number of operations to make all elements divisible by 3", () => {
        expect(minimumOperations([3, 6, 9])).toBe(0);
    });
});
