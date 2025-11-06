const { insert } = require("./insertInterval");

/*
Convert these to tests below

   def test_returns_new_interval_if_empty_list(self):
        """Takes in no intervals + new interval and returns new interval"""
        result = insert([], [5, 6])
        self.assertEqual(result, [[5, 6]])

    def test_returns_new_interval_at_beginning(self):
        """Takes in intervals + new interval and places it at beginning unmerged"""
        result = insert([[4, 5], [6, 7]], [0, 0])
        self.assertEqual(result, [[0, 0], [4, 5], [6, 7]])

    def test_returns_new_interval_at_end(self):
        """Takes in intervals + new interval and places it at end unmerged"""
        result = insert([[3, 4], [5, 6], [7, 8]], [9, 10])
        self.assertEqual(result, [[3, 4], [5, 6], [7, 8], [9, 10]])
    
    def test_returns_new_interval_in_middle(self):
        """Takes in intervals + new interval and places it in middle unmerged"""
        result = insert([[0, 0], [9, 10]], [5, 6])
        self.assertEqual(result, [[0, 0], [5, 6], [9, 10]])

    def test_merges_new_interval_and_existing_intervals(self):
        """Takes in intervals + new interval and merges them all together"""
        result = insert([[0, 3], [2, 8], [15, 20], [16, 19]], [7, 16])
        self.assertEqual(result, [[0, 19]])

    def test_merges_new_interval_at_single_point(self):
        """Takes in intervals + new interval and merges it in the correct spot"""
        result = insert([[0, 3], [5, 8], [16, 19]], [7, 10])
        self.assertEqual(result, [[0, 3], [5, 10], [16, 19]])
        */

describe("insert", () => {
    it("returns the new interval if the list is empty", () => {
        const result = insert([], [5, 6]);
        expect(result).toEqual([[5, 6]]);
    });

    it("returns the new interval at the beginning if new interval is less than first interval start", () => {
        const result = insert([[4, 5], [6, 7]], [0, 1]);
        expect(result).toEqual([[0, 1], [4, 5], [6, 7]]);
    });
    
    it("returns the new interval at the end if new interval is greater than last interval end", () => {
        const result = insert([[3, 4], [5, 6], [7, 8]], [9, 10]);
        expect(result).toEqual([[3, 4], [5, 6], [7, 8], [9, 10]]);
    });

    it("returns the new interval in the middle if new interval is between two intervals", () => {
        const result = insert([[0, 0], [9, 10]], [5, 6]);
        expect(result).toEqual([[0, 0], [5, 6], [9, 10]]);
    });

    it("merges the new interval and the existing intervals if new interval is spanning multiple intervals", () => {
        const result = insert([[0, 3], [4, 8], [15, 16], [17, 20]], [0, 17]);
        expect(result).toEqual([[0, 20]]);
    });

    it("merges the new interval at the single point if new interval is overlapping with a single interval", () => {
        const result = insert([[0, 3], [5, 8], [16, 19]], [7, 10]);
        expect(result).toEqual([[0, 3], [5, 10], [16, 19]]);
    });
});