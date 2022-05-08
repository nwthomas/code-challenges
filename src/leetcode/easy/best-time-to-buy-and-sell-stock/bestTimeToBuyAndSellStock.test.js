const { maxProfit } = require("./bestTimeToBuyAndSellStock.js");

describe("Best Time to Buy and Sell Stock", () => {
    test("returns 0 if the array length is 1", () => {
        const result = maxProfit([1]);
        expect(result).toBe(0);
    });

    test("returns 0 if the array length is 0", () => {
        const result = maxProfit([]);
        expect(result).toBe(0);
    });

    test("returns largest profit possible with small list of stock prices", () => {
        const result = maxProfit([1, 4, 19, 2, 10]);
        expect(result).toBe(18);
    });

    test("returns largest profit possible with large list of stock prices", () => {
        const result = maxProfit([17, 1, 10, 5, 3, 28, 49, 3, 20, 1, 10, 60]);
        expect(result).toBe(59);
    });
});
