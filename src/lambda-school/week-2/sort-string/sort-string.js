/*

Good morning! Write a function called sortString that takes a string of letters and returns a string with the letters sorted in alphabetical order.

Input:
'dcba'
'zycxbwa'
'AzycxbCwBaA'

Expected Output:
'abcd'
'abcwxyz'
'AABCabcwxyz'

*/

function sortString(str) {
  return str
    .split("")
    .sort()
    .join("");
}

module.exports = sortString;
