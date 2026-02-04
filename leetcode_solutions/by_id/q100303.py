# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100303
标题: 数据流中的中位数
难度: hard
链接: https://leetcode.cn/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/
题目类型: 设计、双指针、数据流、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 160. 数据流中的中位数 - 中位数 是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。 例如， [2,3,4] 的中位数是 3 [2,3] 的中位数是 (2 + 3) / 2 = 2.5 设计一个支持以下两种操作的数据结构： * void addNum(int num) - 从数据流中添加一个整数到数据结构中。 * double findMedian() - 返回目前所有元素的中位数。 示例 1： 输入： ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"] [[],[1],[2],[],[3],[]] 输出：[null,null,null,1.50000,null,2.00000] 示例 2： 输入： ["MedianFinder","addNum","findMedian","addNum","findMedian"] [[],[2],[],[3],[]] 输出：[null,null,2.00000,null,2.50000] 提示： * 最多会对 addNum、findMedian 进行 50000 次调用。 注意：本题与主站 295 题相同：https://leetcode.cn/problems/find-median-from-data-stream/ [https://leetcode.cn/problems/find-median-from-data-stream/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个堆（大根堆和小根堆）来维护数据流中的中位数。

算法步骤:
1. 初始化两个堆：大根堆 `max_heap` 用于存储较小的一半数据，小根堆 `min_heap` 用于存储较大的一半数据。
2. 在 `addNum` 方法中：
   - 如果 `max_heap` 为空或新数小于等于 `max_heap` 的最大值，则将新数加入 `max_heap`。
   - 否则，将新数加入 `min_heap`。
   - 平衡两个堆的大小，确保 `max_heap` 的大小始终不小于 `min_heap` 的大小，并且最多相差 1。
3. 在 `findMedian` 方法中：
   - 如果 `max_heap` 和 `min_heap` 的大小相等，则中位数为两个堆顶元素的平均值。
   - 否则，中位数为 `max_heap` 的堆顶元素。

关键点:
- 使用两个堆来分别存储较小和较大的一半数据。
- 通过平衡两个堆的大小来确保中位数的计算正确。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 每次插入和查找中位数的时间复杂度都是 O(log n)，其中 n 是当前数据流的长度。
空间复杂度: O(n) - 需要存储所有的数据流元素。
"""

# ============================================================================
# 代码实现
# ============================================================================

from heapq import heappush, heappop, heapify

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # 存储较小的一半数据
        self.min_heap = []  # 存储较大的一半数据

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        
        # 平衡两个堆的大小
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]

# 示例测试
if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # 输出: 1.5
    mf.addNum(3)
    print(mf.findMedian())  # 输出: 2.0