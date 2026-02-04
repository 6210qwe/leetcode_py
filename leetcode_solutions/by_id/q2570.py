# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2570
标题: Maximize Total Tastiness of Purchased Fruits
难度: medium
链接: https://leetcode.cn/problems/maximize-total-tastiness-of-purchased-fruits/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2431. 最大限度地提高购买水果的口味 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义一个二维数组 dp，其中 dp[i][j] 表示前 i 种水果中选择 j 个水果的最大总口味。

算法步骤:
1. 初始化一个 (n+1) x (m+1) 的二维数组 dp，所有元素初始化为 0。
2. 遍历每种水果 i 和每个可能的选择数量 j。
3. 对于每种水果 i 和每个选择数量 j，有两种情况：
   - 不选择第 i 种水果：dp[i][j] = dp[i-1][j]
   - 选择第 i 种水果：dp[i][j] = max(dp[i][j], dp[i-1][j-k] + k * tastiness[i-1])，其中 k 是选择的数量，且 1 <= k <= min(j, quantity[i-1])

关键点:
- 动态规划的状态转移方程
- 选择和不选择当前水果的两种情况
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m^2)，其中 n 是水果种类数，m 是最大选择数量。
空间复杂度: O(n * m)，用于存储动态规划数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(tastiness: List[int], quantity: List[int], maxAmount: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    n = len(tastiness)
    m = maxAmount
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 不选择第 i 种水果
            dp[i][j] = dp[i - 1][j]
            # 选择第 i 种水果
            for k in range(1, min(j, quantity[i - 1]) + 1):
                if j - k >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - k] + k * tastiness[i - 1])

    return dp[n][m]


Solution = create_solution(solution_function_name)