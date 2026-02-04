# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3691
标题: Minimum Operations to Make Columns Strictly Increasing
难度: easy
链接: https://leetcode.cn/problems/minimum-operations-to-make-columns-strictly-increasing/
题目类型: 贪心、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3402. 使每一列严格递增的最少操作次数 - 给你一个由 非负 整数组成的 m x n 矩阵 grid。 在一次操作中，你可以将任意元素 grid[i][j] 的值增加 1。 返回使 grid 的所有列 严格递增 所需的 最少 操作次数。 示例 1： 输入: grid = [[3,2],[1,3],[3,4],[0,1]] 输出: 15 解释: * 为了让第 0 列严格递增，可以对 grid[1][0] 执行 3 次操作，对 grid[2][0] 执行 2 次操作，对 grid[3][0] 执行 6 次操作。 * 为了让第 1 列严格递增，可以对 grid[3][1] 执行 4 次操作。 [https://assets.leetcode.com/uploads/2024/11/10/firstexample.png] 示例 2： 输入: grid = [[3,2,1],[2,1,0],[1,2,3]] 输出: 12 解释: * 为了让第 0 列严格递增，可以对 grid[1][0] 执行 2 次操作，对 grid[2][0] 执行 4 次操作。 * 为了让第 1 列严格递增，可以对 grid[1][1] 执行 2 次操作，对 grid[2][1] 执行 2 次操作。 * 为了让第 2 列严格递增，可以对 grid[1][2] 执行 2 次操作。 [https://assets.leetcode.com/uploads/2024/11/10/secondexample.png] 提示: * m == grid.length * n == grid[i].length * 1 <= m, n <= 50 * 0 <= grid[i][j] < 2500
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法逐列处理，确保每列的每个元素都大于前一个元素。

算法步骤:
1. 初始化操作次数为 0。
2. 遍历每一列，对于每一列中的每个元素，如果当前元素不大于前一个元素，则计算需要的操作次数，并更新当前元素。
3. 返回总的操作次数。

关键点:
- 逐列处理，确保每列的每个元素都大于前一个元素。
- 使用贪心算法，每次只做必要的操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 是矩阵的行数，n 是矩阵的列数。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_operations_to_make_columns_strictly_increasing(grid: List[List[int]]) -> int:
    """
    函数式接口 - 计算使每一列严格递增的最少操作次数
    """
    m, n = len(grid), len(grid[0])
    operations = 0

    for j in range(n):
        for i in range(1, m):
            if grid[i][j] <= grid[i - 1][j]:
                needed_operations = grid[i - 1][j] - grid[i][j] + 1
                operations += needed_operations
                grid[i][j] += needed_operations

    return operations


Solution = create_solution(min_operations_to_make_columns_strictly_increasing)