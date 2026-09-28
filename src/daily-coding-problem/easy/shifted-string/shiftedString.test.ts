import { describe, test, expect } from "vitest";

import isShiftPossible from "./shiftedString.ts";

describe("isShiftPossible", () => {
    test("returns false if string is not possible", () => {
        const result = isShiftPossible("asdfasdfasdf", "testing");
        expect(result).toBeFalsy();
    });

    test("returns true if the strings are the same", () => {
        const result = isShiftPossible("testing", "testing");
        expect(result).toBeTruthy();
    });

    test("returns true if the rotation is possible", () => {
        const result = isShiftPossible("asdfasdfasdf", "dfasdfasdfas");
        expect(result).toBeTruthy();
    });

    test("returns null if the first argument is not a string", () => {
        // @ts-expect-error Exercise legacy runtime behavior with an input outside the typed API.
        const result = isShiftPossible(34, "test");
        expect(result).toBeNull();
    });

    test("returns null if the second argument is not a string", () => {
        // @ts-expect-error Exercise legacy runtime behavior with an input outside the typed API.
        const result = isShiftPossible("test", 100);
        expect(result).toBeNull();
    });
});
