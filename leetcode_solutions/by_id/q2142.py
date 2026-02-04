# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2142
标题: Average Height of Buildings in Each Segment
难度: medium
链接: https://leetcode.cn/problems/average-height-of-buildings-in-each-segment/
题目类型: 贪心、数组、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2015. 每段建筑物的平均高度 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用扫描线算法来处理每个建筑物的开始和结束位置，并计算每个区间的平均高度。

算法步骤:
1. 将每个建筑物的开始和结束位置分别存储在两个列表中。
2. 对这两个列表进行排序。
3. 使用一个计数器来记录当前区间内的建筑物数量和总高度。
4. 遍历排序后的列表，更新计数器并在每个区间的结束位置计算平均高度。
5. 将结果存储在一个列表中并返回。

关键点:
- 使用扫描线算法可以有效地处理区间重叠问题。
- 通过排序和遍历，可以确保每个区间的平均高度计算是正确的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 buildings 的长度。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，需要额外的空间来存储开始和结束位置。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def solution_function_name(buildings: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 计算每段建筑物的平均高度
    """
    events = []
    for start, end, height in buildings:
        events.append((start, height, 1))  # 建筑物开始
        events.append((end, height, -1))   # 建筑物结束
    
    events.sort()
    
    result = []
    current_height_sum = 0
    current_count = 0
    prev_position = None
    
    for position, height, event_type in events:
        if current_count > 0 and prev_position is not None and position != prev_position:
            result.append([prev_position, position, current_height_sum // current_count])
        
        current_height_sum += height * event_type
        current_count += event_type
        
        prev_position = position
    
    return result

Solution = create_solution(solution_function_name)