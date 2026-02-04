# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 550
标题: Shortest Path to Get Food
难度: medium
链接: https://leetcode.cn/problems/shortest-path-to-get-food/
题目类型: 广度优先搜索、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1730. 获取食物的最短路径 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来找到从起点到食物的最短路径。

算法步骤:
1. 初始化一个队列，将起点位置加入队列，并标记为已访问。
2. 开始进行BFS遍历：
   - 从队列中取出一个位置。
   - 检查该位置是否是食物，如果是则返回当前步数。
   - 否则，将该位置的四个相邻位置（上、下、左、右）加入队列，并标记为已访问。
3. 如果队列为空且未找到食物，则返回-1。

关键点:
- 使用队列进行BFS遍历。
- 使用集合记录已访问的位置，避免重复访问。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中m和n分别是网格的行数和列数。每个位置最多只会被访问一次。
空间复杂度: O(m * n)，在最坏情况下，队列和访问集合的大小可能达到m * n。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(grid: List[List[str]]) -> int:
    """
    函数式接口 - 使用BFS找到从起点到食物的最短路径
    """
    if not grid or not grid[0]:
        return -1

    m, n = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = []
    visited = set()

    # 找到起点位置
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '*':
                queue.append((i, j, 0))
                visited.add((i, j))
                break

    while queue:
        x, y, steps = queue.pop(0)
        if grid[x][y] == '#':
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] != 'X':
                queue.append((nx, ny, steps + 1))
                visited.add((nx, ny))

    return -1


Solution = create_solution(solution_function_name)