# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3837
标题: Grid Teleportation Traversal
难度: medium
链接: https://leetcode.cn/problems/grid-teleportation-traversal/
题目类型: 广度优先搜索、数组、哈希表、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3552. 网格传送门旅游 - 给你一个大小为 m x n 的二维字符网格 matrix，用字符串数组表示，其中 matrix[i][j] 表示第 i 行和第 j 列处的单元格。每个单元格可以是以下几种字符之一： * '.' 表示一个空单元格。 * '#' 表示一个障碍物。 * 一个大写字母（'A' 到 'Z'）表示一个传送门。 你从左上角单元格 (0, 0) 出发，目标是到达右下角单元格 (m - 1, n - 1)。你可以从当前位置移动到相邻的单元格（上、下、左、右），移动后的单元格必须在网格边界内且不是障碍物。 如果你踏入一个包含传送门字母的单元格，并且你之前没有使用过该传送门字母，你可以立即传送到网格中另一个具有相同字母的单元格。这次传送不计入移动次数，但每个字母对应的传送门在旅程中 最多 只能使用一次。 返回到达右下角单元格所需的 最少 移动次数。如果无法到达目的地，则返回 -1。 示例 1： 输入： matrix = ["A..",".A.","..."] 输出： 2 解释： [https://assets.leetcode.com/uploads/2025/03/15/example04140.png] * 在第一次移动之前，从 (0, 0) 传送到 (1, 1)。 * 第一次移动，从 (1, 1) 移动到 (1, 2)。 * 第二次移动，从 (1, 2) 移动到 (2, 2)。 示例 2： 输入： matrix = [".#...",".#.#.",".#.#.","...#."] 输出： 13 解释： [https://assets.leetcode.com/uploads/2025/03/15/ezgifcom-animated-gif-maker.gif] 提示： * 1 <= m == matrix.length <= 103 * 1 <= n == matrix[i].length <= 103 * matrix[i][j] 是 '#'、'.' 或一个大写英文字母。 * matrix[0][0] 不是障碍物。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）结合传送门的特性来找到最短路径。

算法步骤:
1. 构建传送门的位置映射，记录每个传送门字母的所有位置。
2. 使用队列进行BFS，队列中的每个元素包含当前坐标、已使用的传送门集合和当前步数。
3. 对于每个节点，检查其四个方向的邻居，如果邻居是空单元格或未使用过的传送门，则将其加入队列。
4. 如果遇到传送门且未使用过，则通过传送门传送到所有其他相同字母的传送门位置。
5. 如果到达右下角单元格，返回当前步数；如果队列为空且未到达目标，则返回-1。

关键点:
- 使用集合记录已使用的传送门，避免重复使用。
- 通过传送门时，将所有相同字母的传送门位置都加入队列。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中m和n分别是网格的行数和列数。每个单元格最多被访问一次。
空间复杂度: O(m * n)，队列和已访问集合的空间开销。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Set, Tuple
from collections import deque, defaultdict

def solution_function_name(matrix: List[str]) -> int:
    if not matrix or not matrix[0]:
        return -1

    m, n = len(matrix), len(matrix[0])
    portals = defaultdict(list)
    for i in range(m):
        for j in range(n):
            if matrix[i][j].isalpha():
                portals[matrix[i][j]].append((i, j))

    def bfs() -> int:
        queue = deque([((0, 0), set(), 0)])
        visited = set([(0, 0, frozenset())])

        while queue:
            (x, y), used_portals, steps = queue.popleft()
            if (x, y) == (m - 1, n - 1):
                return steps

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != '#':
                    if matrix[nx][ny] == '.':
                        if (nx, ny, frozenset(used_portals)) not in visited:
                            visited.add((nx, ny, frozenset(used_portals)))
                            queue.append(((nx, ny), used_portals, steps + 1))
                    elif matrix[nx][ny].isalpha():
                        if matrix[nx][ny] not in used_portals:
                            new_used_portals = used_portals | {matrix[nx][ny]}
                            for px, py in portals[matrix[nx][ny]]:
                                if (px, py, frozenset(new_used_portals)) not in visited:
                                    visited.add((px, py, frozenset(new_used_portals)))
                                    queue.append(((px, py), new_used_portals, steps + 1))
        return -1

    return bfs()

Solution = create_solution(solution_function_name)