# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 417
标题: Pacific Atlantic Water Flow
难度: medium
链接: https://leetcode.cn/problems/pacific-atlantic-water-flow/
题目类型: 深度优先搜索、广度优先搜索、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
417. 太平洋大西洋水流问题 - 有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。 这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c) 上单元格 高于海平面的高度 。 岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。 返回网格坐标 result 的 2D 列表 ，其中 result[i] = [ri, ci] 表示雨水从单元格 (ri, ci) 流动 既可流向太平洋也可流向大西洋 。 示例 1： [https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg] 输入: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]] 输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]] 示例 2： 输入: heights = [[2,1],[1,2]] 输出: [[0,0],[0,1],[1,0],[1,1]] 提示： * m == heights.length * n == heights[r].length * 1 <= m, n <= 200 * 0 <= heights[r][c] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 反向搜索（逆流而上）——从两个海洋边界出发进行 DFS/BFS，标记能到达各自海洋的格子，最终取交集。

算法步骤:
1. 初始化两个布尔矩阵 `pacific_reachable` 和 `atlantic_reachable`，大小均为 m×n，初始为 False。
2. 从太平洋边界（第 0 行、第 0 列）开始 DFS/BFS，标记所有能流向太平洋的格子（条件：邻居高度 >= 当前高度，因逆流需“上坡”）。
3. 从大西洋边界（最后一行、最后一列）开始 DFS/BFS，标记所有能流向大西洋的格子。
4. 遍历整个矩阵，收集同时被两个矩阵标记为 True 的坐标，即为答案。

关键点:
- 注意边界条件：确保坐标在 [0, m) × [0, n) 范围内，且未访问过。
- 优化时间和空间复杂度：使用 DFS 或 BFS 均可，时间 O(mn)，空间 O(mn)（栈/队列 + visited 矩阵）；避免重复递归/入队。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m × n) - 每个格子最多被访问常数次（两次 DFS 各一次 + 最终扫描一次）
空间复杂度: O(m × n) - 用于存储两个访问矩阵及递归栈/队列（最坏深度 O(mn)）
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def pacific_atlantic_water_flow(heights: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 使用反向 DFS 求解太平洋-大西洋水流问题
    
    实现思路:
    从太平洋（上边+左边）和大西洋（下边+右边）边界出发，反向搜索所有能到达对应海洋的格子（要求路径非递减），
    最终返回两个集合的交集坐标。
    
    Args:
        heights: m x n 整数矩阵，heights[r][c] 表示位置 (r, c) 的海拔高度
        
    Returns:
        List[List[int]]: 所有能同时流向太平洋和大西洋的坐标列表，每个元素为 [row, col]
        
    Example:
        >>> pacific_atlantic_water_flow([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
        [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    """
    if not heights or not heights[0]:
        return []

    m, n = len(heights), len(heights[0])
    # 标记能到达太平洋 / 大西洋的格子
    pacific = [[False] * n for _ in range(m)]
    atlantic = [[False] * n for _ in range(m)]

    # 四个方向：上、下、左、右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(r: int, c: int, visited: List[List[bool]], prev_height: int):
        """从 (r,c) 出发，标记所有能流向 prev_height 所代表海洋的格子（逆流：要求 heights[r][c] >= prev_height）"""
        if (r < 0 or r >= m or c < 0 or c >= n or
            visited[r][c] or heights[r][c] < prev_height):
            return
        visited[r][c] = True
        for dr, dc in directions:
            dfs(r + dr, c + dc, visited, heights[r][c])

    # 从太平洋边界（第0行、第0列）开始 DFS
    for i in range(m):
        dfs(i, 0, pacific, heights[i][0])
    for j in range(n):
        dfs(0, j, pacific, heights[0][j])

    # 从大西洋边界（最后一行、最后一列）开始 DFS
    for i in range(m):
        dfs(i, n - 1, atlantic, heights[i][n - 1])
    for j in range(n):
        dfs(m - 1, j, atlantic, heights[m - 1][j])

    # 收集同时可达两洋的坐标
    result = []
    for i in range(m):
        for j in range(n):
            if pacific[i][j] and atlantic[i][j]:
                result.append([i, j])
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(pacific_atlantic_water_flow)