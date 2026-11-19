"""
https://leetcode.com/problems/find-median-from-data-stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:
-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.

Follow up:
If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""

from heapq import heappop, heappush


class MedianFinder:
    def __init__(self):
        self.leftHeap = []  # min heap of nums * -1
        self.rightHeap = []  # min heap, no multiplication

    def addNum(self, num: int) -> None:
        heappush(self.rightHeap, num)

        if len(self.rightHeap) > len(self.leftHeap):
            heappush(self.leftHeap, heappop(self.rightHeap) * -1)

        if self.leftHeap and self.rightHeap:
            while self.leftHeap[0] * -1 > self.rightHeap[0]:
                leftNum = heappop(self.leftHeap)
                rightNum = heappop(self.rightHeap)
                heappush(self.leftHeap, rightNum * -1)
                heappush(self.rightHeap, leftNum * -1)

    def findMedian(self) -> float:
        if len(self.leftHeap) > len(self.rightHeap):
            return self.leftHeap[0] * -1

        leftNum = self.leftHeap[0] * -1
        rightNum = self.rightHeap[0]

        return (leftNum + rightNum) / 2
