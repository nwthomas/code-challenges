const breadthFirstSearch = require("./breadth-first-search");

let deep = {
  1: 2,
  3: { 4: "a", b: "c" },
  5: { 6: { 7: 8 } },
  9: { 10: { 11: { 12: { 13: { 14: { 15: 16 } } } } } }
};

test("Return true if searched item exists in nested objects or false if it doesn't", () => {
  expect(breadthFirstSearch(deep, 16)).toBe(true);
  expect(breadthFirstSearch(deep, "Dude")).toBe(false);
  expect(breadthFirstSearch(deep, "c")).toBe(true);
});
