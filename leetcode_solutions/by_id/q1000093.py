# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000093
标题: 寻宝
难度: hard
链接: https://leetcode.cn/problems/xun-bao/
题目类型: 位运算、广度优先搜索、数组、动态规划、状态压缩、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 13. 寻宝 - 我们得到了一副藏宝图，藏宝图显示，在一个迷宫中存在着未被世人发现的宝藏。 迷宫是一个二维矩阵，用一个字符串数组表示。它标识了唯一的入口（用 'S' 表示），和唯一的宝藏地点（用 'T' 表示）。但是，宝藏被一些隐蔽的机关保护了起来。在地图上有若干个机关点（用 'M' 表示），只有所有机关均被触发，才可以拿到宝藏。 要保持机关的触发，需要把一个重石放在上面。迷宫中有若干个石堆（用 'O' 表示），每个石堆都有无限个足够触发机关的重石。但是由于石头太重，我们一次只能搬一个石头到指定地点。 迷宫中同样有一些墙壁（用 '#' 表示），我们不能走入墙壁。剩余的都是可随意通行的点（用 '.' 表示）。石堆、机关、起点和终点（无论是否能拿到宝藏）也是可以通行的。 我们每步可以选择向上/向下/向左/向右移动一格，并且不能移出迷宫。搬起石头和放下石头不算步数。那么，从起点开始，我们最少需要多少步才能最后拿到宝藏呢？如果无法拿到宝藏，返回 -1 。 示例 1： > 输入： ["S#O", "M..", "M.T"] > > 输出：16 > > 解释：最优路线为： S->O, cost = 4, 去搬石头 O->第二行的M, cost = 3, M机关触发 第二行的M->O, cost = 3, 我们需要继续回去 O 搬石头。 O->第三行的M, cost = 4, 此时所有机关均触发 第三行的M->T, cost = 2，去T点拿宝藏。 总步数为16。 图片.gif [https://pic.leetcode.cn/6bfff669ad65d494cdc237bcedfec10a2b1ac2f2593c2bf97e9aecb41dc8a08b-%E5%9B%BE%E7%89%87.gif] 示例 2： > 输入： ["S#O", "M.#", "M.T"] > > 输出：-1 > > 解释：我们无法搬到石头触发机关 示例 3： > 输入： ["S#O", "M.T", "M.."] > > 输出：17 > > 解释：注意终点也是可以通行的。 限制： * 1 <= maze.length <= 100 * 1 <= maze[i].length <= 100 * maze[i].length == maze[j].length * S 和 T 有且只有一个 * 0 <= M的数量 <= 16 * 0 <= O的数量 <= 40，题目保证当迷宫中存在 M 时，一定存在至少一个 O 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索 (BFS) 来计算从一个点到另一个点的最短路径。使用状态压缩来记录哪些机关已经被触发。

算法步骤:
1. 找到所有的特殊点（起点 S、终点 T、机关 M 和石堆 O）的位置。
2. 使用 BFS 计算从每一个特殊点到其他所有特殊点的最短路径，并存储在一个距离表中。
3. 使用动态规划 (DP) 和状态压缩来找到从起点出发，触发所有机关并到达终点的最短路径。

关键点:
- 使用 BFS 计算最短路径。
- 使用状态压缩来记录哪些机关已经被触发。
- 动态规划来找到最优解。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((M + O + 1) * 2^M)，其中 M 是机关的数量，O 是石堆的数量。
空间复杂度: O((M + O + 1) * 2^M)，用于存储距离表和 DP 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import deque
import sys

def bfs(maze: List[str], start: tuple, special_points: List[tuple]) -> List[int]:
    n, m = len(maze), len(maze[0])
    queue = deque([start])
    visited = set([start])
    dist = {point: -1 for point in special_points}
    
    if start in special_points:
        dist[start] = 0
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
                if (nx, ny) in special_points:
                    dist[(nx, ny)] = dist[(x, y)] + 1
    return [dist[point] for point in special_points]

def solution_function_name(maze: List[str]) -> int:
    n, m = len(maze), len(maze[0])
    special_points = []
    start, end = None, None
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'T':
                end = (i, j)
            elif maze[i][j] in ['M', 'O']:
                special_points.append((i, j))
    
    if start is None or end is None:
        return -1
    
    special_points = [start, end] + special_points
    k = len(special_points)
    dist = [[0] * k for _ in range(k)]
    
    for i in range(k):
        distances = bfs(maze, special_points[i], special_points)
        for j in range(k):
            dist[i][j] = distances[j]
    
    dp = [[sys.maxsize] * k for _ in range(1 << k)]
    dp[1 << 0][0] = 0
    
    for mask in range(1, 1 << k):
        for i in range(k):
            if mask & (1 << i):
                for j in range(k):
                    if not (mask & (1 << j)) and dist[i][j] != -1:
                        dp[mask | (1 << j)][j] = min(dp[mask | (1 << j)][j], dp[mask][i] + dist[i][j])
    
    result = min(dp[(1 << k) - 1])
    return result if result != sys.maxsize else -1

Solution = create_solution(solution_function_name)