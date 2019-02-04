/*

Good morning! Today we will be emulating "logic gates" with JavaScript. Our functions will emulate the "not", "and", "not and", inclusive "or" and exclusive or "xor" operators.

For your emulation functions, you limited to only using the deep equality operator === and if (conditional) {statements}
Do not use !, &&, or ||.
Do not use the functions you have created to emulate any of the other logic gates, e.g. don't use your NOT() function in the NAND() function.

Your NOT() function only takes one parameter.
Your other functions will take two inputs and return a Boolean value which corresponds to the conditions satisfied by their logical operator.
To illustrate this behavior, refer to the truth tables below.
As an example, your AND() function should implement the following behavior:
console.log(AND(true, true));   // ---> true
console.log(AND(true, false));  // ---> false
console.log(AND(false, true));  // ---> false
console.log(AND(false, false)); // ---> false

TRUTH TABLES
! = NOT
| phi | !phi |
|-----|------|
|  T  |   F  |
|  F  |   T  |

& = AND
| phi | psi | phi & psi |
|-----|-----|-----------|
|  T  |  T  |     T     |
|  T  |  F  |     F     |
|  F  |  T  |     F     |
|  F  |  F  |     F     |

NAND
| phi | psi | !(phi & psi) |
|-----|-----|--------------|
|  T  |  T  |       F      |
|  T  |  F  |       T      |
|  F  |  T  |       T      |
|  F  |  F  |       T      |

^ = inclusive OR
| phi | psi | phi ^ psi |
|-----|-----|-----------|
|  T  |  T  |     T     |
|  T  |  F  |     T     |
|  F  |  T  |     T     |
|  F  |  F  |     F     |

XOR = exclusive OR
| phi | psi | phi XOR psi |
|-----|-----|-------------|
|  T  |  T  |      F      |
|  T  |  F  |      T      |
|  F  |  T  |      T      |
|  F  |  F  |      F      |

*/

function NOT(b) {
  if (b === true) return false;
  return true;
}

function AND(x, y) {
  if (x === y) {
    // Covers True, True and False, False
    if (x === true) return true; // True, True
  }
  return false; // All other cases
}

function NAND(x, y) {
  if (x === y) {
    // Covers True, True and False, False cases
    if (x === true) return false; // True, True
  }
  return true; // Covers all other cases
}

function OR(x, y) {
  if (x === y) {
    // Covers True, True and False, False cases
    if (x === false) return false; // False, False
  }
  return true; // All other cases would return true
}

function XOR(x, y) {
  if (x === y) return false; // Cover True, True and False, False
  return true; // Covers all other use cases
}

module.exports = { NOT, AND, NAND, OR, XOR };
