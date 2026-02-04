# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2672
标题: Number of Good Binary Strings
难度: medium
链接: https://leetcode.cn/problems/number-of-good-binary-strings/
题目类型: 动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定三个整数 low, high 和 zero，返回 [low, high] 范围内的好二进制字符串的数量。好二进制字符串定义为：长度在 [low, high] 范围内，且包含的 '0' 的数量不超过 zero。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来计算满足条件的二进制字符串数量。

算法步骤:
1. 初始化一个二维数组 dp，其中 dp[i][j] 表示长度为 i 且包含 j 个 '0' 的好二进制字符串的数量。
2. 初始化 dp[0][0] = 1，表示空字符串。
3. 遍历所有可能的字符串长度 i 从 1 到 high。
4. 对于每个长度 i，遍历所有可能的 '0' 的数量 j 从 0 到 min(i, zero)。
5. 更新 dp[i][j] 为 dp[i-1][j] + dp[i-1][j-1]，分别表示在长度为 i-1 的字符串末尾添加 '1' 或 '0'。
6. 最后，累加 dp[i][j] 从 low 到 high 的所有值，得到结果。

关键点:
- 使用动态规划避免重复计算。
- 确保 '0' 的数量不超过 zero。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(high * zero)
空间复杂度: O(high * zero)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(low: int, high: int, zero: int) -> int:
    """
    函数式接口 - 计算 [low, high] 范围内的好二进制字符串的数量
    """
    # 初始化 dp 数组
    dp = [[0] * (zero + 1) for _ in range(high + 1)]
    dp[0][0] = 1  # 空字符串

    # 动态规划计算
    for i in range(1, high + 1):
        for j in range(min(i, zero) + 1):
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]  # 在末尾添加 '0'
            dp[i][j] += dp[i - 1][j]  # 在末尾添加 '1'

    # 累加结果
    result = sum(dp[i][j] for i in range(low, high + 1) for j in range(zero + 1))
    return result


Solution = create_solution(solution_function_name)