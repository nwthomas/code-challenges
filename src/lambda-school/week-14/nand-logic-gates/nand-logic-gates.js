/*

For this coding challenge you will be recreating low level logic gates.

You will first create the NAND function and then you will create

NOT, OR, AND, and XOR all using the NAND function that you created.

Implement NAND however you would like and then use NAND to implement the

other logic gates.



See the link below for the truth tables for these logic gates.

https://en.wikipedia.org/wiki/NAND_logic#NAND

All functions should return a 1 for true and a 0 for false.

*/

function NAND(x, y) {
    // You can use whatever JS operators that you would like: &&, ||, !
    return x ? (y ? 0 : 1) : 1;
}

function NOT(n) {
    // Do not use !
    return NAND(n, n);
}

function AND(x, y) {
    // Do not use &&, ||, or !
    // You can use any of the functions that you have already written
    return NAND(x, y) ? 0 : 1;
}

function OR(x, y) {
    // Do not use ||, &&, or !
    // You can use any of the functions that you have already written
    return NAND(NAND(x, x), NAND(y, y));
}

function NOR(x, y) {
    // Do not use ||, &&, or !
    // You can use any of the functions that you have already written
    return NAND(NAND(x, x), NAND(y, y)) ? 0 : 1;
}

function XOR(x, y) {
    // Do not use ||, &&, or !
    // You can use any of the functions that you have already written
    return NAND(NAND(x, NAND(x, y)), NAND(y, NAND(x, y)));
}

function XNOR(x, y) {
    // Do not use ||, &&, or !
    // You can use any of the functions that you have already written
    return NAND(NAND(NAND(x, x), NAND(y, y)), NAND(x, y));
}

function MUX(x, y, selector) {
    // Do not use ||, &&, or !
    // You can use any of the functions that you have already written
    return NAND(NAND(x, NAND(selector, selector)), NAND(y, selector));
}

function DEMUX(data, selector) {
    // Do not use ||, &&, or !
    // You can use any of the functions that you have already written
    return {
        a: AND(data, NOT(selector)),
        b: AND(data, selector),
    };
}

module.exports = { NAND, NOT, AND, OR, NOR, XOR, XNOR, MUX, DEMUX };
