import { describe, test, expect } from "vitest";

import getNumberOf1Bits from "./numberOf1Bits.ts";

describe(getNumberOf1Bits.name, () => {
    test("handles number 0", () => {
        const result = getNumberOf1Bits(0);
        expect(result).toBe(0);
    });

    test("handles larger numbers", () => {
        const result = getNumberOf1Bits(1034510);
        expect(result).toBe(11);
    });
});
