# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3391
标题: Maximum Difference Score in a Grid
难度: medium
链接: https://leetcode.cn/problems/maximum-difference-score-in-a-grid/
题目类型: 数组、动态规划、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3148. 矩阵中的最大得分 - 给你一个由 正整数 组成、大小为 m x n 的矩阵 grid。你可以从矩阵中的任一单元格移动到另一个位于正下方或正右侧的任意单元格（不必相邻）。从值为 c1 的单元格移动到值为 c2 的单元格的得分为 c2 - c1 。 你可以从 任一 单元格开始，并且必须至少移动一次。 返回你能得到的 最大 总得分。 示例 1： [https://assets.leetcode.com/uploads/2024/03/14/grid1.png] 输入：grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]] 输出：9 解释：从单元格 (0, 1) 开始，并执行以下移动： - 从单元格 (0, 1) 移动到 (2, 1)，得分为 7 - 5 = 2 。 - 从单元格 (2, 1) 移动到 (2, 2)，得分为 14 - 7 = 7 。 总得分为 2 + 7 = 9 。 示例 2： [https://assets.leetcode.com/uploads/2024/04/08/moregridsdrawio-1.png] 输入：grid = [[4,3,2],[3,2,1]] 输出：-1 解释：从单元格 (0, 0) 开始，执行一次移动：从 (0, 0) 到 (0, 1) 。得分为 3 - 4 = -1 。 提示： * m == grid.length * n == grid[i].length * 2 <= m, n <= 1000 * 4 <= m * n <= 105 * 1 <= grid[i][j] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来计算每个单元格的最大得分。

算法步骤:
1. 初始化两个数组 `max_right` 和 `max_down`，分别记录每个单元格向右和向下移动的最大得分。
2. 从右下角开始，逆向遍历矩阵，更新 `max_right` 和 `max_down`。
3. 计算每个单元格的最大得分，取 `max_right` 和 `max_down` 中的最大值。
4. 返回最大得分。

关键点:
- 逆向遍历矩阵，确保每个单元格在计算时已经知道其右侧和下方的最大得分。
- 使用两个辅助数组来存储中间结果，避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)
空间复杂度: O(m * n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_difference_score(grid: List[List[int]]) -> int:
    """
    函数式接口 - 计算矩阵中的最大得分
    """
    m, n = len(grid), len(grid[0])
    
    # 初始化两个辅助数组
    max_right = [[0] * n for _ in range(m)]
    max_down = [[0] * n for _ in range(m)]
    
    # 从右下角开始逆向遍历矩阵
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i < m - 1:
                max_down[i][j] = max(max_down[i + 1][j], grid[i + 1][j] - grid[i][j])
            if j < n - 1:
                max_right[i][j] = max(max_right[i][j + 1], grid[i][j + 1] - grid[i][j])
    
    # 计算每个单元格的最大得分
    max_score = float('-inf')
    for i in range(m):
        for j in range(n):
            max_score = max(max_score, max(max_right[i][j], max_down[i][j]))
    
    return max_score


Solution = create_solution(max_difference_score)