import { describe, expect, it } from "bun:test";

import { searchMatrix } from "./searchMatrix.ts";

describe(searchMatrix.name, () => {
    it("returns true when target exists in a multi-row matrix", () => {
        const matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60],
        ];

        expect(searchMatrix(matrix, 3)).toBe(true);
    });

    it("returns false when target does not exist in matrix", () => {
        const matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60],
        ];

        expect(searchMatrix(matrix, 13)).toBe(false);
    });

    it("returns true when target exists in a single-element matrix", () => {
        expect(searchMatrix([[1]], 1)).toBe(true);
    });

    it("returns false when target does not exist in a single-element matrix", () => {
        expect(searchMatrix([[1]], 2)).toBe(false);
    });

    it("returns true when target exists at the end of the first row", () => {
        expect(
            searchMatrix(
                [
                    [1, 3],
                    [5, 7],
                ],
                3,
            ),
        ).toBe(true);
    });

    it("returns true when target exists at the start of the second row", () => {
        expect(
            searchMatrix(
                [
                    [1, 3],
                    [5, 7],
                ],
                5,
            ),
        ).toBe(true);
    });
});
