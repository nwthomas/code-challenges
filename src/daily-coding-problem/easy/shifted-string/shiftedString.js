/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
*/

function isShiftPossible(originalStr, newStr) {
  if (originalStr === newStr) {
    return true;
  }
  let str = originalStr;
  for (let i = 0; i < originalStr.length; i++) {
    str = str[str.length - 1] + str.slice(0, str.length - 1);
    console.log(str);
    if (str === newStr) {
      return true;
    }
  }
  return false;
}

module.exports = isShiftPossible;
