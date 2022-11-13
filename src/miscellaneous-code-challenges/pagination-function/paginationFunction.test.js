const buildPagePagination = require("./paginationFunction.js");

describe("buildPagePagination", () => {
    test("will return the correct pagination string for small window", () => {
        const result = buildPagePagination(10, 3, 5);
        expect(result).toBe("<4, 5* 6>");
    });

    test("will return the correct pagination string for a large window", () => {
        const result = buildPagePagination(15, 10, 8);
        expect(result).toBe("<4, 5, 6, 7, 8* 9, 10, 11, 12, 13>");
    });

    test("will return the correct pagination string for a single digit window", () => {
        const result = buildPagePagination(10, 1, 3);
        expect(result).toBe("<3*>");
    });

    test("will return a modified window if current is at end of total", () => {
        const result = buildPagePagination(15, 5, 14);
        expect(result).toBe("<11, 12, 13, 14* 15>");
    });

    test("will return a modified window if current is towards page 1", () => {
        const result = buildPagePagination(15, 5, 2);
        expect(result).toBe("<1, 2* 3, 4, 5>");
    });

    test("will throw an error if the window is greater than the total", () => {
        const result = () => {
            return buildPagePagination(10, 15, 4);
        };
        expect(result).toThrow(Error);
    });

    test("will throw an error if current is greater than total", () => {
        const result = () => {
            return buildPagePagination(10, 5, 11);
        };
        expect(result).toThrow(Error);
    });

    test("will throw an error if current is less than 1", () => {
        const result = () => {
            return buildPagePagination(6, 3, -1);
        };
        expect(result).toThrow(Error);
    });
});
