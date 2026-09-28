import { test, expect } from "vitest";

import isSquare from "./you're-a-square.ts";

test("Determines if integral number is a square", () => {
    expect(isSquare(-1)).toBe(false);
    expect(isSquare(4)).toBe(true);
    expect(isSquare(25)).toBe(true);
    expect(isSquare(5)).toBe(false);
});
