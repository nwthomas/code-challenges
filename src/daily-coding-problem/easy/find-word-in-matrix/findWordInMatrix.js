/*

Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

*/

function findWordInMatrix(matrix, word) {
    let yIndex = 0;
    let xIndex = 0;

    while (yIndex < matrix.length) {
        while (xIndex < matrix[yIndex].length) {
            if (matrix[yIndex][xIndex] === word[0]) {
                if (isWordPresent(matrix, word, yIndex, xIndex)) {
                    return true;
                }
            }

            xIndex++;
        }

        xIndex = 0;
        yIndex++;
    }

    return false;
}

function isWordPresent(matrix, word, currentYIndex, currentXIndex) {
    return (
        isWordPresentInYAxis(matrix, word, currentYIndex, currentXIndex) ||
        isWordPresentInXAxis(matrix, word, currentYIndex, currentXIndex)
    );
}

function isWordPresentInYAxis(matrix, word, currentYIndex, currentXIndex) {
    let wordIndex = 0;
    while (currentYIndex < matrix.length) {
        if (matrix[currentYIndex][currentXIndex] !== word[wordIndex]) {
            return false;
        } else if (word[wordIndex] === word[word.length - 1]) {
            return true;
        }

        currentYIndex++;
        wordIndex++;
    }
}

function isWordPresentInXAxis(matrix, word, currentYIndex, currentXIndex) {
    let wordIndex = 0;
    while (currentXIndex < matrix[currentYIndex].length) {
        if (matrix[currentYIndex][currentXIndex] !== word[wordIndex]) {
            return false;
        } else if (word[wordIndex] === word[word.length - 1]) {
            return true;
        }

        currentXIndex++;
        wordIndex++;
    }
}

module.exports = {
    findWordInMatrix,
    isWordPresent,
};
