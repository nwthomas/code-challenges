const reverse = require("./reverse-every-other-word-in-the-string.js");

describe("Reverse Every Other Word in the String CodeWars 6kyu code challenge", () => {
  describe("tests that the function reverses every second word in a string passed as an argument", () => {
    it("should take in a short string of words and reverse every second word", () => {
      expect(reverse("this is a test of the reverse function")).toBe(
        "this si a tset of eht reverse noitcnuf"
      );
    });

    it("should take in a long string of words and reverse every second word", () => {
      expect(
        reverse(
          "This is an even longer test of the reverse function in fact the sentence keeps on going on and on and on"
        )
      ).toBe(
        "This si an neve longer tset of eht reverse noitcnuf in tcaf the ecnetnes keeps no going no and no and no"
      );
    });

    it("should take in a string with punction and still reverse every second word", () => {
      expect(reverse("Dude, where's my car??!")).toBe(
        "Dude, s'erehw my !??rac"
      );
    });

    it("should take in a string filled with numbers and still reverse every second grouping of them", () => {
      expect(reverse("578 75514 071697 876976")).toBe(
        "578 41557 071697 679678"
      );
    });
  });
});
