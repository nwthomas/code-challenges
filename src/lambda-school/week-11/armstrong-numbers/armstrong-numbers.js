/*

An Armstrong number is an n-digit number that is equal to the sum of the n'th powers of its digits. Determine if the input number is an Armstrong number.  Return either true or false .

 For example with the number 153 there are 3 digits so you would add together the cubed values of all the digits like this: 1^3 + 5^3 + 3^3 === 153 

Input Sample:

6
153
351

Output Sample:  

true
true
false

*/

function isArmstrongNumber(n) {
  const nums = n.toString().split("");
  const length = nums.length;
  const total = nums.reduce((accum, nextNum) => {
    return (accum += Math.pow(Number(nextNum), length));
  }, 0);
  return total === n;
}

module.exports = isArmstrongNumber;
