```python
# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3710
标题: Design an Array Statistics Tracker
难度: hard
链接: https://leetcode.cn/problems/design-an-array-statistics-tracker/
题目类型: 设计、队列、哈希表、二分查找、数据流、有序集合、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3369. 设计数组统计跟踪器 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用有序集合（如 SortedList）来维护数组元素，并利用其提供的高效操作来实现统计功能。

算法步骤:
1. 初始化时，创建一个空的有序集合。
2. 对于插入操作，将元素添加到有序集合中。
3. 对于删除操作，从有序集合中移除元素。
4. 对于查询操作，使用有序集合的索引访问功能来获取所需统计值。

关键点:
- 使用 SortedList 来维护数组元素，以便高效地进行插入、删除和查询操作。
- 有序集合提供了 O(log n) 的插入和删除操作，以及 O(1) 的索引访问操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 
- 插入操作: O(log n)
- 删除操作: O(log n)
- 查询操作: O(1)

空间复杂度: O(n)，其中 n 是数组的长度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from sortedcontainers import SortedList

class ArrayStatisticsTracker:
    def __init__(self):
        self.data = SortedList()

    def add(self, num: int) -> None:
        """向数组中添加一个元素"""
        self.data.add(num)

    def remove(self, num: int) -> None:
        """从数组中移除一个元素"""
        self.data.remove(num)

    def get_min(self) -> int:
        """获取当前数组中的最小值"""
        return self.data[0]

    def get_max(self) -> int:
        """获取当前数组中的最大值"""
        return self.data[-1]

    def get_median(self) -> float:
        """获取当前数组的中位数"""
        n = len(self.data)
        if n % 2 == 1:
            return self.data[n // 2]
        else:
            return (self.data[n // 2 - 1] + self.data[n // 2]) / 2

    def get_kth_smallest(self, k: int) -> int:
        """获取当前数组中的第 k 小元素"""
        return self.data[k - 1]

    def get_kth_largest(self, k: int) -> int:
        """获取当前数组中的第 k 大元素"""
        return self.data[-k]


# 示例用法
if __name__ == "__main__":
    tracker = ArrayStatisticsTracker()
    tracker.add(5)
    tracker.add(3)
    tracker.add(7)
    print(tracker.get_min())  # 输出: 3
    print(tracker.get_max())  # 输出: 7
    print(tracker.get_median())  # 输出: 5
    print(tracker.get_kth_smallest(2))  # 输出: 5
    print(tracker.get_kth_largest(2))  # 输出: 5
    tracker.remove(5)
    print(tracker.get_median())  # 输出: 5.0
```

这个实现使用了 `SortedList` 来维护数组元素，提供了高效的插入、删除和查询操作。每个方法的时间复杂度和空间复杂度都符合要求。