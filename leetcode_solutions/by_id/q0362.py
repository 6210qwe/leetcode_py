# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 362
标题: Design Hit Counter
难度: medium
链接: https://leetcode.cn/problems/design-hit-counter/
题目类型: 设计、队列、数组、二分查找、数据流
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
362. 敲击计数器 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 队列维护最近 300 秒内的敲击记录，并维护当前总次数，访问前先清理过期记录。

算法步骤:
1. 使用双端队列保存 (timestamp, count) 对，表示在某一时间戳发生了 count 次 hit；同时维护一个总次数 `total`。
2. 每次 hit(timestamp)：
   - 先调用内部函数 `_evict(timestamp)`，弹出所有时间戳小于 `timestamp-299` 的记录并从 `total` 中减去对应次数。
   - 若队尾记录的时间戳等于当前 timestamp，则将其 count 加一；否则向队尾追加一条新记录 (timestamp, 1)。并将 `total` 加一。
3. 每次 getHits(timestamp)：同样先 `_evict(timestamp)` 清理过期记录，然后返回 `total`。

关键点:
- 利用时间戳单调递增的条件，只需从队头往外弹出过期记录，整个队列每条记录只进出一次。
- 同一时间戳的多次 hit 合并成一条记录，减少队列长度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: hit 和 getHits 均为 O(1) 均摊，每条记录最多入队、出队各一次。
空间复杂度: O(k)，k 为最近 300 秒内不同时间戳的数量，上界为 300。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class HitCounter:
    """
    敲击计数器：记录过去 300 秒内的 hit 次数。

    使用队列维护 (timestamp, count) 对，并在查询/新增时清理过期数据。
    """

    def __init__(self):
        from collections import deque

        self.q = deque()  # (timestamp, count)
        self.total = 0

    def _evict(self, timestamp: int) -> None:
        # 删除 300 秒之前的记录（只保留 timestamp-299 ~ timestamp）
        while self.q and timestamp - self.q[0][0] >= 300:
            t, c = self.q.popleft()
            self.total -= c

    def hit(self, timestamp: int) -> None:
        self._evict(timestamp)
        if self.q and self.q[-1][0] == timestamp:
            t, c = self.q.pop()
            self.q.append((t, c + 1))
        else:
            self.q.append((timestamp, 1))
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        self._evict(timestamp)
        return self.total


def design_hit_counter() -> HitCounter:
    """
    函数式接口 - 返回 HitCounter 实例，便于在测试中进行方法调用。
    """
    return HitCounter()


# 自动生成Solution类（无需手动编写）
Solution = create_solution(design_hit_counter)
