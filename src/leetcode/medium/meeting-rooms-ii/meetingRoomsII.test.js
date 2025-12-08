const { getMinimumMeetingRoomsCount, Interval } = require("./meetingRoomsII");

function createIntervalList(intervals) {
    return intervals.map((interval) => new Interval(interval[0], interval[1]));
}

describe("getMinimumMeetingRoomsCount", () => {
    it("takes in a list with two overlapping meetings and returns correct count", () => {
        const result = getMinimumMeetingRoomsCount(
            createIntervalList([
                [1, 5],
                [4, 9],
            ]),
        );
        expect(result).toEqual(2);
    });

    it("takes in a list with no overlapping meetings and returns 1", () => {
        const result = getMinimumMeetingRoomsCount(
            createIntervalList([
                [1, 5],
                [6, 9],
                [10, 11],
            ]),
        );
        expect(result).toEqual(1);
    });

    it("takes in an empty meetings list and returns 0", () => {
        const result = getMinimumMeetingRoomsCount([]);
        expect(result).toEqual(0);
    });

    it("takes in a small list of overlapping meetings and returns correct day count", () => {
        const result = getMinimumMeetingRoomsCount(
            createIntervalList([
                [0, 30],
                [5, 10],
                [15, 20],
            ]),
        );
        expect(result).toEqual(2);
    });

    it("takes in a large list of overlapping meetings and returns correct day count", () => {
        const result = getMinimumMeetingRoomsCount(
            createIntervalList([
                [1, 40],
                [3, 10],
                [5, 15],
                [20, 41],
                [44, 45],
            ]),
        );
        expect(result).toEqual(3);
    });
});
