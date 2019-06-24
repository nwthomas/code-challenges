const spinWords = require("./stop-gninnips-my-sdrow!");

describe("spinWords()", () => {
  describe("tests that it takes in a string and reverses any word over 5 letters", () => {
    it("should leave a string with words unter 5 letters unchanged", () => {
      expect(spinWords("Dude")).toBe("Dude");
    });

    it("should reverse the order of a string with a word that has more than five letters", () => {
      expect(spinWords("Testing")).toBe("gnitseT");
    });

    it("should selectively reverse the order of words in a sentence that have more than 5 letters", () => {
      expect(spinWords("Marty we have to go back")).toBe(
        "ytraM we have to go back"
      );
    });

    it("should return a string with whitespaces when it is passed into it", () => {
      expect(spinWords("    ")).toBe("    ");
    });

    it("should reverse multiple 5 letter words withing a single string", () => {
      expect(
        spinWords("This is a testing string that tests the spinWords function")
      ).toBe("This is a gnitset gnirts that stset the sdroWnips noitcnuf");
    });
  });
});
