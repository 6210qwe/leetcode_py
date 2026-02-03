# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 57
标题: Insert Interval
难度: medium
链接: https://leetcode.cn/problems/insert-interval/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
57. 插入区间 - 给你一个 无重叠的 ，按照区间起始端点排序的区间列表 intervals，其中 intervals[i] = [starti, endi] 表示第 i 个区间的开始和结束，并且 intervals 按照 starti 升序排列。同样给定一个区间 newInterval = [start, end] 表示另一个区间的开始和结束。 在 intervals 中插入区间 newInterval，使得 intervals 依然按照 starti 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。 返回插入之后的 intervals。 注意 你不需要原地修改 intervals。你可以创建一个新数组然后返回它。 示例 1： 输入：intervals = [[1,3],[6,9]], newInterval = [2,5] 输出：[[1,5],[6,9]] 示例 2： 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8] 输出：[[1,2],[3,10],[12,16]] 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。 提示： * 0 <= intervals.length <= 104 * intervals[i].length == 2 * 0 <= starti <= endi <= 105 * intervals 根据 starti 按 升序 排列 * newInterval.length == 2 * 0 <= start <= end <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 分三段处理：插入前的不重叠区间、需要合并的区间、插入后的不重叠区间

算法步骤:
1. 找到插入位置：遍历intervals，找到所有与newInterval重叠的区间
2. 合并重叠区间：将newInterval与所有重叠区间合并
3. 构建结果：插入前的不重叠区间 + 合并后的区间 + 插入后的不重叠区间

关键点:
- 判断重叠：interval[0] <= newInterval[1] and interval[1] >= newInterval[0]
- 合并：取所有重叠区间的最小起始和最大结束
- 由于intervals已排序，可以一次遍历完成
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 只需一次遍历
空间复杂度: O(n) - 存储结果区间列表
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """
    函数式接口 - 分三段处理
    
    实现思路:
    找到与newInterval重叠的区间，合并它们，然后构建结果列表。
    
    Args:
        intervals: 无重叠的、按起始端点排序的区间列表
        new_interval: 要插入的新区间[start, end]
        
    Returns:
        插入并合并后的区间列表
        
    Example:
        >>> insert([[1,3],[6,9]], [2,5])
        [[1, 5], [6, 9]]
    """
    result = []
    i = 0
    n = len(intervals)
    
    # 添加所有在newInterval之前的区间
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    # 合并所有与newInterval重叠的区间
    merged = new_interval[:]
    while i < n and intervals[i][0] <= merged[1]:
        merged[0] = min(merged[0], intervals[i][0])
        merged[1] = max(merged[1], intervals[i][1])
        i += 1
    result.append(merged)
    
    # 添加所有在newInterval之后的区间
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(insert)
