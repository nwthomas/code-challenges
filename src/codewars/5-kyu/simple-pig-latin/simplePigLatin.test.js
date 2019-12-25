const pigIt = require("./simplePigLatin.js");

describe("simplePigLatin", () => {
  describe("pigIt()", () => {
    test("returns null if the type of argument passed in is not string", () => {
      const result = pigIt([]);
      expect(result).toBeNull();
    });

    test("returns simple pig latin for a short string with no punctuation", () => {
      const result = pigIt("this is a simple sentence");
      expect(result).toBe("histay siay aay implesay entencesay");
    });

    test("returns simple pig latin for a long string with no punctuation", () => {
      const result = pigIt(
        "this is a test sentence and it contains lots of long big words that are easy to read"
      );
      expect(result).toBe(
        "histay siay aay esttay entencesay ndaay tiay ontainscay otslay foay onglay igbay ordsway hattay reaay asyeay otay eadray"
      );
    });

    test("handles punctuation using regular expressions", () => {
      const result = pigIt(
        "this sentence, while nice, has tons of punctuation."
      );
      expect(result).toBe(
        "histay sentence, hileway nice, ashay onstay foay punctuation."
      );
    });
  });
});
