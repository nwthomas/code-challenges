const Iterator2DArray = require("./nextItemIn2dArray.js");

const utils = {
    small2dArray: [[1, 3, 5, 6], [], [1, 3], [5, 1, 2, 3, 4, 5, 6], ["end"]]
};

describe("Implement2DIterator", () => {
    describe("instantiates", () => {
        test("instantiates a new version of the Iterator2DArray class", () => {
            const result = new Iterator2DArray(utils.small2dArray);
            expect(result instanceof Iterator2DArray).toBeTruthy();
        });
    });

    describe("next()", () => {
        // finish
    });

    describe("hasNext()", () => {
        // finish
    });
});
