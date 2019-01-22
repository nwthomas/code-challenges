const goodVsEvil = require("./good-vs-evil");

test("Make the forces of good and evil fight each other", () => {
  expect(goodVsEvil("2 3 0 2 1 3", "0 3 4 3 1 7 0")).toBe(
    "Battle Result: Evil eradicates all trace of Good"
  );
  expect(goodVsEvil("1", "1")).toBe(
    "Battle Result: No victor on this battle field"
  );
  expect(goodVsEvil("5 2 4 10 0 2", "4 0 3 2 0 0 0")).toBe(
    "Battle Result: Good triumphs over Evil"
  );
});
