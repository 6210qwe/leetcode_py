# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2762
标题: Cache With Time Limit
难度: medium
链接: https://leetcode.cn/problems/cache-with-time-limit/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2622. 有时间限制的缓存 - 编写一个类，它允许获取和设置键-值对，并且每个键都有一个 过期时间 。 该类有三个公共方法： set(key, value, duration) ：接收参数为整型键 key 、整型值 value 和以毫秒为单位的持续时间 duration 。一旦 duration 到期后，这个键就无法访问。如果相同的未过期键已经存在，该方法将返回 true ，否则返回 false 。如果该键已经存在，则它的值和持续时间都应该被覆盖。 get(key) ：如果存在一个未过期的键，它应该返回这个键相关的值。否则返回 -1 。 count() ：返回未过期键的总数。 示例 1： 输入： actions = ["TimeLimitedCache", "set", "get", "count", "get"] values = [[], [1, 42, 100], [1], [], [1]] timeDelays = [0, 0, 50, 50, 150] 输出： [null, false, 42, 1, -1] 解释： 在 t=0 时，缓存被构造。 在 t=0 时，添加一个键值对 (1: 42) ，过期时间为 100ms 。因为该值不存在，因此返回false。 在 t=50 时，请求 key=1 并返回值 42。 在 t=50 时，调用 count() ，缓存中有一个未过期的键。 在 t=100 时，key=1 到期。 在 t=150 时，调用 get(1) ，返回 -1，因为缓存是空的。 示例 2： 输入： actions = ["TimeLimitedCache", "set", "set", "get", "get", "get", "count"] values = [[], [1, 42, 50], [1, 50, 100], [1], [1], [1], []] timeDelays = [0, 0, 40, 50, 120, 200, 250] 输出： [null, false, true, 50, 50, -1] 解释： 在 t=0 时，缓存被构造。 在 t=0 时，添加一个键值对 (1: 42) ，过期时间为 50ms。因为该值不存在，因此返回false。 当 t=40 时，添加一个键值对 (1: 50) ，过期时间为 100ms。因为一个未过期的键已经存在，返回 true 并覆盖这个键的旧值。 在 t=50 时，调用 get(1) ，返回 50。 在 t=120 时，调用 get(1) ，返回 50。 在 t=140 时，key=1 过期。 在 t=200 时，调用 get(1) ，但缓存为空，因此返回 -1。 在 t=250 时，count() 返回0 ，因为缓存是空的，没有未过期的键。 提示： * 0 <= key, value <= 109 * 0 <= duration <= 1000 * 1 <= actions.length <= 100 * actions.length === values.length * actions.length === timeDelays.length * 0 <= timeDelays[i] <= 1450 * actions[i] 是 "TimeLimitedCache"、"set"、"get" 和 "count" 中的一个。 * 第一个操作始终是 "TimeLimitedCache" 而且一定会以 0 毫秒的延迟立即执行
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典来存储键值对及其过期时间，并使用一个计时器来管理过期时间。

算法步骤:
1. 初始化一个字典 `cache` 来存储键值对及其过期时间。
2. `set` 方法：检查键是否已存在且未过期，如果存在则更新值和过期时间并返回 True，否则插入新键值对并返回 False。
3. `get` 方法：检查键是否存在且未过期，如果存在则返回值，否则返回 -1。
4. `count` 方法：遍历字典，统计未过期的键的数量。

关键点:
- 使用字典来存储键值对及其过期时间。
- 使用 `time.time()` 来管理过期时间。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - `set` 和 `get` 操作的时间复杂度都是 O(1)，`count` 操作的时间复杂度是 O(n)，其中 n 是缓存中的键的数量。
空间复杂度: O(n) - 存储键值对及其过期时间的空间复杂度是 O(n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

import time

class TimeLimitedCache:
    def __init__(self):
        self.cache = {}

    def set(self, key: int, value: int, duration: int) -> bool:
        current_time = time.time()
        if key in self.cache and self.cache[key][1] > current_time:
            self.cache[key] = (value, current_time + duration / 1000)
            return True
        else:
            self.cache[key] = (value, current_time + duration / 1000)
            return False

    def get(self, key: int) -> int:
        current_time = time.time()
        if key in self.cache and self.cache[key][1] > current_time:
            return self.cache[key][0]
        return -1

    def count(self) -> int:
        current_time = time.time()
        return sum(1 for key in self.cache if self.cache[key][1] > current_time)

# 示例测试
if __name__ == "__main__":
    cache = TimeLimitedCache()
    print(cache.set(1, 42, 100))  # False
    print(cache.get(1))           # 42
    print(cache.count())          # 1
    time.sleep(0.15)
    print(cache.get(1))           # -1
    print(cache.count())          # 0