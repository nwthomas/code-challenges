/*

Good morning! Your function takes a single parameter: an array ("chain") of functions.  Return the results iterating through the array and invoking them one at a time. Each function in the array will take an additional argument from a second set of parentheses when chainedFunctions is invoked, i.e. you will invoke chainedFunctions like so:
chainedFunctions(Array)(value);

Note that you only need to write chainedFunctions to accept the one parameter, arr. The value in the second set of parentheses is the argument that each of the functions in the array will act upon. 

For example:
function one(x) { return x + x; }
function two(x) { return x * 2; }
console.log(chainedFunctions([one,two])); // <--- [Function] or, [Function: {name}]
console.log(chainedFunctions([one,two])(3)); // <--- 12

Given functions one and two as arguments, chainedFunctions([one,two])(3) returns twelve because in iterating through each function in the array, their returns accept (3) as their argument.

chainedFunctions() resolves one(3) to six, and two(3) doubles the return from one(3).

Note that if you invoke chainedFunctions() without a second set of parentheses, you will end up with the return of a [Function].

function a(x) { return x + "!" };
function b(x) { return x + "?" };
function c(x) { return "Hello " + x };
function d(x) { return x + " ¯\\_(ツ)_/¯" };
console.log(chainedFunctions([c, a, a, d, b])('Ryan'));
// <--- Hello Ryan!! ¯\_(ツ)_/¯?

Note the order in which functions a(), b(), c(), and d() are invoked within the array passed to chainedFunctions().

*/

function chainedFunctions(x) {
  return function(b) {
    let total;
    for (let i = 0; i < x.length; i++) {
      if (total) {
        total = x[i](total);
      } else {
        total = x[i](b);
      }
    }
    return total;
  };
}

module.exports = chainedFunctions;
