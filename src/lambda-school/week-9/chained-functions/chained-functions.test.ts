import { describe, it, expect } from "vitest";

import chainedFunctions from "./chained-functions.ts";

describe("Chained Functions Lambda School code challenge", () => {
    describe("tests that an array of functions and a number are curried in and invoked", () => {
        it("should take in an array of functions and a number and return the total", () => {
            const one = (x: number) => {
                return x * 2;
            };
            const two = (x: number) => {
                return x * x;
            };
            expect(chainedFunctions([one, two])(3)).toBe(36);
        });

        it("should take in an array of functions and a string and return the concatenated string", () => {
            const one = (x: string) => {
                return "Hello " + x + ", ";
            };
            const two = (x: string) => {
                return x + "this is totally a test.";
            };
            expect(chainedFunctions([one, two])("Nathan")).toBe(
                "Hello Nathan, this is totally a test.",
            );
        });

        it("should take in a very long array of functions and a number and return the total", () => {
            const one = (x: number) => x + 1;
            const two = (x: number) => x + 2;
            const three = (x: number) => x + 3;
            const four = (x: number) => x + 4;
            const five = (x: number) => x + 5;
            const arr = [one, two, three, four, five];
            expect(chainedFunctions(arr)(1)).toBe(16);
        });
    });
});
