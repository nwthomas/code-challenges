const { scanJumpGame } = require("./jumpGame");

describe("scanJumpGame", () => {
    it("returns true if the last index is reachable", () => {
        const result = scanJumpGame([1, 2, 0, 1, 0]);
        expect(result).toBe(true);
    });

    it("returns false if the last index is not reachable", () => {
        const result = scanJumpGame([1, 2, 1, 0, 1]);
        expect(result).toBe(false);
    });

    it("returns true if the last index is reachable with a single jump", () => {
        const result = scanJumpGame([100]);
        expect(result).toBe(true);
    });
});