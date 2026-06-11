import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        followees = set(self.follow_map[userId])
        followees.add(userId)
        for followeeId in followees:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                time, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(min_heap, [-time, tweetId, followeeId, index - 1])

        while min_heap and len(res) < 10:
            time, tweetId, followeeId, idx = heapq.heappop(min_heap)
            res.append(tweetId)

            if idx >= 0:
                next_time, next_tweetId = self.tweet_map[followeeId][idx]
                heapq.heappush(min_heap, [-next_time, next_tweetId, followeeId,idx - 1 ])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)

        
