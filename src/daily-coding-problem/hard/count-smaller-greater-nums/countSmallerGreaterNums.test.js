const countSmallerGreaterNums = require("./countSmallerGreaterNums.js");

const smallMatrix = [
    [2, 6, 9, 20],
    [3, 6, 27, 48],
    [7, 34, 57, 62],
    [1, 4, 61, 100],
];

const largeMatrix = [
    [4, 20, 45, 74, 400, 524, 607],
    [2, 6, 9, 20, 48, 71, 300],
    [3, 6, 27, 48, 52, 82, 482],
    [7, 34, 57, 60, 467, 500, 617],
    [1, 4, 61, 100, 105, 306, 416],
    [100, 101, 102, 103, 104, 105, 106],
    [84, 89, 401, 482, 901, 1001, 1500],
];

describe("countSmallerGreaterNums", () => {
    test("returns the correct number of smaller/greater numbers in small matrix", () => {
        const result = countSmallerGreaterNums(smallMatrix, 1, 1, 3, 2);
        expect(result).toBe(6);
    });

    test("returns the correct number of smaller/greater numbers in large matrix", () => {
        const result = countSmallerGreaterNums(largeMatrix, 1, 2, 4, 3);
        expect(result).toBe(25);
    });

    test("returns 0 if no smaller/greater numbers exist in matrix", () => {
        const result = countSmallerGreaterNums(smallMatrix, 3, 0, 3, 3);
        expect(result).toBe(0);
    });

    test("returns 0 if the matrix is empty", () => {
        const result = countSmallerGreaterNums([], 0, 0, 1, 1);
        expect(result).toBe(0);
    });

    test("returns 0 if the index arguments are not of type number", () => {
        const result = countSmallerGreaterNums(
            smallMatrix,
            0,
            false,
            4,
            "dude",
        );
        expect(result).toBe(0);
    });
});
