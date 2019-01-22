const descendingOrder = require("./descending-order");

test("Takes any non-negative integer and returns it with its digits in order", () => {
  expect(descendingOrder(21445)).toBe(54421);
  expect(descendingOrder(145263)).toBe(654321);
  expect(descendingOrder(1254859723)).toBe(9875543221);
});
