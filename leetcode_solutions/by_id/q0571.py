# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 571
标题: Find Median Given Frequency of Numbers
难度: hard
链接: https://leetcode.cn/problems/find-median-given-frequency-of-numbers/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
571. 给定数字的频率查询中位数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个堆来维护前半部分和后半部分的元素，使得中位数可以在 O(1) 时间内获取。

算法步骤:
1. 初始化两个堆：一个最大堆（维护较小的一半元素）和一个最小堆（维护较大的一半元素）。
2. 遍历输入数组，将每个元素按频率插入到相应的堆中。
3. 保持两个堆的平衡，确保最大堆的大小不超过最小堆的大小加一。
4. 根据两个堆的大小关系，返回中位数。

关键点:
- 使用两个堆来维护元素，确保中位数可以在 O(1) 时间内获取。
- 保持两个堆的平衡，确保最大堆的大小不超过最小堆的大小加一。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是输入数组的长度。每次插入堆的操作是 O(log n)。
空间复杂度: O(n)，需要存储所有元素。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import heapq

def find_median(nums: List[int], freq: List[int]) -> float:
    """
    给定数字的频率查询中位数
    :param nums: 数字列表
    :param freq: 每个数字对应的频率
    :return: 中位数
    """
    max_heap = []  # 最大堆，存储较小的一半元素
    min_heap = []  # 最小堆，存储较大的一半元素
    
    for num, f in zip(nums, freq):
        for _ in range(f):
            if not max_heap or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)
        
        # 保持两个堆的平衡
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
    
    # 返回中位数
    if len(max_heap) == len(min_heap):
        return (-max_heap[0] + min_heap[0]) / 2
    else:
        return -max_heap[0]

Solution = create_solution(find_median)