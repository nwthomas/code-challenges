import { describe, expect, it } from "bun:test";

import { maxProduct } from "./maximumProductSubarray.ts";

describe("Maximum Product Subarray", () => {
    it("returns the only value if array length is one", () => {
        const result = maxProduct([10101]);
        expect(result).toBe(10101);
    });

    it("returns the largest product within the array", () => {
        const result = maxProduct([2, 3, -2, 4, 10, -5, 3, 2, 1]);
        expect(result).toBe(14400);
    });
});
