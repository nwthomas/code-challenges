/*

https://www.codewars.com/kata/strip-comments/train/javascript

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

var result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
(result should == "apples, pears\ngrapes\nbananas")

*/

function stripComments(input, markers) {
  if (typeof input !== "string" || !Array.isArray(markers)) {
    return null;
  }
  if (!input.length) {
    return "";
  }
  const inputArray = input.split("\n");
  const finalInputArray = [];
  inputArray.forEach(line => {
    let changed = false;
    for (let i = 0; i < markers.length; i++) {
      const markerIndex = line.indexOf(markers[i]);
      if (markerIndex !== -1) {
        newLine = line.slice(0, markerIndex).trim();
        finalInputArray.push(newLine);
        changed = true;
        break;
      }
    }
    if (!changed) {
      finalInputArray.push(line);
    }
  });
  return finalInputArray.join("\n");
}

module.exports = stripComments;
