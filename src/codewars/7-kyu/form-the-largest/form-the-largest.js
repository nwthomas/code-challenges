/*

https://www.codewars.com/kata/form-the-largest/train/javascript

TASK
Given a number , Return The Maximum number could be formed from the digits of the number given .

NOTES
Only Positve numbers passed to the function, numbers Contain digits [1:9] inclusive

Digit Duplications could occur, So also consider it when forming the Largest

Input >> Output Examples:
1- maxNumber (213) ==> return (321)
Explanation:
As 321 is The Maximum number could be formed from the digits of the number 213 .

2- maxNumber (7389) ==> return (9873)
Explanation:
As 9873 is The Maximum number could be formed from the digits of the number 7389 .

3- maxNumber (63729) ==> return (97632)
Explanation:
As 97632 is The Maximum number could be formed from the digits of the number 63729 .

4- maxNumber (566797) ==> return (977665)
Explanation:
As 977665 is The Maximum number could be formed from the digits of the number 566797 .

Note : Digit duplications are considered when forming the largest .

5- maxNumber (17693284) ==> return (98764321)
Explanation:
As 98764321 is The Maximum number could be formed from the digits of the number 17693284 .

*/

function maxNumber(n) {
  return Number(
    n
      .toString()
      .split("")
      .sort()
      .reverse()
      .join("")
  );
}

module.exports = maxNumber;
