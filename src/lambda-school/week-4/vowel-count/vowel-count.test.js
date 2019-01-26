const vowelCount = require("./vowel-count");

test("counts the number of vowels in a given string and returns that number", () => {
  expect(vowelCount("-bcd-fgh-jklmn-pqrst-vwxyz")).toBe(0);
  expect(vowelCount("Hello world!")).toBe(3);
  expect(vowelCount("Pinto beans")).toBe(4);
  expect(vowelCount("The quick brown fox jumped over the lazy dog.")).toBe(12);
  expect(
    vowelCount(
      "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal."
    )
  ).toBe(58);
  expect(vowelCount("All I have ever wanted is to be an Uber driver!")).toBe(
    16
  );
});
