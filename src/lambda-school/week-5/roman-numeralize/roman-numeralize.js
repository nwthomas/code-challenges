/*

Good morning! Define a function that takes in a positive integer and returns the Roman Numeral representation of that number.  

Symbol    Value
  I         1
  IV        4
  V         5
  IX        9
  X         10
  XL        40
  L         50
  XC        90
  C         100
  CD        400
  D         500
  CM        900
  M         1,000  

Example: romanNumeralize(1973) should return 'MCMLXXIII'.  

*/

function romanNumeralize(n) {
  const numerals = {
    M: 1000,
    CM: 900,
    D: 500,
    CD: 400,
    C: 100,
    XC: 90,
    L: 50,
    XL: 40,
    X: 10,
    IX: 9,
    V: 5,
    IV: 4,
    I: 1
  };
  let finalRoman = "";

  for (let i in numerals) {
    while (n >= numerals[i]) {
      finalRoman += i;
      n -= numerals[i];
    }
  }
  return finalRoman;
}

module.exports = romanNumeralize;
