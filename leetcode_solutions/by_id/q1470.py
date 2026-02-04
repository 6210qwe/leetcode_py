# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1470
标题: Tweet Counts Per Frequency
难度: medium
链接: https://leetcode.cn/problems/tweet-counts-per-frequency/
题目类型: 设计、哈希表、字符串、二分查找、有序集合、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1348. 推文计数 - 一家社交媒体公司正试图通过分析特定时间段内出现的推文数量来监控其网站上的活动。这些时间段可以根据特定的频率（ 每分钟 、每小时 或 每一天 ）划分为更小的 时间段 。 例如，周期 [10,10000] （以 秒 为单位）将被划分为以下频率的 时间块 : * 每 分钟 (60秒 块)： [10,69], [70,129], [130,189], ..., [9970,10000] * 每 小时 (3600秒 块)：[10,3609], [3610,7209], [7210,10000] * 每 天 (86400秒 块)： [10,10000] 注意，最后一个块可能比指定频率的块大小更短，并且总是以时间段的结束时间结束(在上面的示例中为 10000 )。 设计和实现一个API来帮助公司进行分析。 实现 TweetCounts 类: * TweetCounts() 初始化 TweetCounts 对象。 * 存储记录时间的 tweetName (以秒为单位)。 * List<integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) 返回一个整数列表，表示给定时间 [startTime, endTime] （单位秒）和频率频率中，每个 时间块 中带有 tweetName 的 tweet 的数量。 * freq 是 “minute” 、 “hour” 或 “day” 中的一个，分别表示 每分钟 、 每小时 或 每一天 的频率。 示例： 输入： ["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"] [[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]] 输出： [null,null,null,null,[2],[2,1],null,[4]] 解释： TweetCounts tweetCounts = new TweetCounts(); tweetCounts.recordTweet("tweet3", 0); tweetCounts.recordTweet("tweet3", 60); tweetCounts.recordTweet("tweet3", 10); // "tweet3" 发布推文的时间分别是 0, 10 和 60 。 tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // 返回 [2]。统计频率是每分钟（60 秒），因此只有一个有效时间间隔 [0,60> - > 2 条推文。 tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // 返回 [2,1]。统计频率是每分钟（60 秒），因此有两个有效时间间隔 1) [0,60> - > 2 条推文，和 2) [60,61> - > 1 条推文。 tweetCounts.recordTweet("tweet3", 120); // "tweet3" 发布推文的时间分别是 0, 10, 60 和 120 。 tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210); // 返回 [4]。统计频率是每小时（3600 秒），因此只有一个有效时间间隔 [0,211> - > 4 条推文。 提示： * 0 <= time, startTime, endTime <= 109 * 0 <= endTime - startTime <= 104 * recordTweet 和 getTweetCountsPerFrequency，最多有 104 次操作。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用有序字典存储推文时间，根据频率划分时间段并统计每个时间段内的推文数量。

算法步骤:
1. 初始化 TweetCounts 对象，使用有序字典存储每个推文名称及其发布时间。
2. 记录推文时间，将其添加到对应的推文名称的有序列表中。
3. 根据频率划分时间段，并使用二分查找统计每个时间段内的推文数量。

关键点:
- 使用有序字典和二分查找来高效地记录和查询推文时间。
- 根据频率动态计算时间段的大小。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n + m)，其中 n 是推文的数量，m 是时间段的数量。
空间复杂度: O(n)，用于存储推文时间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import defaultdict
import bisect

class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        # 使用二分插入保持列表有序
        bisect.insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == "minute":
            interval = 60
        elif freq == "hour":
            interval = 3600
        else:
            interval = 86400

        result = []
        times = self.tweets[tweetName]
        for start in range(startTime, endTime + 1, interval):
            end = min(start + interval, endTime + 1)
            count = bisect.bisect_left(times, end) - bisect.bisect_left(times, start)
            result.append(count)
        return result

# 测试用例
if __name__ == "__main__":
    tweetCounts = TweetCounts()
    tweetCounts.recordTweet("tweet3", 0)
    tweetCounts.recordTweet("tweet3", 60)
    tweetCounts.recordTweet("tweet3", 10)
    print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59))  # 输出: [2]
    print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60))  # 输出: [2, 1]
    tweetCounts.recordTweet("tweet3", 120)
    print(tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210))  # 输出: [4]