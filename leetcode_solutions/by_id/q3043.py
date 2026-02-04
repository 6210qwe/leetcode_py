# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3043
标题: Minimum Time Takes to Reach Destination Without Drowning
难度: hard
链接: https://leetcode.cn/problems/minimum-time-takes-to-reach-destination-without-drowning/
题目类型: 广度优先搜索、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2814. 避免淹死并到达目的地的最短时间 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来找到从起点到终点的最短路径。在每一步中，我们需要检查当前水位是否允许我们移动到下一个位置。

算法步骤:
1. 初始化队列，将起点加入队列，并记录起点的时间为0。
2. 使用一个集合来记录已经访问过的位置，避免重复访问。
3. 开始BFS遍历：
   - 从队列中取出一个位置和当前时间。
   - 检查该位置是否是终点，如果是则返回当前时间。
   - 检查该位置是否被淹没，如果被淹没则跳过。
   - 将该位置的四个方向（上、下、左、右）加入队列，并更新时间。
4. 如果遍历完所有可能的位置仍未到达终点，则返回-1。

关键点:
- 使用BFS可以保证找到最短路径。
- 需要处理水位变化，确保在移动时不会被淹没。
- 使用集合记录已访问位置，避免重复访问。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中m和n分别是网格的行数和列数。每个位置最多只会被访问一次。
空间复杂度: O(m * n)，队列和已访问集合的最大空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from collections import deque

def solution_function_name(grid: List[List[int]], water: List[List[int]]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    if not grid or not grid[0]:
        return -1

    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0, 0)])  # (row, col, time)
    visited = set([(0, 0)])

    while queue:
        row, col, time = queue.popleft()
        if row == m - 1 and col == n - 1:
            return time

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < m and 0 <= new_col < n and (new_row, new_col) not in visited:
                if water[new_row][new_col] > time + 1:
                    continue
                if grid[new_row][new_col] == 0:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, time + 1))

    return -1

Solution = create_solution(solution_function_name)