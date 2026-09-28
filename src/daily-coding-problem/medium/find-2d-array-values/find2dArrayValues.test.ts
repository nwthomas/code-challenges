import { describe, test, expect } from "vitest";

import { createArray, findValues, flattenArray } from "./find2dArrayValues.ts";

const utils = {
    getSides: function (array: number[][]) {
        const y = array.length;
        const x = array[0].length;
        return { x, y };
    },
};

describe("find2dArrayValues", () => {
    describe("createArray", () => {
        test("creates array array of specified length correctly", () => {
            const result = createArray(10, 10);
            expect(utils.getSides(result!)).toEqual({ x: 10, y: 10 });
        });

        test("has the correct integers for each position", () => {
            const result = createArray(5, 5);
            expect(result![0][0]).toBe(1);
            expect(result![1][4]).toBe(10);
            expect(result![4][4]).toBe(25);
        });

        test("returns null if x or y are not integers", () => {
            // @ts-expect-error Exercise legacy runtime behavior with an input outside the typed API.
            const result = createArray("test", []);
            expect(result).toBeNull();
        });
    });

    describe("flattenArray", () => {
        test("should successfully flatten a small array of arrays", () => {
            const array = [1, [[9, [[1, 5]]], 2]];
            const result = flattenArray(array);
            expect(result).toEqual([1, 9, 1, 5, 2]);
        });

        test("should successfully flatten a large array of arrays", () => {
            const array = [
                [[[[[[[[[[[[[[[[5]]]]]]]], 0]]]]]]]],
                [[[1, [[[[[[[[[[[[4]]]]]]], 3, 2]]]]]]]],
                [[[[10]], 3], [[[[[[[[[[[[[7198237]]]]]]]]]]]]]],
            ];
            const result = flattenArray(array);
            expect(result).toEqual([5, 0, 1, 4, 3, 2, 10, 3, 7198237]);
        });

        test("returns null if a non-array or one with no length is passed in", () => {
            const emptyResult = flattenArray([]);
            // @ts-expect-error Exercise legacy runtime behavior with an input outside the typed API.
            const nonArrayResult = flattenArray("test");
            expect(emptyResult).toBeNull();
            expect(nonArrayResult).toBeNull();
        });
    });

    describe("findMostUsed2dArrayValues", () => {
        test("returns null if x or y arguments are not integers", () => {
            // @ts-expect-error Exercise legacy runtime behavior with an input outside the typed API.
            const result = findValues("test", [], {});
            expect(result).toBeNull();
        });

        test("should return the number of times an integer is seen in a small 2D array", () => {
            const result = findValues(10, 10, 2);
            expect(result).toEqual(2);
        });

        test("should return the number of times an integer is seen in a large 2D array", () => {
            const result = findValues(1000, 1000, 50);
            expect(result).toBe(6);
        });
    });
});
