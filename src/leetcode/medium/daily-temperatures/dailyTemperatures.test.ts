import { describe, it, expect } from "vitest";

import { dailyTemperatures } from "./dailyTemperatures.ts";

describe("dailyTemperatures", () => {
    it("should return the correct result", () => {
        const temperatures = [73, 74, 75, 71, 69, 72, 76, 73];
        const result = dailyTemperatures(temperatures);
        expect(result).toEqual([1, 1, 4, 2, 1, 1, 0, 0]);
    });
});
