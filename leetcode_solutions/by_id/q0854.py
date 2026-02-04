# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 854
标题: Making A Large Island
难度: hard
链接: https://leetcode.cn/problems/making-a-large-island/
题目类型: 深度优先搜索、广度优先搜索、并查集、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
827. 最大人工岛 - 给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。 返回执行此操作后，grid 中最大的岛屿面积是多少？ 岛屿 由一组上、下、左、右四个方向相连的 1 形成。 示例 1: 输入: grid = [[1, 0], [0, 1]] 输出: 3 解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。 示例 2: 输入: grid = [[1, 1], [1, 0]] 输出: 4 解释: 将一格0变成1，岛屿的面积扩大为 4。 示例 3: 输入: grid = [[1, 1], [1, 1]] 输出: 4 解释: 没有0可以让我们变成1，面积依然为 4。 提示： * n == grid.length * n == grid[i].length * 1 <= n <= 500 * grid[i][j] 为 0 或 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来标记每个岛屿，并计算每个岛屿的面积。然后遍历所有的 0 位置，计算将其变为 1 后的最大岛屿面积。

算法步骤:
1. 使用 DFS 标记每个岛屿，并计算每个岛屿的面积。
2. 遍历所有的 0 位置，计算将其变为 1 后的最大岛屿面积。

关键点:
- 使用字典来存储每个岛屿的面积。
- 在遍历 0 位置时，合并相邻岛屿的面积。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是网格的边长。我们需要遍历整个网格两次，一次是标记岛屿，一次是计算最大岛屿面积。
空间复杂度: O(n^2)，用于存储每个岛屿的面积和访问标记。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def dfs(grid, i, j, index):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
        return 0
    grid[i][j] = index
    area = 1
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        area += dfs(grid, i + di, j + dj, index)
    return area

def largest_island(grid: List[List[int]]) -> int:
    n = len(grid)
    if n == 0:
        return 0
    
    # 标记岛屿并计算面积
    index = 2
    area_dict = {}
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                area = dfs(grid, i, j, index)
                area_dict[index] = area
                index += 1
    
    # 计算最大岛屿面积
    max_area = max(area_dict.values(), default=0)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                seen = set()
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                        seen.add(grid[ni][nj])
                new_area = 1 + sum(area_dict[index] for index in seen)
                max_area = max(max_area, new_area)
    
    return max_area

Solution = create_solution(largest_island)