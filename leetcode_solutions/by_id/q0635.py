# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 635
标题: Design Log Storage System
难度: medium
链接: https://leetcode.cn/problems/design-log-storage-system/
题目类型: 设计、哈希表、字符串、有序集合
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
635. 设计日志存储系统 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个字典来存储每个日志的ID和时间戳，并使用一个有序集合来存储所有的时间戳以便快速查找。

算法步骤:
1. 初始化一个字典 `logs` 来存储日志ID和时间戳，以及一个有序集合 `timestamps` 来存储所有的时间戳。
2. 在 `put` 方法中，将日志ID和时间戳添加到 `logs` 字典中，并将时间戳添加到 `timestamps` 有序集合中。
3. 在 `retrieve` 方法中，使用 `timestamps` 有序集合来快速找到在给定范围内的所有时间戳，并返回这些时间戳对应的日志ID。

关键点:
- 使用有序集合来存储时间戳，可以快速查找指定范围的时间戳。
- 使用字典来存储日志ID和时间戳，可以快速获取日志ID。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 有序集合的插入和查找操作的时间复杂度为 O(log n)。
空间复杂度: O(n) - 存储 n 个日志的时间戳和ID。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from sortedcontainers import SortedSet


class LogSystem:

    def __init__(self):
        self.logs = {}
        self.timestamps = SortedSet()

    def put(self, id: int, timestamp: str) -> None:
        self.logs[timestamp] = id
        self.timestamps.add(timestamp)

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        # 根据粒度截断时间戳
        start = self._truncate(start, granularity)
        end = self._truncate(end, granularity, is_end=True)
        
        # 找到在给定范围内的所有时间戳
        range_timestamps = self.timestamps.irange(start, end, inclusive=(True, True))
        
        # 返回这些时间戳对应的日志ID
        return [self.logs[ts] for ts in range_timestamps]

    def _truncate(self, timestamp: str, granularity: str, is_end: bool = False) -> str:
        units = ["Year", "Month", "Day", "Hour", "Minute", "Second"]
        idx = units.index(granularity)
        parts = timestamp.split(':')
        if is_end:
            for i in range(idx + 1, len(parts)):
                parts[i] = '99' if i % 2 == 0 else '59'
        else:
            for i in range(idx + 1, len(parts)):
                parts[i] = '00'
        return ':'.join(parts)


# 示例用法
if __name__ == "__main__":
    log_system = LogSystem()
    log_system.put(1, "2017:01:01:23:59:59")
    log_system.put(2, "2017:01:02:20:59:59")
    print(log_system.retrieve("2017:01:01:23:59:59", "2017:01:02:20:59:59", "Day"))  # 输出: [1, 2]
    print(log_system.retrieve("2017:01:01:23:59:59", "2017:01:02:20:59:59", "Hour"))  # 输出: [1, 2]

Solution = create_solution(LogSystem)