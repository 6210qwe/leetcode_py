# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2641
标题: Disconnect Path in a Binary Matrix by at Most One Flip
难度: medium
链接: https://leetcode.cn/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/
题目类型: 深度优先搜索、广度优先搜索、数组、动态规划、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2556. 二进制矩阵中翻转最多一次使路径不连通 - 给你一个下标从 0 开始的 m x n 二进制 矩阵 grid 。你可以从一个格子 (row, col) 移动到格子 (row + 1, col) 或者 (row, col + 1) ，前提是前往的格子值为 1 。如果从 (0, 0) 到 (m - 1, n - 1) 没有任何路径，我们称该矩阵是 不连通 的。 你可以翻转 最多一个 格子的值（也可以不翻转）。你 不能翻转 格子 (0, 0) 和 (m - 1, n - 1) 。 如果可以使矩阵不连通，请你返回 true ，否则返回 false 。 注意 ，翻转一个格子的值，可以使它的值从 0 变 1 ，或从 1 变 0 。 示例 1： [https://assets.leetcode.com/uploads/2022/12/07/yetgrid2drawio.png] 输入：grid = [[1,1,1],[1,0,0],[1,1,1]] 输出：true 解释：按照上图所示我们翻转蓝色格子里的值，翻转后从 (0, 0) 到 (2, 2) 没有路径。 示例 2： [https://assets.leetcode.com/uploads/2022/12/07/yetgrid3drawio.png] 输入：grid = [[1,1,1],[1,0,1],[1,1,1]] 输出：false 解释：无法翻转至多一个格子，使 (0, 0) 到 (2, 2) 没有路径。 提示： * m == grid.length * n == grid[i].length * 1 <= m, n <= 1000 * 1 <= m * n <= 105 * grid[0][0] == grid[m - 1][n - 1] == 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来找到从 (0, 0) 到 (m-1, n-1) 的所有路径，并记录每个格子在这些路径中出现的次数。如果某个格子在所有路径中都出现过，则翻转该格子可以使得路径不连通。

算法步骤:
1. 使用 DFS 找到从 (0, 0) 到 (m-1, n-1) 的所有路径，并记录每个格子在这些路径中出现的次数。
2. 检查是否有某个格子在所有路径中都出现过，如果有则返回 True，否则返回 False。

关键点:
- 使用一个二维数组 `path_count` 来记录每个格子在路径中出现的次数。
- 通过 DFS 递归地遍历所有可能的路径。
- 如果某个格子在所有路径中都出现过，则翻转该格子可以使得路径不连通。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是矩阵的行数和列数。每个格子最多被访问一次。
空间复杂度: O(m * n)，用于存储路径计数和递归调用栈。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def is_possible_to_cut_path(grid: List[List[int]]) -> bool:
    m, n = len(grid), len(grid[0])
    path_count = [[0] * n for _ in range(m)]
    
    def dfs(x: int, y: int) -> bool:
        if x == m - 1 and y == n - 1:
            path_count[x][y] += 1
            return True
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
            return False
        grid[x][y] = 0  # Mark as visited
        if dfs(x + 1, y) or dfs(x, y + 1):
            path_count[x][y] += 1
        grid[x][y] = 1  # Unmark
        return path_count[x][y] > 0
    
    if not dfs(0, 0):
        return True  # No path from (0, 0) to (m-1, n-1)
    
    grid[0][0] = 1  # Unmark the start point
    if not dfs(0, 0):
        return True  # No path after unmarking the start point
    
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if path_count[i][j] == 2:
                return True  # Found a critical cell
    
    return False

Solution = create_solution(is_possible_to_cut_path)