import { describe, test, expect } from "vitest";

import getRandomNumber from "./randomNumberExceptList.ts";

describe("randomNumberExceptList", () => {
    describe("getRandomNumber()", () => {
        test("returns null if the type of the first argument is not a number", () => {
            const result = getRandomNumber("test", [1, 2, 3, 4]);
            expect(result).toBeNull();
        });

        test("returns null if the first argument is less-than-or-equal-to 0", () => {
            const result = getRandomNumber(-1, [1, 2, 3, 4]);
            expect(result).toBeNull();
        });

        test("returns null if the type of the second argument is not an object", () => {
            // @ts-expect-error Exercise legacy runtime behavior with an input outside the typed API.
            const result = getRandomNumber(10, { test: "test" });
            expect(result).toBeNull();
        });

        test("returns a random number lesser than the small number passed in and also not in the short list", () => {
            const list = [0, 3];
            const result = getRandomNumber(3, list);
            expect(list).not.toContain(result);
        });

        test("returns a random number lesser than the large number passed in and also not in the large list", () => {
            const list = [
                1, 56, 24, 32, 6, 19, 2, 3, 4, 5, 6, 7, 8, 9, 34, 31, 20, 55,
            ];
            const result = getRandomNumber(55, list);
            expect(list).not.toContain(result);
        });
    });
});
