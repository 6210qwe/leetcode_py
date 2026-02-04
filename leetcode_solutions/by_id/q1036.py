# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1036
标题: Rotting Oranges
难度: medium
链接: https://leetcode.cn/problems/rotting-oranges/
题目类型: 广度优先搜索、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
994. 腐烂的橘子 - 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一： * 值 0 代表空单元格； * 值 1 代表新鲜橘子； * 值 2 代表腐烂的橘子。 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/02/16/oranges.png] 输入：grid = [[2,1,1],[1,1,0],[0,1,1]] 输出：4 示例 2： 输入：grid = [[2,1,1],[0,1,1],[1,0,1]] 输出：-1 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。 示例 3： 输入：grid = [[0,2]] 输出：0 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。 提示： * m == grid.length * n == grid[i].length * 1 <= m, n <= 10 * grid[i][j] 仅为 0、1 或 2
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来模拟腐烂过程。

算法步骤:
1. 初始化队列，将所有腐烂的橘子加入队列，并记录初始时间。
2. 使用 BFS 进行层次遍历，每层遍历完后时间加一。
3. 对于每个腐烂的橘子，检查其四个方向上的邻居，如果邻居是新鲜橘子，则将其标记为腐烂并加入队列。
4. 如果队列为空且仍有新鲜橘子，则返回 -1，否则返回总时间。

关键点:
- 使用队列进行 BFS。
- 记录时间和新鲜橘子的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是网格的行数和列数。
空间复杂度: O(m * n)，最坏情况下队列中可能包含所有的橘子。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def oranges_rotting(grid: List[List[int]]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    queue = []
    fresh_count = 0

    # 初始化队列并将所有腐烂的橘子加入队列
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_count += 1

    # 如果没有新鲜橘子，直接返回 0
    if fresh_count == 0:
        return 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    minutes_passed = 0

    while queue and fresh_count > 0:
        minutes_passed += 1
        new_queue = []

        for r, c in queue:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    new_queue.append((nr, nc))

        queue = new_queue

    return minutes_passed if fresh_count == 0 else -1


Solution = create_solution(oranges_rotting)