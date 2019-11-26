const closewisePrintArray = require("./clockwiseSpiralArray.js");

describe("clockwisePrintArray()", () => {
  let finished = false;
  let direction = "right";
  let x = 0;
  let y = 0;
  while (!finished) {
    if (direction === "right" && x < arr[y].length && arr[y][x + 1]) {
      console.log(arr[y][x]);
      x++;
    } else if (direction === "down" && y < arr.length && arr[y + 1][x]) {
      console.log(arr[y][x]);
      y++;
    } else if (direction === "left" && x >= 0 && arr[y][x - 1]) {
      console.log(arr[y][x]);
      x--;
    } else if (direction === "up" && y >= 0 && arr[y - 1][x]) {
      console.log(arr[y][x]);
      y--;
    } else {
      if (direction === "right") direction = "down";
      if (direction === "down") direction = "left";
      if (direction === "left") direction = "up";
      if (direction === "up") direction = "right";
    }
    arr[y][x] = null;
  }
});
