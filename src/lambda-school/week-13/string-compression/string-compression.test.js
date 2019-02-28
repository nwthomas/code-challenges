const stringCompression = require("./string-compression");

test("takes in a string and returns its compressed form if it is shorter than the original in length", () => {
  expect(stringCompression("aabcccccaaa")).toBe("a2b1c5a3");
  expect(stringCompression("ahjsiuyrlfnlsoifhkjhsdf")).toBe(
    "ahjsiuyrlfnlsoifhkjhsdf"
  );
  expect(stringCompression("dudette")).toBe("dudette");
  expect(stringCompression("zzzzzzzzuuufffrrryyy")).toBe("z8u3f3r3y3");
  expect(stringCompression("e")).toBe("e");
});
