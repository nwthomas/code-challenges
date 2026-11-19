

from find_median_from_data_stream import MedianFinder


def test_finds_median_in_small_data_stream():
    mf = MedianFinder()
    mf.addNum(5),
    mf.addNum(10)
    first_median = mf.findMedian()
    mf.addNum(3)
    second_median = mf.findMedian()
    assert first_median == 7.5
    assert second_median == 5


def test_finds_media_in_large_data_stream():
    mf = MedianFinder()

    for i in range(1000000):
        mf.addNum(i)

    median = mf.findMedian()
    assert median == 499999.5
