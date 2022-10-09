const findShortestStandardizedPath = require("./shortestStandardizedPath.js");

describe("findShortestStandardizedPath", () => {
    it("returns correct shortened path for short string", () => {
        const originalPath = "/usr/bin/../bin/./scripts/../";
        const result = findShortestStandardizedPath(originalPath);

        expect(result).toBe("/usr/bin/");
    });
});
