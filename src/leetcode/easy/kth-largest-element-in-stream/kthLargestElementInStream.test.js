const { KthLargest } = require("./kthLargestElementInStream");

describe("KthLargest", () => {
    it("should return the kth largest element in the stream", () => {
        const kthLargest = new KthLargest(3, [4, 5, 8, 2]);
        expect(kthLargest.add(3)).toBe(4);
        expect(kthLargest.add(5)).toBe(5);
        expect(kthLargest.add(10)).toBe(5);
        expect(kthLargest.add(9)).toBe(8);
        expect(kthLargest.add(4)).toBe(8);
    });

    it("should return the kth largest element in the stream with a large stream", () => {
        const kthLargest = new KthLargest(
            4,
            [7, 7, 7, 7, 8, 3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        );
        expect(kthLargest.add(2)).toBe(17);
        expect(kthLargest.add(10)).toBe(17);
        expect(kthLargest.add(21)).toBe(18);
        expect(kthLargest.add(9)).toBe(18);
    });
});
