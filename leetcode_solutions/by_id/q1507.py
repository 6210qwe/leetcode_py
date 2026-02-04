# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1507
标题: Check if There is a Valid Path in a Grid
难度: medium
链接: https://leetcode.cn/problems/check-if-there-is-a-valid-path-in-a-grid/
题目类型: 深度优先搜索、广度优先搜索、并查集、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1391. 检查网格中是否存在有效路径 - 给你一个 m x n 的网格 grid。网格里的每个单元都代表一条街道。grid[i][j] 的街道可以是： * 1 表示连接左单元格和右单元格的街道。 * 2 表示连接上单元格和下单元格的街道。 * 3 表示连接左单元格和下单元格的街道。 * 4 表示连接右单元格和下单元格的街道。 * 5 表示连接左单元格和上单元格的街道。 * 6 表示连接右单元格和上单元格的街道。 [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/21/main.png] 你最开始从左上角的单元格 (0,0) 开始出发，网格中的「有效路径」是指从左上方的单元格 (0,0) 开始、一直到右下方的 (m-1,n-1) 结束的路径。该路径必须只沿着街道走。 注意：你 不能 变更街道。 如果网格中存在有效的路径，则返回 true，否则返回 false 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/21/e1.png] 输入：grid = [[2,4,3],[6,5,2]] 输出：true 解释：如图所示，你可以从 (0, 0) 开始，访问网格中的所有单元格并到达 (m - 1, n - 1) 。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/21/e2.png] 输入：grid = [[1,2,1],[1,2,1]] 输出：false 解释：如图所示，单元格 (0, 0) 上的街道没有与任何其他单元格上的街道相连，你只会停在 (0, 0) 处。 示例 3： 输入：grid = [[1,1,2]] 输出：false 解释：你会停在 (0, 1)，而且无法到达 (0, 2) 。 示例 4： 输入：grid = [[1,1,1,1,1,1,3]] 输出：true 示例 5： 输入：grid = [[2],[2],[2],[2],[2],[2],[6]] 输出：true 提示： * m == grid.length * n == grid[i].length * 1 <= m, n <= 300 * 1 <= grid[i][j] <= 6
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）来检查从起点到终点是否存在有效路径。

算法步骤:
1. 定义方向数组 `directions` 来表示每个街道类型的连通方向。
2. 使用递归 DFS 函数来遍历网格，标记已访问的单元格以避免重复访问。
3. 从起点 (0, 0) 开始进行 DFS，如果能到达终点 (m-1, n-1)，则返回 True；否则返回 False。

关键点:
- 使用方向数组来简化方向判断。
- 递归 DFS 函数来遍历网格，并使用集合 `visited` 来记录已访问的单元格。
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

def has_valid_path(grid: List[List[int]]) -> bool:
    if not grid or not grid[0]:
        return False

    m, n = len(grid), len(grid[0])
    directions = {
        1: [(0, -1), (0, 1)],
        2: [(-1, 0), (1, 0)],
        3: [(0, -1), (1, 0)],
        4: [(0, 1), (1, 0)],
        5: [(0, -1), (-1, 0)],
        6: [(0, 1), (-1, 0)]
    }

    def dfs(x: int, y: int, visited: set) -> bool:
        if (x, y) == (m - 1, n - 1):
            return True
        visited.add((x, y))
        for dx, dy in directions[grid[x][y]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                for ddx, ddy in directions[grid[nx][ny]]:
                    if (nx + ddx, ny + ddy) == (x, y):
                        if dfs(nx, ny, visited):
                            return True
        return False

    return dfs(0, 0, set())

Solution = create_solution(has_valid_path)