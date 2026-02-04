# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2067
标题: Maximum Number of Points with Cost
难度: medium
链接: https://leetcode.cn/problems/maximum-number-of-points-with-cost/
题目类型: 数组、动态规划、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1937. 扣分后的最大得分 - 给你一个 m x n 的整数矩阵 points （下标从 0 开始）。一开始你的得分为 0 ，你想最大化从矩阵中得到的分数。 你的得分方式为：每一行 中选取一个格子，选中坐标为 (r, c) 的格子会给你的总得分 增加 points[r][c] 。 然而，相邻行之间被选中的格子如果隔得太远，你会失去一些得分。对于相邻行 r 和 r + 1 （其中 0 <= r < m - 1），选中坐标为 (r, c1) 和 (r + 1, c2) 的格子，你的总得分 减少 abs(c1 - c2) 。 请你返回你能得到的 最大 得分。 abs(x) 定义为： * 如果 x >= 0 ，那么值为 x 。 * 如果 x < 0 ，那么值为 -x 。 示例 1： [https://assets.leetcode.com/uploads/2021/07/12/screenshot-2021-07-12-at-13-40-26-diagram-drawio-diagrams-net.png] 输入：points = [[1,2,3],[1,5,1],[3,1,1]] 输出：9 解释： 蓝色格子是最优方案选中的格子，坐标分别为 (0, 2)，(1, 1) 和 (2, 0) 。 你的总得分增加 3 + 5 + 3 = 11 。 但是你的总得分需要扣除 abs(2 - 1) + abs(1 - 0) = 2 。 你的最终得分为 11 - 2 = 9 。 示例 2： [https://assets.leetcode.com/uploads/2021/07/12/screenshot-2021-07-12-at-13-42-14-diagram-drawio-diagrams-net.png] 输入：points = [[1,5],[2,3],[4,2]] 输出：11 解释： 蓝色格子是最优方案选中的格子，坐标分别为 (0, 1)，(1, 1) 和 (2, 0) 。 你的总得分增加 5 + 3 + 4 = 12 。 但是你的总得分需要扣除 abs(1 - 1) + abs(1 - 0) = 1 。 你的最终得分为 12 - 1 = 11 。 提示： * m == points.length * n == points[r].length * 1 <= m, n <= 105 * 1 <= m * n <= 105 * 0 <= points[r][c] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们维护一个二维数组 dp，其中 dp[i][j] 表示到第 i 行选择第 j 列的最大得分。通过前一行的状态更新当前行的状态。

算法步骤:
1. 初始化 dp 数组，dp[0] 为 points 的第一行。
2. 对于每一行，从左到右和从右到左分别计算最大得分。
3. 更新 dp 数组，使其包含当前行的最大得分。
4. 返回 dp 数组最后一行的最大值。

关键点:
- 通过两次遍历（从左到右和从右到左）来更新 dp 数组，确保每一步都考虑了相邻列的代价。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_points_with_cost(points: List[List[int]]) -> int:
    """
    动态规划解法
    """
    if not points or not points[0]:
        return 0

    m, n = len(points), len(points[0])
    dp = points[0][:]

    for i in range(1, m):
        left_max = [0] * n
        right_max = [0] * n

        # 从左到右更新 left_max
        left_max[0] = dp[0]
        for j in range(1, n):
            left_max[j] = max(left_max[j - 1] - 1, dp[j])

        # 从右到左更新 right_max
        right_max[-1] = dp[-1]
        for j in range(n - 2, -1, -1):
            right_max[j] = max(right_max[j + 1] - 1, dp[j])

        # 更新 dp 数组
        for j in range(n):
            dp[j] = points[i][j] + max(left_max[j], right_max[j])

    return max(dp)


Solution = create_solution(max_points_with_cost)