/*

https://www.codewars.com/kata/tic-tac-toe-checker/javascript

If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
We want our function to return:

-1 if the board is not yet finished (there are empty spots),
1 if "X" won,
2 if "O" won,
0 if it's a cat's game (i.e. a draw).
You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

*/

function isSolved(board) {
  if (checkBoard(1, board)) {
    return 1;
  } else if (checkBoard(2, board)) {
    return 2;
  } else if (JSON.stringify(board).includes("0")) {
    return -1;
  } else {
    return 0;
  }
}

function checkBoard(value, board) {
  if (
    (board[0][0] === value && board[0][1] === value && board[0][2] === value) ||
    (board[1][0] === value && board[1][1] === value && board[1][2] === value) ||
    (board[2][0] === value && board[2][1] === value && board[2][2] === value) ||
    (board[0][0] === value && board[1][0] === value && board[2][0] === value) ||
    (board[0][1] === value && board[1][1] === value && board[2][1] === value) ||
    (board[0][2] === value && board[1][2] === value && board[2][2] === value) ||
    (board[0][0] === value && board[1][1] === value && board[2][2] === value) ||
    (board[0][2] === value && board[1][1] === value && board[2][0] === value)
  ) {
    return true;
  } else {
    return false;
  }
}

module.exports = isSolved;
