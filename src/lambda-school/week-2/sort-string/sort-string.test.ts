import { test, expect } from "bun:test";

import sortString from "./sort-string.ts";

test("Sorts letters in a string", () => {
    expect(sortString("dcba")).toBe("abcd");
    expect(sortString("zycxbwa")).toBe("abcwxyz");
    expect(sortString("AzycxbCwBaA")).toBe("AABCabcwxyz");
});
