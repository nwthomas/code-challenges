import { test, expect } from "vitest";

import firstNonRepeatingLetter from "./first-non-repeating-character.ts";

test("Takes string and returns the first character that does not repeat itself or empty string otherwise", () => {
    expect(firstNonRepeatingLetter("stress")).toBe("t");
    expect(firstNonRepeatingLetter("98dji9f")).toBe("8");
    expect(firstNonRepeatingLetter("aaIIuuEE")).toBe("");
    expect(firstNonRepeatingLetter("Moonmen")).toBe("e");
    expect(firstNonRepeatingLetter("891jhDoi7(*&$aJsdfB981")).toBe("h");
});
