const { checkInclusion } = require("./permutationInString");

describe("checkInclusion", () => {
    it("returns true if s2 contains a permutation of s1", () => {
        const result = checkInclusion("abc", "lecabee");
        expect(result).toBeTruthy();
    });

    it("returns false if s2 does not contain a permutation of s1", () => {
        const result = checkInclusion("abc", "lecaabee");
        expect(result).toBeFalsy();
    });

    it("correctly returns true if s2 contains a permutation of s1 with multiple characters", () => {
        const result = checkInclusion("adc", "dadclecabee");
        expect(result).toBeTruthy();
    });
});
