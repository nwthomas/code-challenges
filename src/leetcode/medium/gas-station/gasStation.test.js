const { canCompleteCircuit } = require("./gasStation");

describe("canCompleteCircuit", () => {
    it("returns the starting gas station index", () => {
        expect(canCompleteCircuit([1, 2, 3, 4], [2, 2, 4, 1])).toBe(3);
    });

    it("returns -1 if it's impossible to complete the circuit", () => {
        expect(canCompleteCircuit([1, 2, 3], [2, 3, 2])).toBe(-1);
    });
});
