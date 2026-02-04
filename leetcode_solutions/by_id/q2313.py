# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2313
标题: Longest Winning Streak
难度: hard
链接: https://leetcode.cn/problems/longest-winning-streak/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2173. 最多连胜的次数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算最长的连胜次数。

算法步骤:
1. 创建一个临时表，记录每个用户的每次比赛结果。
2. 使用窗口函数计算每个用户的连胜次数。
3. 找出每个用户最长的连胜次数。

关键点:
- 使用窗口函数 `ROW_NUMBER()` 和 `LAG()` 来计算连胜次数。
- 使用 `MAX()` 函数找到最长的连胜次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def solution_function_name(matches: List[List[int]]) -> int:
    """
    函数式接口 - 计算最长的连胜次数
    """
    # 创建一个字典来存储每个用户的比赛结果
    user_results = {}
    for match in matches:
        user_id, result = match
        if user_id not in user_results:
            user_results[user_id] = []
        user_results[user_id].append(result)
    
    max_streak = 0
    for user_id, results in user_results.items():
        current_streak = 0
        longest_streak = 0
        for result in results:
            if result == 1:
                current_streak += 1
                longest_streak = max(longest_streak, current_streak)
            else:
                current_streak = 0
        max_streak = max(max_streak, longest_streak)
    
    return max_streak

Solution = create_solution(solution_function_name)