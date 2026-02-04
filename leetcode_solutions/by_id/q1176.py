# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1176
标题: Design A Leaderboard
难度: medium
链接: https://leetcode.cn/problems/design-a-leaderboard/
题目类型: 设计、哈希表、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
设计一个排行榜，支持以下操作：
1. addScore(playerId, score)：给玩家增加分数。
2. top(K)：返回前 K 名玩家的总分。
3. reset(playerId)：将指定玩家的分数重置为 0。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储每个玩家的分数，并使用有序列表（如堆）来维护分数的排序。

算法步骤:
1. 使用哈希表存储每个玩家的分数。
2. 使用一个最大堆来维护分数的排序。
3. addScore 操作更新哈希表，并在堆中更新该玩家的分数。
4. top 操作从堆中取出前 K 大的分数并求和。
5. reset 操作将哈希表中的分数重置为 0，并从堆中移除该玩家的分数。

关键点:
- 使用哈希表快速查找和更新玩家的分数。
- 使用最大堆来高效地获取前 K 大的分数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 
- addScore: O(log n)，其中 n 是玩家数量，因为需要更新堆。
- top: O(K log n)，因为需要从堆中取出前 K 大的元素。
- reset: O(log n)，因为需要从堆中移除元素。

空间复杂度: O(n)，其中 n 是玩家数量，因为需要存储每个玩家的分数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq

class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.heap = []

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            old_score = self.scores[playerId]
            self.scores[playerId] += score
            new_score = self.scores[playerId]
            # 更新堆
            for i, (s, p) in enumerate(self.heap):
                if p == playerId:
                    self.heap[i] = (-new_score, playerId)
                    break
            heapq.heapify(self.heap)
        else:
            self.scores[playerId] = score
            heapq.heappush(self.heap, (-score, playerId))

    def top(self, K: int) -> int:
        return -sum(heapq.nsmallest(K, self.heap)[i][0] for i in range(K))

    def reset(self, playerId: int) -> None:
        if playerId in self.scores:
            del self.scores[playerId]
            self.heap = [(-s, p) for s, p in self.heap if p != playerId]
            heapq.heapify(self.heap)

# 示例用法
# leaderboard = Leaderboard()
# leaderboard.addScore(1, 73)
# leaderboard.addScore(2, 56)
# leaderboard.addScore(3, 39)
# leaderboard.addScore(4, 51)
# leaderboard.addScore(5, 4)
# print(leaderboard.top(1))  # 返回 73
# leaderboard.reset(1)
# leaderboard.reset(2)
# leaderboard.addScore(2, 51)
# print(leaderboard.top(3))  # 返回 141

Solution = create_solution(Leaderboard)