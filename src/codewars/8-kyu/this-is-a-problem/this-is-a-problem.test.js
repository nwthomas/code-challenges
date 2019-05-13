const NameMe = require("./this-is-a-problem");

describe('"This" Is a Problem CodeWars 8kyu challenge', () => {
  it("should instantiate a new class object successfully", () => {
    const nathan = new NameMe("Nathan", "Thomas");
    expect(nathan).toBeDefined();
  });
  it("should return a string successfully when this.nam is called from an instantiated object", () => {
    const nathan = new NameMe("Nathan", "Thomas");
    expect(nathan.name).toBe("Nathan Thomas");
  });
  it("should return falsy when passed arguments that aren't a string", () => {
    const nathan = new NameMe(undefined, null);
    expect(nathan.firstName).toBeFalsy();
  });
});
