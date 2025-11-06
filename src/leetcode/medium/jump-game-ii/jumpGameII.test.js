const { jump } = require("./jumpGameII");

describe("jump", () => {
    it("returns the minimum number of jumps to reach the last index", () => {
        const result = jump([2, 3, 1, 1, 4]);
        expect(result).toBe(2);
    });

    it("returns the minimum number of jumps to reach the last index with a single jump", () => {
        const result = jump([100]);
        expect(result).toBe(0);
    });

    it("returns the minimum number of jumps to reach the last index with multiple jumps", () => {
        const result = jump([2, 3, 0, 1, 4]);
        expect(result).toBe(2);
    });
});