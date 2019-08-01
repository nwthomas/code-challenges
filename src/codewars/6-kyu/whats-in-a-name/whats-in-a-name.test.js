const nameInStr = require("./whats-in-a-name.js");

describe("What's in a Name CodeWars code challenge", () => {
  describe("tests that a string passed as an argument contains all the letters in strict order to make a second string", () => {
    it("should take in a short first argument string and return truthy if it can make the second short argument string", () => {
      expect(nameInStr("Naytksha n T hoimas", "Nathan Thomas")).toBeTruthy();
    });

    it("should take in long first argument string and check if it can make the second long argument string", () => {
      expect(
        nameInStr(
          "D u789AHd e, Wh eYUiore's m&*^(y car",
          "Dude, where's my car"
        )
      ).toBeTruthy();
    });
  });

  describe("tests that a string passed as an argument does not contain all the letters in strict order to make a second string", () => {
    it("should return falsy when passed a short string that cannot make another short string", () => {
      expect(nameInStr("87^AY(GYUAOUYT(YAUOGFI", "876AIJGHJFf f")).toBeFalsy();
    });

    it("should return falsy when passed a long string that cannot make another long string", () => {
      expect(
        nameInStr(
          "OAIh ogas hfuy&*^A75uofa  GAOUYTfyogjJOAHGOIUGFOUYGAO",
          "9869&*^A)ughOUGA(&^GFOHGKAGFo"
        )
      ).toBeFalsy();
    });
  });
});
