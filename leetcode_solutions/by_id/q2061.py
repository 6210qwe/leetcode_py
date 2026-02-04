# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2061
标题: Painting a Grid With Three Different Colors
难度: hard
链接: https://leetcode.cn/problems/painting-a-grid-with-three-different-colors/
题目类型: 动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1931. 用三种不同颜色为网格涂色 - 给你两个整数 m 和 n 。构造一个 m x n 的网格，其中每个单元格最开始是白色。请你用 红、绿、蓝 三种颜色为每个单元格涂色。所有单元格都需要被涂色。 涂色方案需要满足：不存在相邻两个单元格颜色相同的情况 。返回网格涂色的方法数。因为答案可能非常大， 返回 对 109 + 7 取余 的结果。 示例 1： [https://assets.leetcode.com/uploads/2021/06/22/colorthegrid.png] 输入：m = 1, n = 1 输出：3 解释：如上图所示，存在三种可能的涂色方案。 示例 2： [https://assets.leetcode.com/uploads/2021/06/22/copy-of-colorthegrid.png] 输入：m = 1, n = 2 输出：6 解释：如上图所示，存在六种可能的涂色方案。 示例 3： 输入：m = 5, n = 5 输出：580986 提示： * 1 <= m <= 5 * 1 <= n <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义一个状态 `dp[i][mask]` 表示前 `i` 列的涂色方案，并且第 `i` 列的颜色配置为 `mask`。`mask` 是一个二进制数，每一位表示一个颜色（0, 1, 2），并且相邻两位不能相同。

算法步骤:
1. 初始化 `dp[0][mask]` 为 1，表示第一列的初始状态。
2. 对于每一列 `i`，遍历所有可能的 `mask`，并检查与前一列的 `mask` 是否合法。
3. 更新 `dp[i][mask]` 为所有合法前一列 `mask` 的和。
4. 最终结果是 `dp[n-1]` 中所有状态的和。

关键点:
- 使用位运算来表示和处理颜色配置。
- 通过预处理合法的 `mask` 来优化状态转移。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(3^m * n)
空间复杂度: O(3^m * n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

MOD = 10**9 + 7

def solution_function_name(m: int, n: int) -> int:
    """
    函数式接口 - 计算 m x n 网格的涂色方案数
    """
    # 生成所有合法的 mask
    valid_masks = []
    for mask in range(3 ** m):
        colors = [mask // (3 ** i) % 3 for i in range(m)]
        if all(colors[i] != colors[i + 1] for i in range(m - 1)):
            valid_masks.append(mask)

    # 初始化 dp 数组
    dp = [[0] * (3 ** m) for _ in range(n)]
    for mask in valid_masks:
        dp[0][mask] = 1

    # 动态规划计算
    for i in range(1, n):
        for mask in valid_masks:
            colors = [mask // (3 ** j) % 3 for j in range(m)]
            for prev_mask in valid_masks:
                prev_colors = [prev_mask // (3 ** j) % 3 for j in range(m)]
                if all(colors[j] != prev_colors[j] for j in range(m)):
                    dp[i][mask] = (dp[i][mask] + dp[i - 1][prev_mask]) % MOD

    # 返回最终结果
    return sum(dp[n - 1]) % MOD

Solution = create_solution(solution_function_name)