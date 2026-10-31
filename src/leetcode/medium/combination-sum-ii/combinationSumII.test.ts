import { describe, expect, it } from "vitest";

import { combinationSum2 } from "./combinationSumII.ts";

describe(combinationSum2.name, () => {
    it("should return all unique combinations sums", () => {
        const result = combinationSum2([10, 1, 2, 7, 6, 1, 5], 8);
        expect(result).toEqual([
            [1, 1, 6],
            [1, 2, 5],
            [1, 7],
            [2, 6],
        ]);
    });

    it("should return a larger array of unique combination sums", () => {
        const result = combinationSum2([2, 5, 2, 1, 2], 5);
        expect(result).toEqual([[1, 2, 2], [5]]);
    });

    it("should return an empty array if no combination sums are possible", () => {
        const result = combinationSum2([2, 3, 5], 1);
        expect(result).toEqual([]);
    });
});
