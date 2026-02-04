# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 568
标题: Maximum Vacation Days
难度: hard
链接: https://leetcode.cn/problems/maximum-vacation-days/
题目类型: 数组、动态规划、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
568. 最大休假天数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义一个二维数组 dp，其中 dp[i][j] 表示在第 i 周选择城市 j 的最大休假天数。

算法步骤:
1. 初始化 dp 数组，dp[0][i] 表示第一周选择城市 i 的休假天数。
2. 从第二周开始，对于每一周的每一个城市，计算从上一周的所有城市转移过来的最大休假天数。
3. 最后，返回 dp 数组最后一行的最大值。

关键点:
- 动态规划的状态转移方程为：dp[i][j] = max(dp[i-1][k] + flights[k][j]) + days[i][j]，其中 k 是上一周的城市。
- 需要处理不能直接从城市 k 转移到城市 j 的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m^2)，其中 n 是周数，m 是城市的数量。
空间复杂度: O(n * m)，存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(flights: List[List[int]], days: List[List[int]]) -> int:
    """
    函数式接口 - 计算最大休假天数
    """
    n = len(days)
    m = len(flights)
    
    # 初始化 dp 数组
    dp = [[float('-inf')] * m for _ in range(n)]
    dp[0] = [days[0][i] if flights[0][i] == 1 or i == 0 else float('-inf') for i in range(m)]
    
    # 动态规划填表
    for week in range(1, n):
        for city in range(m):
            for prev_city in range(m):
                if flights[prev_city][city] == 1 or (prev_city == city and flights[prev_city][city] == 0):
                    dp[week][city] = max(dp[week][city], dp[week - 1][prev_city] + days[week][city])
    
    # 返回最大休假天数
    return max(dp[-1])


Solution = create_solution(solution_function_name)