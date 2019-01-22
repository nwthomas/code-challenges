const sortString = require("./sort-string");

test("Sorts letters in a string", () => {
  expect(sortString("dcba")).toBe("abcd");
  expect(sortString("zycxbwa")).toBe("abcwxyz");
  expect(sortString("AzycxbCwBaA")).toBe("AABCabcwxyz");
});
