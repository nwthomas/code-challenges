const mergeLists = require("./combineEmojiArrays.js");

const matthew = [
    { t: 1, emoji: "smiley" },
    { t: 1, emoji: "lovingIt" },
    { t: 3, emoji: "laugh" },
];
const nathan = [
    { t: 2, emoji: "wow" },
    { t: 3, emoji: "laugh" },
    { t: 10, emoji: "wow" },
];

describe("combineEmojisArray", () => {
    test("returns combined array of emojis", () => {
        const result = mergeLists(matthew, nathan, 5);
        expect(result).toEqual([
            { t: 1, emoji: "smiley" },
            { t: 1, emoji: "lovingIt" },
            { t: 2, emoji: "wow" },
            { t: 3, emoji: "laugh" },
            { t: 3, emoji: "laugh" },
        ]);
    });

    test("returns an empty array if both arrays are empty", () => {
        const result = mergeLists([], [], 5);
        expect(result).toEqual([]);
    });

    test("returns the items in one array if the other array is empty", () => {
        const result = mergeLists(matthew, [], 5);
        expect(result).toEqual(matthew);
    });
});
