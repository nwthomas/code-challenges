const matrixAddition = require("./matrixAddition.js");

describe("matrixAddition function", () => {
    test("returns an empty array when the first argument has no length", () => {
        const result = matrixAddition(
            [],
            [
                [0, 1, 2],
                [3, 4, 5],
            ]
        );
        expect(result).toEqual([]);
    });

    test("returns an empty array when the second argument has no length", () => {
        const result = matrixAddition(
            [
                [1, 2, 3],
                [4, 5, 6],
            ],
            []
        );
        expect(result).toEqual([]);
    });

    test("throws a new TypeError when either of the two arguments are not of type Array", () => {
        const arg1 = () => matrixAddition({}, []);
        const arg2 = () => matrixAddition([], {});

        expect(arg1).toThrow(
            TypeError("Both arguments in matrixAddition must be of type Array")
        );
        expect(arg2).toThrow(
            TypeError("Both arguments in matrixAddition must be of type Array")
        );
    });

    test("adds two matrices together", () => {
        const matrix1 = [
            [1, 2],
            [3, 4],
        ];
        const matrix2 = [
            [6, 7],
            [1, 2],
        ];
        const result = matrixAddition(matrix1, matrix2);
        expect(result).toEqual([
            [7, 9],
            [4, 6],
        ]);
    });
});
