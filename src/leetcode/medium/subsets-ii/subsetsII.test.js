const { subsetsWithDup } = require("./subsetsII");

describe("subsetsWithDup", () => {
    it("returns all possible subsets for a short array of nums", () => {
        const result = subsetsWithDup([1, 2, 2]);
        expect(result).toEqual([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]);
    });

    it("returns all possible subsets for a long array of nums", () => {
        const result = subsetsWithDup([1, 2, 2, 3, 3, 3]);
        expect(result).toEqual([
            [],
            [1],
            [1, 2],
            [1, 2, 2],
            [1, 2, 2, 3],
            [1, 2, 2, 3, 3],
            [1, 2, 2, 3, 3, 3],
            [1, 2, 3],
            [1, 2, 3, 3],
            [1, 2, 3, 3, 3],
            [1, 3],
            [1, 3, 3],
            [1, 3, 3, 3],
            [2],
            [2, 2],
            [2, 2, 3],
            [2, 2, 3, 3],
            [2, 2, 3, 3, 3],
            [2, 3],
            [2, 3, 3],
            [2, 3, 3, 3],
            [3],
            [3, 3],
            [3, 3, 3],
        ]);
    });

    it("returns all possible subsets for an array of same nums", () => {
        const result = subsetsWithDup([7, 7]);
        expect(result).toEqual([[], [7], [7, 7]]);
    });
});
