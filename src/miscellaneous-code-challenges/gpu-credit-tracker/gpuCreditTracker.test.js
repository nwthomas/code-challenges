const { GPUCreditTracker } = require("./gpuCreditTracker");

describe(GPUCreditTracker.name, () => {
    it("inserts transactions correctly and gets the balance", () => {
        const tracker = new GPUCreditTracker();
        tracker.addCredit(10, 80, 5);
        tracker.addCredit(20, 60, 5);
        expect(tracker.getBalance(10)).toBe(5);
        expect(tracker.getBalance(20)).toBe(10);

        tracker.chargeCredit(15, 4);
        tracker.addCredit(15, 20, 8);
        expect(tracker.getBalance(15)).toBe(9);
        expect(tracker.getBalance(20)).toBe(14);

        tracker.addCredit(30, 31, 100);
        tracker.chargeCredit(20, 100);
        expect(tracker.getBalance(30)).toBe(100);
        expect(tracker.getBalance(31)).toBe(100);
        expect(tracker.getBalance(32)).toBe(0);
        expect(tracker.getBalance(20)).toBe(0);
    });
});
