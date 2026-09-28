import { describe, it, expect } from "vitest";

import { partitionLabels } from "./partitionLabels.ts";

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
