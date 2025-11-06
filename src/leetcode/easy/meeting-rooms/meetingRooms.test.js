const { scanAttendMeetings , Interval } = require("./meetingRooms");

describe("scanAttendMeetings", () => {
    it("returns true if there are no meetings", () => {
        const result = scanAttendMeetings([]);
        expect(result).toBe(true);
    });

    it("returns true if there is one meeting", () => {
        const result = scanAttendMeetings([new Interval(0, 30)]);
        expect(result).toBe(true);
    });

    it("returns false if there are overlapping meetings", () => {
        const result = scanAttendMeetings([new Interval(0, 31), new Interval(30, 40)]);
        expect(result).toBe(false);
    });

    it('returns true if prev end and current start are same number', () => {
        const result = scanAttendMeetings([new Interval(0, 30), new Interval(30, 40)]);
        expect(result).toBe(true);
    })
});