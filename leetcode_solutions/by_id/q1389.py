# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1389
标题: Minimum Moves to Move a Box to Their Target Location
难度: hard
链接: https://leetcode.cn/problems/minimum-moves-to-move-a-box-to-their-target-location/
题目类型: 广度优先搜索、数组、矩阵、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1263. 推箱子 - 「推箱子」是一款风靡全球的益智小游戏，玩家需要将箱子推到仓库中的目标位置。 游戏地图用大小为 m x n 的网格 grid 表示，其中每个元素可以是墙、地板或者是箱子。 现在你将作为玩家参与游戏，按规则将箱子 'B' 移动到目标位置 'T' ： * 玩家用字符 'S' 表示，只要他在地板上，就可以在网格中向上、下、左、右四个方向移动。 * 地板用字符 '.' 表示，意味着可以自由行走。 * 墙用字符 '#' 表示，意味着障碍物，不能通行。 * 箱子仅有一个，用字符 'B' 表示。相应地，网格上有一个目标位置 'T'。 * 玩家需要站在箱子旁边，然后沿着箱子的方向进行移动，此时箱子会被移动到相邻的地板单元格。记作一次「推动」。 * 玩家无法越过箱子。 返回将箱子推到目标位置的最小 推动 次数，如果无法做到，请返回 -1。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/11/16/sample_1_1620.png] 输入：grid = [["#","#","#","#","#","#"], ["#","T","#","#","#","#"], ["#",".",".","B",".","#"], ["#",".","#","#",".","#"], ["#",".",".",".","S","#"], ["#","#","#","#","#","#"]] 输出：3 解释：我们只需要返回推箱子的次数。 示例 2： 输入：grid = [["#","#","#","#","#","#"], ["#","T","#","#","#","#"], ["#",".",".","B",".","#"], ["#","#","#","#",".","#"], ["#",".",".",".","S","#"], ["#","#","#","#","#","#"]] 输出：-1 示例 3： 输入：grid = [["#","#","#","#","#","#"], ["#","T",".",".","#","#"], ["#",".","#","B",".","#"], ["#",".",".",".",".","#"], ["#",".",".",".","S","#"], ["#","#","#","#","#","#"]] 输出：5 解释：向下、向左、向左、向上再向上。 提示： * m == grid.length * n == grid[i].length * 1 <= m, n <= 20 * grid 仅包含字符 '.', '#', 'S' , 'T', 以及 'B'。 * grid 中 'S', 'B' 和 'T' 各只能出现一个。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索 (BFS) 来找到从初始状态到目标状态的最短路径。

算法步骤:
1. 初始化 BFS 队列，记录箱子和玩家的位置，并初始化访问集合。
2. 对于队列中的每个状态，尝试所有可能的移动（上下左右）。
3. 如果移动后的新状态未被访问过，则将其加入队列，并更新访问集合。
4. 如果箱子到达目标位置，返回推动次数。
5. 如果队列为空且未找到解，返回 -1。

关键点:
- 使用元组 (box_x, box_y, player_x, player_y, moves) 来表示状态。
- 使用集合来记录已访问的状态，避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * 4^k)，其中 k 是推箱子的最大步数，m 和 n 分别是网格的行数和列数。
空间复杂度: O(m * n * 4^k)，用于存储 BFS 队列和访问集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Tuple
from collections import deque

def min_push_box(grid: List[List[str]]) -> int:
    def is_valid(x: int, y: int) -> bool:
        return 0 <= x < m and 0 <= y < n and grid[x][y] != '#'

    def can_move_to_target(x: int, y: int, target_x: int, target_y: int) -> bool:
        if (x, y) == (target_x, target_y):
            return True
        visited = set()
        queue = deque([(x, y)])
        while queue:
            cur_x, cur_y = queue.popleft()
            for dx, dy in directions:
                new_x, new_y = cur_x + dx, cur_y + dy
                if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                    if (new_x, new_y) == (target_x, target_y):
                        return True
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y))
        return False

    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = None
    box = None
    target = None

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'B':
                box = (i, j)
            elif grid[i][j] == 'T':
                target = (i, j)

    queue = deque([(box[0], box[1], start[0], start[1], 0)])
    visited = set([(box[0], box[1], start[0], start[1])])

    while queue:
        bx, by, px, py, moves = queue.popleft()
        if (bx, by) == target:
            return moves

        for dx, dy in directions:
            nbx, nby = bx + dx, by + dy
            pbx, pby = bx - dx, by - dy

            if is_valid(nbx, nby) and is_valid(pbx, pby) and can_move_to_target(px, py, pbx, pby):
                if (nbx, nby, bx, by) not in visited:
                    visited.add((nbx, nby, bx, by))
                    queue.append((nbx, nby, bx, by, moves + 1))

    return -1

Solution = create_solution(min_push_box)