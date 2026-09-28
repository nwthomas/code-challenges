/*

https://www.codewars.com/kata/calculating-with-functions/javascript

This time we want to write calculations using functions and get the results. Let's have a look at some examples:

JavaScript:
  seven(times(five())); // must return 35
  four(plus(nine())); // must return 13
  eight(minus(three())); // must return 5
  six(dividedBy(two())); // must return 3

Ruby:
  seven(times(five)) # must return 35
  four(plus(nine)) # must return 13
  eight(minus(three)) # must return 5
  six(divided_by(two)) # must return 3

Requirements:
  1. There must be a function for each number from 0 ("zero") to 9 ("nine")
  2. There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby)
  3. Each calculation consist of exactly one operation and two numbers
  4. The most outer function represents the left operand, the most inner function represents the right operand
  5. Divison should be integer division, e.g eight(dividedBy(three()))/eight(divided_by(three)) should return 2, not 2.666666...

*/

function zero(cb?: string) {
    return cb ? Math.floor(eval(`0${cb}`)) : 0;
}
function one(cb?: string) {
    return cb ? Math.floor(eval(`1${cb}`)) : 1;
}
function two(cb?: string) {
    return cb ? Math.floor(eval(`2${cb}`)) : 2;
}
function three(cb?: string) {
    return cb ? Math.floor(eval(`3${cb}`)) : 3;
}
function four(cb?: string) {
    return cb ? Math.floor(eval(`4${cb}`)) : 4;
}
function five(cb?: string) {
    return cb ? Math.floor(eval(`5${cb}`)) : 5;
}
function six(cb?: string) {
    return cb ? Math.floor(eval(`6${cb}`)) : 6;
}
function seven(cb?: string) {
    return cb ? Math.floor(eval(`7${cb}`)) : 7;
}
function eight(cb?: string) {
    return cb ? Math.floor(eval(`8${cb}`)) : 8;
}
function nine(cb?: string) {
    return cb ? Math.floor(eval(`9${cb}`)) : 9;
}

function plus(num: number) {
    return `+${num}`;
}
function minus(num: number) {
    return `-${num}`;
}
function times(num: number) {
    return `*${num}`;
}
function dividedBy(num: number) {
    return `/${num}`;
}

export {
    one,
    two,
    three,
    four,
    five,
    six,
    seven,
    eight,
    nine,
    plus,
    minus,
    times,
    dividedBy,
};
