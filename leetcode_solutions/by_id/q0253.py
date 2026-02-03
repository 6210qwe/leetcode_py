# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 253
标题: Meeting Rooms II
难度: medium
链接: https://leetcode.cn/problems/meeting-rooms-ii/
题目类型: 贪心、数组、双指针、前缀和、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
253. 会议室 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用最小堆，维护当前正在进行的会议结束时间

算法步骤:
1. 按开始时间排序会议
2. 使用最小堆存储当前会议的结束时间
3. 如果新会议开始时间>=堆顶结束时间，可以复用会议室
4. 否则需要新会议室

关键点:
- 最小堆维护结束时间
- 时间复杂度O(n log n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n) - 排序和堆操作
空间复杂度: O(n) - 堆空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import heapq
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    函数式接口 - 会议室 II
    
    实现思路:
    使用最小堆维护当前会议的结束时间。
    
    Args:
        intervals: 会议时间区间数组
        
    Returns:
        最少需要的会议室数量
        
    Example:
        >>> min_meeting_rooms([[0,30],[5,10],[15,20]])
        2
    """
    if not intervals:
        return 0
    
    # 按开始时间排序
    intervals.sort(key=lambda x: x[0])
    
    # 最小堆存储结束时间
    heap = []
    heapq.heappush(heap, intervals[0][1])
    
    for i in range(1, len(intervals)):
        # 如果当前会议开始时间>=最早结束时间，可以复用会议室
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, intervals[i][1])
    
    return len(heap)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(min_meeting_rooms)
