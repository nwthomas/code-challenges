const stripComments = require("./stripComments.js");

describe("stripComments()", () => {
  test("returns an empty string if the inputs are empty arrays", () => {
    const result = stripComments("", []);
    expect(result).toBe("");
  });

  test("returns null if the first argument is not a string", () => {
    const result = stripComments([], []);
    expect(result).toBeNull();
  });

  test("returns null if the second argument is not an array", () => {
    const result = stripComments([], "test");
    expect(result).toBeNull();
  });

  test("strips the comments associated with given markers out of strings", () => {
    const str =
      "this is a test ! this is a test\nthis is a test\nthis is a test % another comment";
    const result = stripComments(str, ["!", "%"]);
    expect(result).toBe("this is a test\nthis is a test\nthis is a test");
  });

  test("strips many comments with complicated markers out of a given input string", () => {
    const str =
      "test ^&* comment\ntest *()&^%$ comment\ntest\ntest\ntest !@# ^ *8 $ % comment\ntest";
    const result = stripComments(str, ["^&*", "*()&^%$", "!@#"]);
    expect(result).toBe("test\ntest\ntest\ntest\ntest\ntest");
  });
});
