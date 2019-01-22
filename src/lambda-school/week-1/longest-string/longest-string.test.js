const longestString = require("./longestString");

test("Finds the longest string", () => {
  expect(
    longestString([
      "Dude.",
      "Whatever, I do what I want!",
      "Blarghy",
      "Blargh Blargh"
    ]).toBe("Whatever, I do what I want!")
  );
  expect(
    longestString(["This is a string", "String", "Spam spam spam spam spam"])
  ).toBe("Spam spam spam spam spam");
});
