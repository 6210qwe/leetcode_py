# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1322
标题: Minimum Moves to Reach Target with Rotations
难度: hard
链接: https://leetcode.cn/problems/minimum-moves-to-reach-target-with-rotations/
题目类型: 广度优先搜索、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1210. 穿过迷宫的最少移动次数 - 你还记得那条风靡全球的贪吃蛇吗？ 我们在一个 n*n 的网格上构建了新的迷宫地图，蛇的长度为 2，也就是说它会占去两个单元格。蛇会从左上角（(0, 0) 和 (0, 1)）开始移动。我们用 0 表示空单元格，用 1 表示障碍物。蛇需要移动到迷宫的右下角（(n-1, n-2) 和 (n-1, n-1)）。 每次移动，蛇可以这样走： * 如果没有障碍，则向右移动一个单元格。并仍然保持身体的水平／竖直状态。 * 如果没有障碍，则向下移动一个单元格。并仍然保持身体的水平／竖直状态。 * 如果它处于水平状态并且其下面的两个单元都是空的，就顺时针旋转 90 度。蛇从（(r, c)、(r, c+1)）移动到 （(r, c)、(r+1, c)）。 [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/09/28/image-2.png] * 如果它处于竖直状态并且其右面的两个单元都是空的，就逆时针旋转 90 度。蛇从（(r, c)、(r+1, c)）移动到（(r, c)、(r, c+1)）。 [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/09/28/image-1.png] 返回蛇抵达目的地所需的最少移动次数。 如果无法到达目的地，请返回 -1。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/09/28/image.png] 输入：grid = [[0,0,0,0,0,1], [1,1,0,0,1,0], [0,0,0,0,1,1], [0,0,1,0,1,0], [0,1,1,0,0,0], [0,1,1,0,0,0]] 输出：11 解释： 一种可能的解决方案是 [右, 右, 顺时针旋转, 右, 下, 下, 下, 下, 逆时针旋转, 右, 下]。 示例 2： 输入：grid = [[0,0,1,1,1,1], [0,0,0,0,1,1], [1,1,0,0,0,1], [1,1,1,0,0,1], [1,1,1,0,0,1], [1,1,1,0,0,0]] 输出：9 提示： * 2 <= n <= 100 * 0 <= grid[i][j] <= 1 * 蛇保证从空单元格开始出发。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来找到从起点到终点的最短路径。每个节点表示蛇的状态，包括蛇头的位置和方向。

算法步骤:
1. 初始化队列，将起始状态加入队列，并标记为已访问。
2. 进行BFS遍历，每次从队列中取出一个状态，检查是否到达目标位置。
3. 如果未到达目标位置，生成所有可能的下一步状态（向右、向下、旋转），并将未访问过的状态加入队列。
4. 如果队列为空且未找到目标位置，返回-1。

关键点:
- 使用一个三维数组 visited 来记录每个状态是否被访问过。
- 每个状态包含蛇头的位置和方向（水平或垂直）。
- 通过检查下一个状态是否有效（即不越界且无障碍物）来生成下一步状态。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)
空间复杂度: O(n^2)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Tuple
from collections import deque

def minimumMoves(grid: List[List[int]]) -> int:
    n = len(grid)
    if grid[0][0] == 1 or grid[0][1] == 1:
        return -1

    # 状态定义：(row, col, direction) 其中direction=0表示水平，direction=1表示垂直
    start = (0, 0, 0)
    end = (n - 1, n - 2, 0)

    # 访问标记
    visited = [[[False for _ in range(2)] for _ in range(n)] for _ in range(n)]
    visited[0][0][0] = True

    # 队列初始化
    queue = deque([(start, 0)])

    while queue:
        (row, col, direction), moves = queue.popleft()

        # 到达终点
        if (row, col, direction) == end:
            return moves

        # 向右移动
        if direction == 0 and col + 2 < n and grid[row][col + 2] == 0 and not visited[row][col + 1][direction]:
            visited[row][col + 1][direction] = True
            queue.append(((row, col + 1, direction), moves + 1))

        # 向下移动
        if direction == 1 and row + 2 < n and grid[row + 2][col] == 0 and not visited[row + 1][col][direction]:
            visited[row + 1][col][direction] = True
            queue.append(((row + 1, col, direction), moves + 1))

        # 顺时针旋转
        if direction == 0 and row + 1 < n and grid[row + 1][col] == 0 and grid[row + 1][col + 1] == 0 and not visited[row][col][1]:
            visited[row][col][1] = True
            queue.append(((row, col, 1), moves + 1))

        # 逆时针旋转
        if direction == 1 and col + 1 < n and grid[row][col + 1] == 0 and grid[row + 1][col + 1] == 0 and not visited[row][col][0]:
            visited[row][col][0] = True
            queue.append(((row, col, 0), moves + 1))

    return -1

Solution = create_solution(minimumMoves)