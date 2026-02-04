# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2588
标题: Maximum Number of Points From Grid Queries
难度: hard
链接: https://leetcode.cn/problems/maximum-number-of-points-from-grid-queries/
题目类型: 广度优先搜索、并查集、数组、双指针、矩阵、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2503. 矩阵查询可获得的最大分数 - 给你一个大小为 m x n 的整数矩阵 grid 和一个大小为 k 的数组 queries 。 找出一个大小为 k 的数组 answer ，且满足对于每个整数 queries[i] ，你从矩阵 左上角 单元格开始，重复以下过程： * 如果 queries[i] 严格 大于你当前所处位置单元格，如果该单元格是第一次访问，则获得 1 分，并且你可以移动到所有 4 个方向（上、下、左、右）上任一 相邻 单元格。 * 否则，你不能获得任何分，并且结束这一过程。 在过程结束后，answer[i] 是你可以获得的最大分数。注意，对于每个查询，你可以访问同一个单元格 多次 。 返回结果数组 answer 。 示例 1： [https://assets.leetcode.com/uploads/2025/03/15/image1.png] 输入：grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2] 输出：[5,8,1] 解释：上图展示了每个查询中访问并获得分数的单元格。 示例 2： [https://assets.leetcode.com/uploads/2022/10/20/yetgriddrawio-2.png] 输入：grid = [[5,2,1],[1,1,2]], queries = [3] 输出：[0] 解释：无法获得分数，因为左上角单元格的值大于等于 3 。 提示： * m == grid.length * n == grid[i].length * 2 <= m, n <= 1000 * 4 <= m * n <= 105 * k == queries.length * 1 <= k <= 104 * 1 <= grid[i][j], queries[i] <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用优先队列和广度优先搜索来处理每个查询。首先对查询进行排序，然后使用优先队列来扩展可以访问的单元格。

算法步骤:
1. 将查询按值从小到大排序。
2. 使用优先队列存储可以访问的单元格及其值。
3. 对于每个查询，从优先队列中取出所有小于当前查询值的单元格，并将其相邻单元格加入优先队列。
4. 记录每个查询的结果。

关键点:
- 使用优先队列来高效地扩展可以访问的单元格。
- 每个查询的结果基于前一个查询的结果进行更新。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((m * n + k) log(m * n))
空间复杂度: O(m * n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq

def maxPoints(grid: List[List[int]], queries: List[int]) -> List[int]:
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * n for _ in range(m)]
    
    def in_bounds(x, y):
        return 0 <= x < m and 0 <= y < n
    
    # 优先队列，存储 (值, 行, 列)
    pq = []
    heapq.heappush(pq, (grid[0][0], 0, 0))
    visited[0][0] = True
    result = [0] * len(queries)
    query_indices = sorted(range(len(queries)), key=lambda i: queries[i])
    
    points = 0
    for i in query_indices:
        while pq and pq[0][0] < queries[i]:
            val, x, y = heapq.heappop(pq)
            points += 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if in_bounds(nx, ny) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(pq, (grid[nx][ny], nx, ny))
        result[i] = points
    
    return [result[i] for i in query_indices]

Solution = create_solution(maxPoints)