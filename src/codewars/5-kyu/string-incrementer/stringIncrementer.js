/*
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
*/

function incrementString (string) {
  let startingIndex = 0;
  
  for (let i = string.length - 1; i > 0; i--) {
    const char = string[i];
    
    if (!char.match(/[0-9]/)) {
      startingIndex = i + 1;
      break;
    }
  }
  
  const incremented = addOneToString(string.slice(startingIndex));
  
  return string.slice(0, startingIndex) + incremented;
}

function addOneToString(string) {
  let finalString = "";
  let carryingOne = true;
  
  for (let i = string.length - 1; i >= 0; i--) {
    const char = string[i];
    let newNum = Number(char);

    if (carryingOne) {
      newNum += 1;
      carryingOne = false;
    }
      
    if (newNum > 9) {
      finalString += newNum - 10;
      carryingOne = true;
    } else {
      finalString += newNum;
    }
  }

  if (carryingOne) {
    finalString += "1";
  }
  
  return finalString.split("").reverse().join("");
}

module.exports = {
    incrementString,
    addOneToStrin
}