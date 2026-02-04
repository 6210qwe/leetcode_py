# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2454
标题: Largest Local Values in a Matrix
难度: easy
链接: https://leetcode.cn/problems/largest-local-values-in-a-matrix/
题目类型: 数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2373. 矩阵中的局部最大值 - 给你一个大小为 n x n 的整数矩阵 grid 。 生成一个大小为 (n - 2) x (n - 2) 的整数矩阵 maxLocal ，并满足： * maxLocal[i][j] 等于 grid 中以 i + 1 行和 j + 1 列为中心的 3 x 3 矩阵中的 最大值 。 换句话说，我们希望找出 grid 中每个 3 x 3 矩阵中的最大值。 返回生成的矩阵。 示例 1： [https://assets.leetcode.com/uploads/2022/06/21/ex1.png] 输入：grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]] 输出：[[9,9],[8,6]] 解释：原矩阵和生成的矩阵如上图所示。 注意，生成的矩阵中，每个值都对应 grid 中一个相接的 3 x 3 矩阵的最大值。 示例 2： [https://assets.leetcode.com/uploads/2022/07/02/ex2new2.png] 输入：grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]] 输出：[[2,2,2],[2,2,2],[2,2,2]] 解释：注意，2 包含在 grid 中每个 3 x 3 的矩阵中。 提示： * n == grid.length == grid[i].length * 3 <= n <= 100 * 1 <= grid[i][j] <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口技术遍历矩阵，找到每个 3x3 子矩阵的最大值。

算法步骤:
1. 初始化一个 (n-2) x (n-2) 的结果矩阵 `maxLocal`。
2. 遍历矩阵 `grid`，对于每个 3x3 子矩阵，找到其最大值并存储在 `maxLocal` 中。

关键点:
- 使用嵌套循环遍历矩阵，确保每个 3x3 子矩阵都被处理。
- 通过滑动窗口技术减少重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)
空间复杂度: O((n-2)^2)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(grid: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 找到矩阵中每个 3x3 子矩阵的最大值
    """
    n = len(grid)
    maxLocal = [[0] * (n - 2) for _ in range(n - 2)]
    
    for i in range(n - 2):
        for j in range(n - 2):
            max_value = 0
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    max_value = max(max_value, grid[x][y])
            maxLocal[i][j] = max_value
    
    return maxLocal


Solution = create_solution(solution_function_name)