const mergeObjects = require("./merged-objects");

test("takes in an array of objects and returns an object with the last used value of each key inside it", () => {
  expect(
    mergeObjects([
      { 1: "1", 2: "2", 3: "3" },
      { 3: "4", 4: "4", 5: "6" },
      { 5: "5", 6: "6", 7: "7" }
    ])
  ).toEqual({ 1: "1", 2: "2", 3: "4", 4: "4", 5: "5", 6: "6", 7: "7" });
  expect(
    mergeObjects([
      { 1: "Dude", 2: "what" },
      { 3: "is", 4: "up" },
      { 3: "the" },
      { 4: "heck" }
    ])
  ).toEqual({ 1: "Dude", 2: "what", 3: "the", 4: "heck" });
  expect(mergeObjects([{}, {}, {}, {}])).toEqual({});
});
