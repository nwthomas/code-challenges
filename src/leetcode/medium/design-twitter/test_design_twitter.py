from design_twitter import Twitter


def test_design_twitter_single_follow_unfollow():
    twitter = Twitter()
    twitter.postTweet(1, 1)
    twitter.postTweet(1, 2)
    twitter.postTweet(1, 3)
    twitter.postTweet(2, 4)
    assert twitter.getNewsFeed(1) == [3, 2, 1]
    twitter.follow(1, 2)
    assert twitter.getNewsFeed(1) == [4, 3, 2, 1]
    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [3, 2, 1]


def test_design_twitter_attempted_self_follow_unfollow():
    twitter = Twitter()
    twitter.postTweet(1, 1)
    twitter.postTweet(1, 2)
    twitter.postTweet(1, 3)
    twitter.follow(1, 1)
    assert twitter.getNewsFeed(1) == [3, 2, 1]
    twitter.unfollow(1, 1)
    assert twitter.getNewsFeed(1) == [3, 2, 1]


def test_design_twitter_out_of_order_tweets():
    twitter = Twitter()
    twitter.postTweet(1, 3)
    twitter.postTweet(1, 1)
    twitter.postTweet(1, 2)
    assert twitter.getNewsFeed(1) == [2, 1, 3]
