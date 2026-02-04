# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 761
标题: Employee Free Time
难度: hard
链接: https://leetcode.cn/problems/employee-free-time/
题目类型: 数组、排序、扫描线、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
759. 员工空闲时间 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用区间合并的方法来找到所有员工的空闲时间。

算法步骤:
1. 将所有员工的时间段合并到一个列表中。
2. 对时间段按开始时间进行排序，如果开始时间相同，则按结束时间排序。
3. 合并重叠的时间段。
4. 找出合并后时间段之间的空闲时间。

关键点:
- 使用排序和合并来处理重叠的时间段。
- 通过比较相邻时间段的结束时间和开始时间来找到空闲时间。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是所有员工的时间段总数。主要开销在排序上。
空间复杂度: O(n)，需要存储所有的时间段。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

def merge_intervals(intervals: List[Interval]) -> List[Interval]:
    if not intervals:
        return []
    
    # 按开始时间排序，如果开始时间相同，则按结束时间排序
    intervals.sort(key=lambda x: (x.start, x.end))
    
    merged = [intervals[0]]
    for current in intervals[1:]:
        last_merged = merged[-1]
        if current.start <= last_merged.end:
            last_merged.end = max(last_merged.end, current.end)
        else:
            merged.append(current)
    
    return merged

def find_free_time(schedule: List[List[Interval]]) -> List[Interval]:
    all_intervals = [interval for employee in schedule for interval in employee]
    merged_intervals = merge_intervals(all_intervals)
    
    free_times = []
    for i in range(1, len(merged_intervals)):
        if merged_intervals[i].start > merged_intervals[i-1].end:
            free_times.append(Interval(merged_intervals[i-1].end, merged_intervals[i].start))
    
    return free_times

def solution_function_name(schedule: List[List[Interval]]) -> List[Interval]:
    """
    函数式接口 - 找到所有员工的空闲时间
    """
    return find_free_time(schedule)

Solution = create_solution(solution_function_name)