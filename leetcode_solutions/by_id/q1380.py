# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1380
标题: Number of Closed Islands
难度: medium
链接: https://leetcode.cn/problems/number-of-closed-islands/
题目类型: 深度优先搜索、广度优先搜索、并查集、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1254. 统计封闭岛屿的数目 - 二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。 请返回 封闭岛屿 的数目。 示例 1： [https://assets.leetcode.com/uploads/2019/10/31/sample_3_1610.png] 输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]] 输出：2 解释： 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/11/07/sample_4_1610.png] 输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]] 输出：1 示例 3： 输入：grid = [[1,1,1,1,1,1,1], [1,0,0,0,0,0,1], [1,0,1,1,1,0,1], [1,0,1,0,1,0,1], [1,0,1,1,1,0,1], [1,0,0,0,0,0,1], [1,1,1,1,1,1,1]] 输出：2 提示： * 1 <= grid.length, grid[0].length <= 100 * 0 <= grid[i][j] <=1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来遍历每个岛屿，并标记已访问的土地。如果一个岛屿在边界上，则它不是封闭岛屿。

算法步骤:
1. 遍历整个网格，找到所有未访问的土地。
2. 对于每个未访问的土地，使用 DFS 进行遍历，并标记所有连通的土地。
3. 如果在遍历过程中遇到边界，则该岛屿不是封闭岛屿。
4. 统计所有封闭岛屿的数量。

关键点:
- 使用 DFS 标记已访问的土地。
- 在遍历过程中检查是否遇到边界。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 是网格的行数，n 是网格的列数。每个格子最多只会被访问一次。
空间复杂度: O(m * n)，递归调用栈的深度最多为 m * n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def num_closed_islands(grid: List[List[int]]) -> int:
    """
    函数式接口 - 统计封闭岛屿的数目
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r: int, c: int) -> bool:
        if (r, c) in visited or grid[r][c] == 1:
            return True
        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            return False

        visited.add((r, c))
        is_closed = True
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if not dfs(nr, nc):
                is_closed = False

        return is_closed

    closed_islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and (r, c) not in visited and dfs(r, c):
                closed_islands += 1

    return closed_islands


Solution = create_solution(num_closed_islands)