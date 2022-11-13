/**
 * This function should output something along the lines of <4, 5, 6, 7* 8, 9, 10> where 7 is the current page, the total number of pages
 * is 10, and the number to be shown is 7. The currently-shown page number (designated with a *) should be centralized if possible.
 *
 * @param {number} total - The is the total number of pages available
 * @param {number} show - The is the number of pages that should be shown in the pagination selector
 * @param {number} current - The currently-selected page
 * @return - String representing the pagination UI
 */
function buildPagePagination(total, show, current) {
    if (show > total) {
        throw Error("Shown pages must be equal-or-lesser than total");
    } else if (current < 1 || current > total) {
        throw Error("Current page must be within valid page bounds");
    }

    const half = Math.floor(show / 2);
    let leftSide = current - half;
    let rightSide = current + half;
    let result = "<";

    if (show % 2 === 0) {
        leftSide += 1;
    }

    if (rightSide > total) {
        const diff = rightSide - total;
        rightSide = total;
        leftSide -= diff;
    }

    if (leftSide < 1) {
        const diff = Math.abs(leftSide) + 1;
        leftSide = 1;
        rightSide += diff;
    }

    for (let i = leftSide; i <= rightSide; i++) {
        if (i !== leftSide && i - 1 !== current) {
            result += ", ";
        } else if (i - 1 === current) {
            result += "* ";
        }

        result += i;
    }

    if (!half) {
        result += "*";
    }

    result += ">";

    return result;
}

module.exports = buildPagePagination;
