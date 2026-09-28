import { test, expect } from "vitest";

import alphanumeric from "./not-very-secure.ts";

test("checks a string for if it only contains upper-and-lower-case alphanumeric character", () => {
    expect(alphanumeric("Mazinkaiser")).toBe(true);
    expect(alphanumeric("hello world_")).toBe(false);
    expect(alphanumeric("PassW0rd")).toBe(true);
    expect(alphanumeric("     ")).toBe(false);
});
