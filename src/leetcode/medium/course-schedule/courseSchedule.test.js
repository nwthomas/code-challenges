const { canFinish } = require('./courseSchedule');

describe('canFinish', () => {
    it('returns true if no prereqs', () => {
        expect(canFinish(100, [])).toBe(true);
    });

    it('returns false if courses are not possible', () => {
        expect(canFinish(1000, [[0, 1], [5, 100], [100, 3], [1, 0]])).toBe(false);
    });

    it('returns true if courses are possible', () => {
        expect(canFinish(20, [[0,10],[3,18],[5,10],[6,11],[11,14],[13,1],[15,1],[17,4]])).toBe(true);
    });
});