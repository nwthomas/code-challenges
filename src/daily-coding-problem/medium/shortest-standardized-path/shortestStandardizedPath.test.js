const findShortestStandardizedPath = require("./shortestStandardizedPath.js");

describe("findShortestStandardizedPath", () => {
    it("returns correct shortened path for short string", () => {
        const originalPath = "/usr/bin/../bin/./scripts/../";
        const result = findShortestStandardizedPath(originalPath);

        expect(result).toBe("/usr/bin/");
    });

    it("returns an empty string when the path is empty", () => {
        const originalPath = "";
        const result = findShortestStandardizedPath(originalPath);

        expect(result).toBe("");
    });

    it("can handle a single short direction", () => {
        const originalPath = "../";
        const result = findShortestStandardizedPath(originalPath);

        expect(result).toBe(originalPath);
    });

    it("throws an TypeError when the argument passed in is not of type string", () => {
        const originalPath = {};
        const result = () => findShortestStandardizedPath(originalPath);

        expect(result).toThrow(
            TypeError(
                "The argument for findShortestStandardizedPath must be of type string",
            ),
        );
    });

    it("can handle backing out of parent directory", () => {
        const originalPath = "./../.././../";
        const result = findShortestStandardizedPath(originalPath);

        expect(result).toBe("../../../");
    });
});
