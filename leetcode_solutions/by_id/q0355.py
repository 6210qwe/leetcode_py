# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 355
标题: Design Twitter
难度: medium
链接: https://leetcode.cn/problems/design-twitter/
题目类型: 设计、哈希表、链表、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
355. 设计推特 - 设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近 10 条推文。 实现 Twitter 类： * Twitter() 初始化简易版推特对象 * void postTweet(int userId, int tweetId) 根据给定的 tweetId 和 userId 创建一条新推文。每次调用此函数都会使用一个不同的 tweetId 。 * List<Integer> getNewsFeed(int userId) 检索当前用户新闻推送中最近 10 条推文的 ID 。新闻推送中的每一项都必须是由用户关注的人或者是用户自己发布的推文。推文必须 按照时间顺序由最近到最远排序 。 * void follow(int followerId, int followeeId) ID 为 followerId 的用户开始关注 ID 为 followeeId 的用户。 * void unfollow(int followerId, int followeeId) ID 为 followerId 的用户不再关注 ID 为 followeeId 的用户。 示例： 输入 ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"] [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]] 输出 [null, null, [5], null, null, [6, 5], null, [5]] 解释 Twitter twitter = new Twitter(); twitter.postTweet(1, 5); // 用户 1 发送了一条新推文 (用户 id = 1, 推文 id = 5) twitter.getNewsFeed(1); // 用户 1 的获取推文应当返回一个列表，其中包含一个 id 为 5 的推文 twitter.follow(1, 2); // 用户 1 关注了用户 2 twitter.postTweet(2, 6); // 用户 2 发送了一个新推文 (推文 id = 6) twitter.getNewsFeed(1); // 用户 1 的获取推文应当返回一个列表，其中包含两个推文，id 分别为 -> [6, 5] 。推文 id 6 应当在推文 id 5 之前，因为它是在 5 之后发送的 twitter.unfollow(1, 2); // 用户 1 取消关注了用户 2 twitter.getNewsFeed(1); // 用户 1 获取推文应当返回一个列表，其中包含一个 id 为 5 的推文。因为用户 1 已经不再关注用户 2 提示： * 1 <= userId, followerId, followeeId <= 500 * 0 <= tweetId <= 104 * 所有推特的 ID 都互不相同 * postTweet、getNewsFeed、follow 和 unfollow 方法最多调用 3 * 104 次 * 用户不能关注自己
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 设计用户-关注关系表和用户-推文列表，并用小顶堆按时间戳合并 K 路有序流，得到最近的 10 条推文

算法步骤:
1. 使用字典 followees[u] 维护用户 u 关注的用户集合（通常默认自己也关注自己，便于统一处理）。
2. 使用字典 tweets[u] 存储用户 u 发表的推文列表，每条推文记为 (time, tweetId)，time 为递增的全局时间戳。
3. postTweet(userId, tweetId)：给当前推文分配时间戳，将其追加到 tweets[userId] 的末尾。
4. getNewsFeed(userId)：
   - 收集该用户自己及其所有关注用户的最近若干条推文（如只取每人最后 10 条），这些序列都按时间戳递减有序。
   - 将每个用户的最新一条推文放入一个以时间戳为键的小顶/大顶堆中，反复弹出时间最新的推文，并推进对应用户在其列表中的下一个推文，直到取满 10 条或堆为空。
5. follow / unfollow：在 followees 映射中增加或删除对应的关注关系，注意不能取消关注自己。

关键点:
- 使用全局递增时间戳来比较不同用户推文的新旧，而不是依赖数组下标。
- getNewsFeed 只需返回最多 10 条推文，可限制每个用户参与归并的推文数量以控制堆大小。
- 需要妥善处理边界情况：用户不存在推文、关注列表为空、重复关注等。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: postTweet 与 follow / unfollow 为 O(1) 均摊；getNewsFeed 设关注人数为 F，则复杂度约为 O((F + 10) log F)。
空间复杂度: O(T + F) - T 为总推文数（存储所有推文），F 为所有关注关系的规模。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class Twitter:
    """
    简化版推特设计：支持发推、关注/取关、获取最近 10 条推文。

    使用全局时间戳记录推文时间，用堆按时间戳合并多路有序流。
    """

    def __init__(self):
        import collections

        self.time = 0
        self.tweets = collections.defaultdict(list)   # userId -> [(time, tweetId), ...]
        self.followees = collections.defaultdict(set)  # userId -> set(followeeId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        import heapq

        self.followees[userId].add(userId)
        heap: list[tuple[int, int, int]] = []  # (-time, userId, idx)
        for uid in self.followees[userId]:
            if self.tweets[uid]:
                t, tid = self.tweets[uid][-1]
                heapq.heappush(heap, (-t, uid, len(self.tweets[uid]) - 1))

        res: List[int] = []
        while heap and len(res) < 10:
            neg_t, uid, idx = heapq.heappop(heap)
            res.append(self.tweets[uid][idx][1])
            if idx > 0:
                t, tid = self.tweets[uid][idx - 1]
                heapq.heappush(heap, (-t, uid, idx - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followees[followerId].discard(followeeId)


def design_twitter() -> Twitter:
    """
    函数式接口 - 返回 Twitter 实例，便于在测试中进行方法调用。
    """
    return Twitter()


# 自动生成Solution类（无需手动编写）
Solution = create_solution(design_twitter)
