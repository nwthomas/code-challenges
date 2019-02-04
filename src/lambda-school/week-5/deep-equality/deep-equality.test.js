const deepEquals = require("./deep-equality");

const johnA = {
  name: "John",
  address: {
    line1: "321 Anytown",
    line2: "Stoke-on-Trent"
  }
};

const johnB = {
  name: "John",
  address: {
    line1: "321 Anytown",
    line2: "Stoke-on-Trent"
  }
};

const johnC = {
  name: "John Charles",
  address: {
    line1: "321 Anytown",
    line2: "Stoke-on-Trent"
  }
};

test("tests whether two objects are equavilant in all keys and sub-keys", () => {
  expect(deepEquals(johnA, johnB)).toBe(true);
  expect(deepEquals(johnA, johnC)).toBe(false);
});
