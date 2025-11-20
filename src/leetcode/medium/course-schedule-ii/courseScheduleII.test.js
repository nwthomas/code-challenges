const { findOrder } = require("./courseScheduleII");

describe("findOrder", () => {
    it("should return the correct order of courses for a short list of courses", () => {
        expect(findOrder(2, [[1, 0]])).toEqual([0, 1]);
    });

    it("should return the correct order of courses for a long list of courses", () => {
        expect(findOrder(20, [[0,10],[3,18],[5,10],[6,11],[11,14],[13,1],[15,1],[17,4]])).toEqual([10, 0, 1, 2, 18, 3, 4, 5, 14, 11, 6, 7, 8, 9, 12, 13, 15, 16, 17, 19]);
    });

    it("should return an empty array if there are no courses", () => {
        expect(findOrder(0, [])).toEqual([]);
    });

    it("should return an empty array if no order is possible", () => {
        expect(findOrder(2, [[1,0],[0,1]])).toEqual([]);
    });
});