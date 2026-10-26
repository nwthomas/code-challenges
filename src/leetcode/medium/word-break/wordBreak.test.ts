import { describe, expect, it } from "bun:test";

import { wordBreak } from "./wordBreak.ts";

describe(wordBreak.name, () => {
    it("successfully breaks words", () => {
        const words = ["leet", "code"];
        const s = "leetcode";
        expect(wordBreak(s, words)).toBe(true);
    });

    it("unsuccessfully breaks words", () => {
        const words = ["cats", "dog", "sand", "and", "cat"];
        const s = "catsandog";
        expect(wordBreak(s, words)).toBe(false);
    });

    it("handles short strings", () => {
        const words = ["dog", "s", "gs"];
        const s = "dogs";
        expect(wordBreak(s, words)).toBe(true);
    });
});
