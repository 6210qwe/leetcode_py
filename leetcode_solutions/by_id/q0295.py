# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 295
标题: Find Median from Data Stream
难度: hard
链接: https://leetcode.cn/problems/find-median-from-data-stream/
题目类型: 设计、双指针、数据流、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
295. 数据流的中位数 - 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。 * 例如 arr = [2,3,4] 的中位数是 3 。 * 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。 实现 MedianFinder 类: * MedianFinder() 初始化 MedianFinder 对象。 * void addNum(int num) 将数据流中的整数 num 添加到数据结构中。 * double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。 示例 1： 输入 ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"] [[], [1], [2], [], [3], []] 输出 [null, null, null, 1.5, null, 2.0] 解释 MedianFinder medianFinder = new MedianFinder(); medianFinder.addNum(1); // arr = [1] medianFinder.addNum(2); // arr = [1, 2] medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2) medianFinder.addNum(3); // arr[1, 2, 3] medianFinder.findMedian(); // return 2.0 提示: * -105 <= num <= 105 * 在调用 findMedian 之前，数据结构中至少有一个元素 * 最多 5 * 104 次调用 addNum 和 findMedian
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个堆，一个大顶堆存储较小的一半，一个小顶堆存储较大的一半

算法步骤:
1. 使用max_heap存储较小的一半（大顶堆）
2. 使用min_heap存储较大的一半（小顶堆）
3. 保持两个堆的大小平衡（最多相差1）
4. 中位数：如果大小相等，取两个堆顶的平均值；否则取较大堆的堆顶

关键点:
- 使用两个堆维护中位数
- 时间复杂度O(logn)插入，O(1)查询，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(logn)插入，O(1)查询中位数
空间复杂度: O(n) - 两个堆的空间
"""

# ============================================================================
# 代码实现
# ============================================================================

import heapq
from leetcode_solutions.utils.solution import create_solution


class MedianFinder:
    """
    数据流的中位数
    """
    def __init__(self):
        self.max_heap = []  # 较小的一半（大顶堆，使用负数实现）
        self.min_heap = []  # 较大的一半（小顶堆）
    
    def addNum(self, num: int) -> None:
        """将数据流中的整数添加到数据结构中"""
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # 保持平衡
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    
    def findMedian(self) -> float:
        """返回到目前为止所有元素的中位数"""
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        elif len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return float(self.min_heap[0])


def find_median_from_data_stream() -> MedianFinder:
    """
    函数式接口 - 创建数据流中位数查找器
    
    实现思路:
    使用两个堆，一个大顶堆存储较小的一半，一个小顶堆存储较大的一半。
    
    Returns:
        MedianFinder实例
        
    Example:
        >>> finder = find_median_from_data_stream()
        >>> finder.addNum(1)
        >>> finder.addNum(2)
        >>> finder.findMedian()
        1.5
    """
    return MedianFinder()


# 自动生成Solution类（无需手动编写）
Solution = create_solution(find_median_from_data_stream)
