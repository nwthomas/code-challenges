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
        self.small = []
        self.large = []

    def add_num(self, num: int) -> None:
        if self.is_even() and len(self.small) < 1 and len(self.large) < 1:
            heappush(self.large, num)
        elif not self.is_even() and len(self.small) < 1:
            heappush(self.large, num)
            heappush(self.small, heappop(self.large) * -1)
        else:
            was_even = self.is_even()
            heappush(self.large, num)
            
            if self.small[0] * -1 > self.large[0]:
                small = heappop(self.small) * -1
                large = heappop(self.large)
                heappush(self.small, large * -1)
                heappush(self.large, small)
                
            if not was_even:
                heappush(self.small, heappop(self.large) * -1)
        
    def find_median(self) -> float:
        return ((self.small[0] * -1) + self.large[0]) / 2 if self.is_even() else self.large[0]
    
    def is_even(self) -> bool:
        return (len(self.small) + len(self.large)) % 2 == 0