const HitCounter = require("./hitCounter.js");

describe("HitCounter", () => {
    describe("instantiates", () => {
        test("instantiates a new version of the HitCounter class", () => {
            const hc = new HitCounter();
            expect(hc instanceof HitCounter).toBeTruthy();
        });
    });

    describe("record()", () => {
        test("records a single instance of a hit timestamp", () => {
            const hc = new HitCounter();
            const now = Date.now();
            hc.record(`${now}`);
            const result = hc.hitCounter;
            expect(result).toEqual({ [now]: 1 });
        });

        test("records a series of instances of a hit timestampd", () => {
            const hc = new HitCounter();
            const tracker = {};
            let i = 0;
            while (i < 10) {
                const now = `${Math.floor(Date.now() * Math.random())}`;
                hc.record(now);
                tracker[now] = 1;
                i++;
            }
            const result = hc.hitCounter;
            expect(result).toEqual(tracker);
        });

        test("records multiple hits for a single timestamp", () => {
            const hc = new HitCounter();
            hc.record("1");
            hc.record("2");
            hc.record("1");
            const result = hc.hitCounter["1"];
            expect(result).toBe(2);
        });
    });

    describe("range()", () => {
        test("returns null if lower is not given as an argument", () => {
            const hc = new HitCounter();
            const result = hc.range(undefined, "1234");
            expect(result).toBe(0);
        });

        test("returns null if upper is not given as an argument", () => {
            const hc = new HitCounter();
            const result = hc.range("1234");
            expect(result).toBe(0);
        });

        test("returns the correct number of hits within the range", () => {
            const hc = new HitCounter();
            hc.record("1");
            hc.record("5");
            hc.record("3");
            hc.record("3");
            const result = hc.range("2", "4");
            expect(result).toBe(2);
        });
    });

    describe("total()", () => {
        test("returns the correct total of a small number of hits recorded", () => {
            const hc = new HitCounter();
            hc.record("0123456789");
            hc.record("1000000000");
            const result = hc.total();
            expect(result).toBe(2);
        });

        test("returns the correct total of a large number of hits recorded", () => {
            const hc = new HitCounter();
            const tracker = {};
            let i = 0;
            while (i < 10) {
                const now = `${Math.floor(Date.now() * Math.random())}`;
                hc.record(now);
                tracker[now] = 1;
                i++;
            }
            const result = hc.total();
            expect(result).toBe(10);
        });
    });
});
