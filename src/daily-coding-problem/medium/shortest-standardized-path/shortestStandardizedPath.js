/*

Good morning! Here's your coding interview problem for today.

This problem was asked by Quora.

Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.

For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".

*/

const BACK_DIRECTION = "..";
const IGNORE_DIRECTIONS = [".", ""];

function findShortestStandardizedPath(path) {
    if (typeof path !== "string") {
        throw new TypeError(
            "The argument for findShortestStandardizedPath must be of type string",
        );
    }

    const stack = [];
    const pathDirections = path.split("/");

    for (let i = 0; i < pathDirections.length; i++) {
        const direction = pathDirections[i];

        // Check that it's not the root folder, it's a truthy string, and not a direction
        // for same folder
        if (i !== 0 && IGNORE_DIRECTIONS.indexOf(direction) > -1) {
            continue;
        }

        // Move back up to parent folder and pop it off
        else if (
            stack[stack.length - 1] !== BACK_DIRECTION &&
            direction === BACK_DIRECTION &&
            stack.length
        ) {
            stack.pop();

            if (!stack.length) {
                stack.push(BACK_DIRECTION);
            }
        }

        // Add to final path
        else {
            stack.push(direction);
        }
    }

    if (stack.length <= 1) {
        return path;
    }

    return `${stack.join("/")}/`;
}

module.exports = findShortestStandardizedPath;
