function getIndicesForAddition(row, index) {
    const finalIndices = [];

    if (row.length === 1 || index === 0) {
        finalIndices.push(0);
    } else if (row.length <= index) {
        finalIndices.push(row.length - 1);
    } else {
        finalIndices.push(index - 1, index);
    }

    return finalIndices;
}

function getPascalTriangleRow(k) {
    let finalRow = [];
    let newRow = [];

    if (k <= 0) {
        return finalRow;
    }

    finalRow.push(1);

    for (let i = 2; i <= k; i++) {
        newRow = Array(i).fill(0);

        for (let j = 0; j < newRow.length; j++) {
            const additionIndices = getIndicesForAddition(finalRow, j);

            newRow[j] = additionIndices.reduce(
                (accum, nextIndex) => accum + finalRow[nextIndex],
                0,
            );
        }

        finalRow = newRow;
    }

    return finalRow;
}

module.exports = getPascalTriangleRow;
