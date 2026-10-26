import { test, expect } from "bun:test";

import reverseString from "./reverse-string.ts";

test("Reverses the string you pass in", () => {
    expect(reverseString("Hello world!")).toBe("!dlrow olleH");
    expect(reverseString("asdfasdf")).toBe("fdsafdsa");
    expect(reverseString("CS rocks!")).toBe("!skcor SC");
    expect(reverseString("Nathan Thomas")).toBe("samohT nahtaN");
});
