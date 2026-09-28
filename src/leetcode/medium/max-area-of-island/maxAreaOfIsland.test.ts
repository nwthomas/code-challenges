import { describe, test, expect } from "vitest";

import { maxAreaOfIsland } from "./maxAreaOfIsland.ts";

describe("maxAreaOfIsland", () => {
    test("returns the maximum area of an island in a grid", () => {
        const grid = [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ];
        const result = maxAreaOfIsland(grid);
        expect(result).toBe(6);
    });

    test("returns 0 if there is no island in the grid", () => {
        const grid = [[0, 0, 0, 0, 0, 0, 0, 0]];
        const result = maxAreaOfIsland(grid);
        expect(result).toBe(0);
    });

    test("returns 0 if the grid is empty", () => {
        const grid: never[] = [];
        const result = maxAreaOfIsland(grid);
        expect(result).toBe(0);
    });
});
