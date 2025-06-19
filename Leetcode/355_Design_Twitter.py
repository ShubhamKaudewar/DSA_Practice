import pytest
from collections import defaultdict
from typing import List
import heapq

class Twitter:
    def __init__(self):
        self.posts = defaultdict(list)
        self.feeds = defaultdict(list)
        self.followers = defaultdict(set)
        self.following = defaultdict(set)
        self.sequence_id = 1
        self.post_sequence = defaultdict(int)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append(tweetId)
        self.feeds[userId].append(tweetId)
        self.post_sequence[self.sequence_id] = tweetId
        self.sequence_id += 1
        
        for followerId in self.followers[userId]:
            self.feeds[followerId].append(tweetId)
        
    # def getNewsFeed(self, userId: int) -> List[int]:
    #     user_feeds = self.feeds[userId]
    #     ordered_feeds = []
    #     for k in sorted(self.post_sequence.keys())[::-1]:
    #         if self.post_sequence[k] in user_feeds:
    #             ordered_feeds.append(self.post_sequence[k])
    #     return ordered_feeds[:10]
    
    # Using heapq
    def getNewsFeed(self, userId: int) -> List[int]:
        user_feeds = set(self.feeds[userId])
        max_heap = [(-seq, tid) for seq, tid in self.post_sequence.items() if tid in user_feeds]
        heapq.heapify(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in range(min(10, len(max_heap)))]
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followeeId].add(followerId)
        self.feeds[followerId].extend(self.posts[followeeId])
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId)
            followee_posts = set(self.posts[followeeId])
            follower_feed = set(self.feeds[followerId])
            self.feeds[followerId] = list(follower_feed - followee_posts)
        
def test_case_1():
    twitter = Twitter()
    commands = ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
    values = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]

    response = []
    for command, value in zip(commands, values):
        if command == "Twitter":
            twitter = Twitter()
            response.append(None)
        elif command == "postTweet":
            twitter.postTweet(*value)
            response.append(None)
        elif command == "getNewsFeed":
            response.append(twitter.getNewsFeed(*value))
        elif command == "follow":
            twitter.follow(*value)
            response.append(None)
        elif command == "unfollow":
            twitter.unfollow(*value)
            response.append(None)

    expected = [None, None, [5], None, None, [6, 5], None, [5]]
    assert response == expected
        
def test_case_2():
    twitter = Twitter()
    commands = ["Twitter","postTweet","getNewsFeed","follow","getNewsFeed","unfollow","getNewsFeed"]
    values = [[],[1,1],[1],[2,1],[2],[2,1],[2]]

    response = []
    for command, value in zip(commands, values):
        if command == "Twitter":
            twitter = Twitter()
            response.append(None)
        elif command == "postTweet":
            twitter.postTweet(*value)
            response.append(None)
        elif command == "getNewsFeed":
            response.append(twitter.getNewsFeed(*value))
        elif command == "follow":
            twitter.follow(*value)
            response.append(None)
        elif command == "unfollow":
            twitter.unfollow(*value)
            response.append(None)

    expected = [None,None,[1],None,[1],None,[]]
    assert response == expected

def test_case_3():
    twitter = Twitter()
    commands = ["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","follow","getNewsFeed","unfollow","getNewsFeed"]
    values = [[],[1,5],[2,3],[1,101],[2,13],[2,10],[1,2],[1,94],[2,505],[1,333],[2,22],[1,11],[1,205],[2,203],[1,201],[2,213],[1,200],[2,202],[1,204],[2,208],[2,233],[1,222],[2,211],[1],[1,2],[1],[1,2],[1]]

    response = []
    for command, value in zip(commands, values):
        if command == "Twitter":
            twitter = Twitter()
            response.append(None)
        elif command == "postTweet":
            twitter.postTweet(*value)
            response.append(None)
        elif command == "getNewsFeed":
            response.append(twitter.getNewsFeed(*value))
        elif command == "follow":
            twitter.follow(*value)
            response.append(None)
        elif command == "unfollow":
            twitter.unfollow(*value)
            response.append(None)

    expected = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,[222,204,200,201,205,11,333,94,2,101],None,[211,222,233,208,204,202,200,213,201,203],None,[222,204,200,201,205,11,333,94,2,101]]
    assert response == expected

if __name__ == '__main__':
    pytest.main()