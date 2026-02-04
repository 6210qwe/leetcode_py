# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000375
标题: 自行车炫技赛场
难度: medium
链接: https://leetcode.cn/problems/kplEvH/
题目类型: 深度优先搜索、广度优先搜索、记忆化搜索、数组、动态规划、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 45. 自行车炫技赛场 - 「力扣挑战赛」中 `N*M` 大小的自行车炫技赛场的场地由一片连绵起伏的上下坡组成，场地的高度值记录于二维数组 `terrain` 中，场地的减速值记录于二维数组 `obstacle` 中。 - 若选手骑着自行车从高度为 `h1` 且减速值为 `o1` 的位置到高度为 `h2` 且减速值为 `o2` 的相邻位置（上下左右四个方向），速度变化值为 `h1-h2-o2`（负值减速，正值增速）。 选手初始位于坐标 `position` 处且初始速度为 1，请问选手可以刚好到其他哪些位置时速度依旧为 1。请以二维数组形式返回这些位置。若有多个位置则按行坐标升序排列，若有多个位置行坐标相同则按列坐标升序排列。 **注意：** 骑行过程中速度不能为零或负值 **示例 1：** > 输入：`position = [0,0], terrain = [[0,0],[0,0]], obstacle = [[0,0],[0,0]]` > > 输出：`[[0,1],[1,0],[1,1]]` > > 解释： > 由于当前场地属于平地，根据上面的规则，选手从`[0,0]`的位置出发都能刚好在其他处的位置速度为 1。 **示例 2：** > 输入：`position = [1,1], terrain = [[5,0],[0,6]], obstacle = [[0,6],[7,0]]` > > 输出：`[[0,1]]` > > 解释： > 选手从 `[1,1]` 处的位置出发，到 `[0,1]` 处的位置时恰好速度为 1。 **提示：** - `n == terrain.length == obstacle.length` - `m == terrain[i].length == obstacle[i].length` - `1 <= n <= 100` - `1 <= m <= 100` - `0 <= terrain[i][j], obstacle[i][j] <= 100` - `position.length == 2` - `0 <= position[0] < n` - `0 <= position[1] < m`
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索（DFS）结合记忆化搜索来解决这个问题。通过记忆化搜索避免重复计算，提高效率。

算法步骤:
1. 定义一个递归函数 `dfs`，用于从当前位置进行深度优先搜索。
2. 在 `dfs` 函数中，检查当前位置是否已经访问过，并且当前速度是否为 1。如果是，则将该位置加入结果列表。
3. 如果当前位置没有访问过，则继续向四个方向进行搜索。
4. 使用一个字典 `memo` 来记录已经访问过的状态，避免重复计算。
5. 对结果列表进行排序，确保按行坐标升序排列，若有多个位置行坐标相同则按列坐标升序排列。

关键点:
- 使用记忆化搜索来避免重复计算。
- 确保速度不能为零或负值。
- 对结果进行排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m * max(terrain[i][j]) * max(obstacle[i][j]))，其中 n 和 m 分别是 terrain 和 obstacle 的行数和列数。
空间复杂度: O(n * m * max(terrain[i][j]) * max(obstacle[i][j]))，用于存储记忆化搜索的状态。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(position: List[int], terrain: List[List[int]], obstacle: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 使用深度优先搜索（DFS）结合记忆化搜索来解决这个问题。
    """
    n, m = len(terrain), len(terrain[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    memo = {}
    result = []

    def dfs(x, y, speed):
        if (x, y, speed) in memo:
            return
        memo[(x, y, speed)] = True

        if speed == 1 and (x, y) != tuple(position):
            result.append([x, y])

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                new_speed = speed + terrain[x][y] - terrain[nx][ny] - obstacle[nx][ny]
                if new_speed > 0:
                    dfs(nx, ny, new_speed)

    dfs(position[0], position[1], 1)
    result.sort()
    return result


Solution = create_solution(solution_function_name)