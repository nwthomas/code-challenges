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

        test("instantiates an empty array as the default", () => {
            const result = new Iterator2DArray();
            expect(result._array).toEqual([]);
        });

        test("instantiates with null as the default nextValue if the 2D array is empty", () => {
            const result = new Iterator2DArray([]);
            expect(result._nextValue).toBeNull();
        });

        test("instantiates with a non-null value for nextValue if 2D array isn't empty", () => {
            const result = new Iterator2DArray(utils.small2dArray);
            expect(result._nextValue).toBe(1);
        });
    });

    describe("hasNext()", () => {
        test("returns true if there is a next item in the 2D array", () => {
            const Iterator = new Iterator2DArray(utils.small2dArray);
            const result = Iterator.hasNext();
            expect(result).toBeTruthy();
        });

        test("returns false if there is not a next item in the 2D array", () => {
            const Iterator = new Iterator2DArray([]);
            const result = Iterator.hasNext();
            expect(result).toBeFalsy();
        });

        test("sets the _nextValue class property when it runs if a next value is available", () => {
            const Iterator = new Iterator2DArray(utils.small2dArray);
            const initialNextValue = Iterator._nextValue;
            Iterator._nextValue = null;
            Iterator.hasNext();
            const finalNextValue = Iterator._nextValue;
            expect(initialNextValue).toBe(1);
            expect(finalNextValue).toBe(3);
        });

        test("should not throw a reference error when any index is n + 1", () => {
            const Iterator = new Iterator2DArray([[1]]);
            Iterator.next();
            const result = Iterator.hasNext();
            expect(result).toBeFalsy();
        });
    });

    describe("next()", () => {
        test("returns the _nextValue property if it is not null", () => {
            const Iterator = new Iterator2DArray(utils.small2dArray);
            const result = Iterator.next();
            expect(result).toBe(1);
        });

        test("calling next() repeatedly returns different values", () => {
            const Iterator = new Iterator2DArray(utils.small2dArray);
            const resultOne = Iterator.next();
            const resultTwo = Iterator.next();
            const resultThree = Iterator.next();
            expect(resultOne).toBe(1);
            expect(resultTwo).toBe(3);
            expect(resultThree).toBe(5);
        });

        test("calling next() at n + 1 for any index throws a ReferenceError", () => {
            const Iterator = new Iterator2DArray([[1]]);
            Iterator.next();
            const result = () => Iterator.next();
            expect(result).toThrow(
                ReferenceError(`The (x, y) indices of (0, 1) are not valid`)
            );
        });
    });
});
