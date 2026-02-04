# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1117
标题: As Far from Land as Possible
难度: medium
链接: https://leetcode.cn/problems/as-far-from-land-as-possible/
题目类型: 广度优先搜索、数组、动态规划、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1162. 地图分析 - 你现在手里有一份大小为 n x n 的 网格 grid，上面的每个 单元格 都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地。 请你找出一个海洋单元格，这个海洋单元格到离它最近的陆地单元格的距离是最大的，并返回该距离。如果网格上只有陆地或者海洋，请返回 -1。 我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个单元格之间的距离是 |x0 - x1| + |y0 - y1| 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/08/17/1336_ex1.jpeg] 输入：grid = [[1,0,1],[0,0,0],[1,0,1]] 输出：2 解释： 海洋单元格 (1, 1) 和所有陆地单元格之间的距离都达到最大，最大距离为 2。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/08/17/1336_ex2.jpeg] 输入：grid = [[1,0,0],[0,0,0],[0,0,0]] 输出：4 解释： 海洋单元格 (2, 2) 和所有陆地单元格之间的距离都达到最大，最大距离为 4。 提示： * n == grid.length * n == grid[i].length * 1 <= n <= 100 * grid[i][j] 不是 0 就是 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用多源广度优先搜索（BFS）从所有陆地单元格同时开始扩展，直到找到最远的海洋单元格。

算法步骤:
1. 初始化队列，将所有陆地单元格加入队列。
2. 初始化距离矩阵，所有陆地单元格的距离设为 0，海洋单元格的距离设为无穷大。
3. 使用 BFS 从所有陆地单元格同时开始扩展，更新海洋单元格的距离。
4. 找到距离矩阵中最大的距离值，即为所求的最大距离。

关键点:
- 使用多源 BFS 可以同时从所有陆地单元格开始扩展，避免了多次单源 BFS 的重复计算。
- 使用距离矩阵记录每个单元格到最近陆地的距离。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是网格的边长。每个单元格最多会被访问一次。
空间复杂度: O(n^2)，用于存储队列和距离矩阵。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_distance(grid: List[List[int]]) -> int:
    """
    函数式接口 - 返回网格中海洋单元格到最近陆地单元格的最大距离
    """
    if not grid or not grid[0]:
        return -1

    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = []
    distance = [[float('inf')] * n for _ in range(n)]

    # 初始化队列和距离矩阵
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                queue.append((i, j))
                distance[i][j] = 0

    # 如果没有陆地或全是陆地，返回 -1
    if not queue or len(queue) == n * n:
        return -1

    # 多源 BFS
    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and distance[nx][ny] > distance[x][y] + 1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

    # 找到最大距离
    max_dist = max(max(row) for row in distance)
    return max_dist if max_dist != float('inf') else -1


Solution = create_solution(max_distance)