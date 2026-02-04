# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2344
标题: Escape the Spreading Fire
难度: hard
链接: https://leetcode.cn/problems/escape-the-spreading-fire/
题目类型: 广度优先搜索、数组、二分查找、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2258. 逃离火灾 - 给你一个下标从 0 开始大小为 m x n 的二维整数数组 grid ，它表示一个网格图。每个格子为下面 3 个值之一： * 0 表示草地。 * 1 表示着火的格子。 * 2 表示一座墙，你跟火都不能通过这个格子。 一开始你在最左上角的格子 (0, 0) ，你想要到达最右下角的安全屋格子 (m - 1, n - 1) 。每一分钟，你可以移动到 相邻 的草地格子。每次你移动 之后 ，着火的格子会扩散到所有不是墙的 相邻 格子。 请你返回你在初始位置可以停留的 最多 分钟数，且停留完这段时间后你还能安全到达安全屋。如果无法实现，请你返回 -1 。如果不管你在初始位置停留多久，你 总是 能到达安全屋，请你返回 109 。 注意，如果你到达安全屋后，火马上到了安全屋，这视为你能够安全到达安全屋。 如果两个格子有共同边，那么它们为 相邻 格子。 示例 1： [https://assets.leetcode.com/uploads/2022/03/10/ex1new.jpg] 输入：grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]] 输出：3 解释：上图展示了你在初始位置停留 3 分钟后的情形。 你仍然可以安全到达安全屋。 停留超过 3 分钟会让你无法安全到达安全屋。 示例 2： [https://assets.leetcode.com/uploads/2022/03/10/ex2new2.jpg] 输入：grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]] 输出：-1 解释：上图展示了你马上开始朝安全屋移动的情形。 火会蔓延到你可以移动的所有格子，所以无法安全到达安全屋。 所以返回 -1 。 示例 3： [https://assets.leetcode.com/uploads/2022/03/10/ex3new.jpg] 输入：grid = [[0,0,0],[2,2,0],[1,2,0]] 输出：1000000000 解释：上图展示了初始网格图。 注意，由于火被墙围了起来，所以无论如何你都能安全到达安全屋。 所以返回 109 。 提示： * m == grid.length * n == grid[i].length * 2 <= m, n <= 300 * 4 <= m * n <= 2 * 104 * grid[i][j] 是 0 ，1 或者 2 。 * grid[0][0] == grid[m - 1][n - 1] == 0
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来模拟火的扩散和人的移动。使用二分查找来确定最大等待时间。

算法步骤:
1. 使用 BFS 计算火从每个格子蔓延到其他格子的时间。
2. 使用 BFS 计算人从起点到终点的最短路径，并记录每一步的火蔓延时间。
3. 使用二分查找来确定最大等待时间，使得人在等待后仍能安全到达终点。

关键点:
- 使用 BFS 来计算火的蔓延时间和人的移动时间。
- 使用二分查找来优化等待时间的确定。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * log(m * n))
空间复杂度: O(m * n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import deque

def can_escape(grid: List[List[int]], wait_time: int) -> bool:
    m, n = len(grid), len(grid[0])
    fire_time = [[float('inf')] * n for _ in range(m)]
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    # BFS to calculate fire spread time
    queue = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                queue.append((i, j, 0))
                fire_time[i][j] = 0
    
    while queue:
        x, y, t = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and fire_time[nx][ny] > t + 1:
                fire_time[nx][ny] = t + 1
                queue.append((nx, ny, t + 1))
    
    # BFS to check if person can escape
    queue = deque([(0, 0, wait_time)])
    visited = set([(0, 0)])
    
    while queue:
        x, y, t = queue.popleft()
        if (x, y) == (m - 1, n - 1):
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] == 0:
                if t + 1 < fire_time[nx][ny]:
                    visited.add((nx, ny))
                    queue.append((nx, ny, t + 1))
    
    return False

def max_wait_time(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    low, high = 0, m * n
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        if can_escape(grid, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    
    if result == m * n:
        return 1000000000
    return result

Solution = create_solution(max_wait_time)