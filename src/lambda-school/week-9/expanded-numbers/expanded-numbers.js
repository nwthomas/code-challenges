/*

Write a function that accepts a number and returns it in a string as it's expanded form.

Example: Given the number 562 your function should return '500 + 60 + 2'.

*/

function expandedNums(num) {
  const numbers = num.toString().split("");
  let outputStr = "";
  numbers.forEach((num, index) => {
    if (num !== "0") {
      let newExpandedNum = num;
      for (let i = index + 1; i < numbers.length; i++) {
        newExpandedNum = `${newExpandedNum}` + "0";
      }
      return outputStr === ""
        ? (outputStr = newExpandedNum)
        : (outputStr += ` + ${newExpandedNum}`);
    }
  });
  return outputStr;
}

module.exports = expandedNums;