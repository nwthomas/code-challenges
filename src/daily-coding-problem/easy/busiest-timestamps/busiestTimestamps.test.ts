import { describe, test, expect } from "vitest";

import findBusiestTimes from "./busiestTimestamps.ts";

describe("findBusiestTimes()", () => {
    test("throws a TypeError when the argument is not an array", () => {
        // @ts-expect-error Exercise legacy runtime behavior with an input outside the typed API.
        const result = () => findBusiestTimes("test");
        expect(result).toThrow(TypeError("The argument must be an array"));
    });

    test("returns an empty array if the input argument array has no length", () => {
        const result = findBusiestTimes([]);
        expect(result).toEqual([]);
    });

    test("returns the correct start and ending timestamps for a short array of data objects", () => {
        const result = findBusiestTimes([
            { timestamp: "1234", count: 3, type: "enter" },
            { timestamp: "1235", count: 3, type: "exit" },
        ]);
        expect(result).toEqual(["1234", "1235"]);
    });

    test("returns the correct start and ending timestamps for a long array of data objects", () => {
        const result = findBusiestTimes([
            { timestamp: "1222", count: 1, type: "enter" },
            { timestamp: "1234", count: 3, type: "enter" },
            { timestamp: "1266", count: 4, type: "exit" },
            { timestamp: "1299", count: 10, type: "enter" },
            { timestamp: "1235", count: 3, type: "exit" },
            { timestamp: "1000", count: 7, type: "exit" },
        ]);
        expect(result).toEqual(["1299", "1235"]);
    });
});
