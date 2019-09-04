const digital_root = require("./digital-root.js");

describe("digital_root()", () => {
  describe("should return the digital root when a small number is passed as an argument", () => {
    it("tests that the digital root is returned when a small number is passed in", () => {
      expect(digital_root(15)).toBe(6);
      expect(digital_root(20)).toBe(2);
      expect(digital_root(100)).toBe(1);
    });
  });

  describe("should return the digital root when a large number is passed as an argument", () => {
    it("tests that the digital root is returned when a small number is passed in", () => {
      expect(digital_root(1679172635123)).toBe(8);
      expect(digital_root(89698761876523849612)).toBe(7);
    });
  });

  describe("should return 0 as the digital root when 0 is passed as an argument", () => {
    it("tests that 0 is returned as the digital root when 0 is passed in", () => {
      expect(digital_root(0)).toBe(0);
    });
  });
});
