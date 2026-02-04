# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000028
标题: Continuous Median LCCI
难度: hard
链接: https://leetcode.cn/problems/continuous-median-lcci/
题目类型: 设计、双指针、数据流、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 17.20. 连续中值 - 随机产生数字并传递给一个方法。你能否完成这个方法，在每次产生新值时，寻找当前所有值的中间值（中位数）并保存。 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。 例如， [2,3,4] 的中位数是 3 [2,3] 的中位数是 (2 + 3) / 2 = 2.5 设计一个支持以下两种操作的数据结构： * void addNum(int num) - 从数据流中添加一个整数到数据结构中。 * double findMedian() - 返回目前所有元素的中位数。 示例： addNum(1) addNum(2) findMedian() -> 1.5 addNum(3) findMedian() -> 2
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个堆（最大堆和最小堆）来维护数据流中的中位数。
- 最大堆存储较小的一半数据，最小堆存储较大的一半数据。
- 保证两个堆的大小差不超过1。

算法步骤:
1. 初始化两个堆：最大堆和最小堆。
2. 添加新数时，根据当前两个堆的大小关系，决定将新数添加到哪个堆中。
3. 调整堆以保持平衡，并确保最大堆的所有元素都小于最小堆的所有元素。
4. 查找中位数时，根据两个堆的大小关系返回中位数。

关键点:
- 使用堆来高效地维护中位数。
- 保持两个堆的平衡。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 每次插入和查找中位数的时间复杂度。
空间复杂度: O(n) - 存储所有数据的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

import heapq

class MedianFinder:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.max_heap = []  # 最大堆，存储较小的一半数据
        self.min_heap = []  # 最小堆，存储较大的一半数据

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # 平衡两个堆
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]


# 示例用法
if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # 输出 1.5
    mf.addNum(3)
    print(mf.findMedian())  # 输出 2.0