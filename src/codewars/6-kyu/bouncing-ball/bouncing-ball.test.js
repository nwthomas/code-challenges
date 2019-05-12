const bouncingBall = require("./bouncing-ball");

describe("Bouncing Balls 6kyu CodeWars code challenge", () => {
  it("should return the number of times the ball is seen out of the window", () => {
    expect(bouncingBall(6, 0.66, 1.5)).toEqual(7);
    expect(bouncingBall(3, 0.66, 1.5)).toEqual(3);
  });
  it("should return -1 if the height is lesser-than-or-equal-to 0", () => {
    expect(bouncingBall(-5, 0.33, 2)).toEqual(-1);
  });
  it("should return -1 if the bounce ratio is less-than-or-equal-to 0 and greater-than-or-equal-to 1", () => {
    expect(bouncingBall(3, -1, 1.5)).toEqual(-1);
    expect(bouncingBall(3, 15, 1.5)).toEqual(-1);
  });
  it("should return return -1 if the window parameter is greater than height", () => {
    expect(bouncingBall(3, 0.35, 5)).toEqual(-1);
  });
});
