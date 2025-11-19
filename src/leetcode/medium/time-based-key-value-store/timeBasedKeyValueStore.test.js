const { TimeMap } = require("./timeBasedKeyValueStore");

describe("TimeMap", () => {
    it("should set a value for a key at a given timestamp", () => {
        const timeMap = new TimeMap();
        timeMap.set("foo", "bar", 1);
        expect(timeMap.get("foo", 1)).toBe("bar");
    });

    it("should return an empty string if no value is found", () => {
        const timeMap = new TimeMap();
        expect(timeMap.get("foo", 1)).toBe("");
    });

    it("should return the correct value if multiple values are set", () => {
        const timeMap = new TimeMap();
        timeMap.set("foo", "bar", 1);
        timeMap.set("foo", "bar2", 2);
        expect(timeMap.get("foo", 1)).toBe("bar");
        expect(timeMap.get("foo", 2)).toBe("bar2");
    });

    it("should return the correct value for different keys", () => {
        const timeMap = new TimeMap();
        timeMap.set("foo", "bar", 1);
        timeMap.set("foo2", "bar2", 2);
        expect(timeMap.get("foo", 1)).toBe("bar");
        expect(timeMap.get("foo2", 2)).toBe("bar2");
    });

    it("should return the correct value for same key at different timestamps", () => {
        const timeMap = new TimeMap();
        timeMap.set("foo", "bar", 1);
        timeMap.set("foo", "bar2", 2);
        timeMap.set("foo", "bar3", 3);
        expect(timeMap.get("foo", 1)).toBe("bar");
        expect(timeMap.get("foo", 2)).toBe("bar2");
        expect(timeMap.get("foo", 3)).toBe("bar3");
    });

    it("should return the correct value for different keys at different timestamps", () => {
        const timeMap = new TimeMap();
        timeMap.set("foo", "bar", 1);
        timeMap.set("foo2", "bar2", 2);
        expect(timeMap.get("foo", 1)).toBe("bar");
        expect(timeMap.get("foo2", 2)).toBe("bar2");
    });
});