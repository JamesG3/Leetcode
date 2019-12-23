import time
    
    
class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follow_dict = {}
        self.users = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.users:
            self.users[userId] = []
        self.users[userId].append([tweetId, time.time()])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        follow = self.follow_dict.get(userId, set([]))
        follow.update(set([userId]))
        feeds = []
        for uid in follow:
            feeds += self.users.get(uid, [])
        return [_[0] for _ in sorted(feeds, key = lambda x: x[1], reverse = True)[:10]]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.follow_dict:
            self.follow_dict[followerId] = set([])
        self.follow_dict[followerId].add(followeeId)
            

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.follow_dict:
            if followeeId in self.follow_dict[followerId]:
                self.follow_dict[followerId].remove(followeeId)
                
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)



'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.

Solution: Hashtable, function getNewsFeed() can be optimized spacewise and timewise by applying sorting algorithm
'''
