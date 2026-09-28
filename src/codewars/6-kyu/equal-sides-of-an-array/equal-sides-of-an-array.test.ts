import { describe, it, expect } from "vitest";

import findEvenIndex from "./equal-sides-of-an-array.ts";

describe("findEvenIndex()", () => {
    describe("should return -1 when equal sides cannot be found", () => {
        it("tests that -1 is returned for a long unequal array", () => {
            const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
            expect(findEvenIndex(arr)).toBe(-1);
        });

        it("tests that -1 is returned for a short unequal array", () => {
            const arr = [1, 2, 3];
            expect(findEvenIndex(arr)).toBe(-1);
        });
    });

    describe("should return the index of the middle of equal sides of an array", () => {
        it("should return the index of the middle of equal sides of a long array", () => {
            const arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
            expect(findEvenIndex(arr)).toBe(5);
        });

        it("should return the index of the middle of equal sides of a short array", () => {
            const arr = [4, 5, 1, 9];
            expect(findEvenIndex(arr)).toBe(2);
        });
    });

    describe("should handle various complex and primitive data types", () => {
        it("should return -1 if a string is passed as an argument", () => {
            const argument = "test";
            // @ts-expect-error Exercise legacy runtime behavior with an input outside the typed API.
            expect(findEvenIndex(argument)).toBe(-1);
        });

        it("should return -1 if an object is passed as an argument", () => {
            const argument = { test: "test" };
            // @ts-expect-error Exercise legacy runtime behavior with an input outside the typed API.
            expect(findEvenIndex(argument)).toBe(-1);
        });

        it("should return -1 if a number is passed as an argument", () => {
            const argument = 5;
            // @ts-expect-error Exercise legacy runtime behavior with an input outside the typed API.
            expect(findEvenIndex(argument)).toBe(-1);
        });

        it("should return -1 if a boolean is passed as an argument", () => {
            const argument = true;
            // @ts-expect-error Exercise legacy runtime behavior with an input outside the typed API.
            expect(findEvenIndex(argument)).toBe(-1);
        });
    });
});
