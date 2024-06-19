const groupAnagrams = require("./groupAnagrams");

describe(groupAnagrams.name, () => {
    test("handles one single string", () => {
        const result = groupAnagrams(["asdf"]);
        expect(result).toEqual([["asdf"]]);
    });

    test("groups two strings together", () => {
        const result = groupAnagrams(["asdf", "asfd"]);
        expect(result).toEqual([["asdf", "asfd"]]);
    });

    test("groups and separates various different anagram strings", () => {
        const result = groupAnagrams(["asdf", "asfd", "asd", "test", "tets"]);
        expect(result).toEqual([["asdf", "asfd"], ["asd"], ["test", "tets"]]);
    });
});
