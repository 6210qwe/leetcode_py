# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2357
标题: Count Integers in Intervals
难度: hard
链接: https://leetcode.cn/problems/count-integers-in-intervals/
题目类型: 设计、线段树、有序集合
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2276. 统计区间中的整数数目 - 给你区间的 空 集，请你设计并实现满足要求的数据结构： * 新增：添加一个区间到这个区间集合中。 * 统计：计算出现在 至少一个 区间中的整数个数。 实现 CountIntervals 类： * CountIntervals() 使用区间的空集初始化对象 * void add(int left, int right) 添加区间 [left, right] 到区间集合之中。 * int count() 返回出现在 至少一个 区间中的整数个数。 注意：区间 [left, right] 表示满足 left <= x <= right 的所有整数 x 。 示例 1： 输入 ["CountIntervals", "add", "add", "count", "add", "count"] [[], [2, 3], [7, 10], [], [5, 8], []] 输出 [null, null, null, 6, null, 8] 解释 CountIntervals countIntervals = new CountIntervals(); // 用一个区间空集初始化对象 countIntervals.add(2, 3); // 将 [2, 3] 添加到区间集合中 countIntervals.add(7, 10); // 将 [7, 10] 添加到区间集合中 countIntervals.count(); // 返回 6 // 整数 2 和 3 出现在区间 [2, 3] 中 // 整数 7、8、9、10 出现在区间 [7, 10] 中 countIntervals.add(5, 8); // 将 [5, 8] 添加到区间集合中 countIntervals.count(); // 返回 8 // 整数 2 和 3 出现在区间 [2, 3] 中 // 整数 5 和 6 出现在区间 [5, 8] 中 // 整数 7 和 8 出现在区间 [5, 8] 和区间 [7, 10] 中 // 整数 9 和 10 出现在区间 [7, 10] 中 提示： * 1 <= left <= right <= 109 * 最多调用 add 和 count 方法 总计 105 次 * 调用 count 方法至少一次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用有序集合来存储区间，并在添加区间时进行合并操作，以确保区间不重叠。

算法步骤:
1. 初始化一个有序集合 `intervals` 来存储区间。
2. 在 `add` 方法中，找到新区间与现有区间的所有交集，并进行合并。
3. 在 `count` 方法中，遍历有序集合中的所有区间，计算总长度。

关键点:
- 使用有序集合来高效地管理和合并区间。
- 在添加区间时，确保区间不重叠。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n + m) 其中 n 是区间数量，m 是新区间的长度。
空间复杂度: O(n) 其中 n 是区间数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from sortedcontainers import SortedDict

class CountIntervals:

    def __init__(self):
        self.intervals = SortedDict()
        self.total_count = 0

    def add(self, left: int, right: int) -> None:
        # 找到第一个大于等于 left 的区间
        i = self.intervals.bisect_left(left)
        
        # 合并区间
        while i < len(self.intervals) and self.intervals.values()[i] <= right:
            l, r = self.intervals.items()[i]
            left = min(left, l)
            right = max(right, r)
            self.total_count -= (r - l + 1)
            del self.intervals[l]
        
        # 插入新区间
        self.intervals[left] = right
        self.total_count += (right - left + 1)

    def count(self) -> int:
        return self.total_count


# 示例测试
if __name__ == "__main__":
    obj = CountIntervals()
    obj.add(2, 3)
    obj.add(7, 10)
    print(obj.count())  # 输出 6
    obj.add(5, 8)
    print(obj.count())  # 输出 8