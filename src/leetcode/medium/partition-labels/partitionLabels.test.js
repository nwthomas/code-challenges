const { partitionLabels } = require("./partitionLabels");

describe("partitionLabels", () => {
    it("returns the correct partition labels", () => {
        expect(partitionLabels("ababcbacadefegdehijhklij")).toEqual([9, 7, 8]);
    });

    it("returns the correct partition labels", () => {
        expect(partitionLabels("eccbbbbdec")).toEqual([10]);
    });

    it("returns the correct partition labels", () => {
        expect(partitionLabels("abc")).toEqual([1, 1, 1]);
    });
});
