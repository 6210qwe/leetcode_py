# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1979
标题: Maximum Number of People That Can Be Caught in Tag
难度: medium
链接: https://leetcode.cn/problems/maximum-number-of-people-that-can-be-caught-in-tag/
题目类型: 贪心、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1989. 捉迷藏中可捕获的最大人数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，优先选择能捕获最多人的区间。

算法步骤:
1. 将所有区间按结束时间从小到大排序。
2. 初始化一个变量 `max_people` 来记录最大捕获人数，初始化一个变量 `end_time` 来记录当前最晚的结束时间。
3. 遍历排序后的区间：
   - 如果当前区间的开始时间大于 `end_time`，则更新 `end_time` 为当前区间的结束时间，并增加 `max_people`。
4. 返回 `max_people`。

关键点:
- 通过按结束时间排序，确保每次选择的区间都是当前最优的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是区间的数量。排序操作的时间复杂度为 O(n log n)，遍历操作的时间复杂度为 O(n)。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_people_caught(intervals: List[List[int]]) -> int:
    """
    函数式接口 - 计算最大可捕获的人数
    """
    # 按结束时间从小到大排序
    intervals.sort(key=lambda x: x[1])
    
    max_people = 0
    end_time = float('-inf')
    
    for interval in intervals:
        start, end = interval
        if start > end_time:
            end_time = end
            max_people += 1
    
    return max_people


Solution = create_solution(max_people_caught)