# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1023
标题: Time Based Key-Value Store
难度: medium
链接: https://leetcode.cn/problems/time-based-key-value-store/
题目类型: 设计、哈希表、字符串、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
981. 基于时间的键值存储 - 设计一个基于时间的键值数据结构，该结构可以在不同时间戳存储对应同一个键的多个值，并针对特定时间戳检索键对应的值。 实现 TimeMap 类： * TimeMap() 初始化数据结构对象 * void set(String key, String value, int timestamp) 存储给定时间戳 timestamp 时的键 key 和值 value。 * String get(String key, int timestamp) 返回一个值，该值在之前调用了 set，其中 timestamp_prev <= timestamp 。如果有多个这样的值，它将返回与最大 timestamp_prev 关联的值。如果没有值，则返回空字符串（""）。 示例 1： 输入： ["TimeMap", "set", "get", "get", "set", "get", "get"] [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]] 输出： [null, null, "bar", "bar", null, "bar2", "bar2"] 解释： TimeMap timeMap = new TimeMap(); timeMap.set("foo", "bar", 1); // 存储键 "foo" 和值 "bar" ，时间戳 timestamp = 1 timeMap.get("foo", 1); // 返回 "bar" timeMap.get("foo", 3); // 返回 "bar", 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"） 。 timeMap.set("foo", "bar2", 4); // 存储键 "foo" 和值 "bar2" ，时间戳 timestamp = 4 timeMap.get("foo", 4); // 返回 "bar2" timeMap.get("foo", 5); // 返回 "bar2" 提示： * 1 <= key.length, value.length <= 100 * key 和 value 由小写英文字母和数字组成 * 1 <= timestamp <= 107 * set 操作中的时间戳 timestamp 都是严格递增的 * 最多调用 set 和 get 操作 2 * 105 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储每个键的时间戳和对应的值，使用二分查找来快速检索特定时间戳的值。

算法步骤:
1. 使用一个字典 `time_map` 来存储每个键的时间戳和对应的值。
2. 在 `set` 方法中，将键、时间戳和值存储在 `time_map` 中。
3. 在 `get` 方法中，使用二分查找来找到小于或等于给定时间戳的最大时间戳，并返回对应的值。

关键点:
- 使用哈希表存储键的时间戳和值。
- 使用二分查找来快速检索特定时间戳的值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 对于 `get` 操作，使用二分查找的时间复杂度为 O(log n)，其中 n 是某个键的时间戳数量。
空间复杂度: O(n) - 存储所有键的时间戳和值需要 O(n) 的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Dict, List


class TimeMap:
    def __init__(self):
        self.time_map: Dict[str, List[tuple]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        
        values = self.time_map[key]
        left, right = 0, len(values) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        if right >= 0 and values[right][0] <= timestamp:
            return values[right][1]
        return ""


Solution = TimeMap