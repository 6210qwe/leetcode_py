# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1990
标题: Get Biggest Three Rhombus Sums in a Grid
难度: medium
链接: https://leetcode.cn/problems/get-biggest-three-rhombus-sums-in-a-grid/
题目类型: 数组、数学、矩阵、前缀和、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1878. 矩阵中最大的三个菱形和 - 给你一个 m x n 的整数矩阵 grid 。 菱形和 指的是 grid 中一个正菱形 边界 上的元素之和。本题中的菱形必须为正方形旋转45度，且四个角都在一个格子当中。下图是四个可行的菱形，每个菱形和应该包含的格子都用了相应颜色标注在图中。 [https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-desc-2.png] 注意，菱形可以是一个面积为 0 的区域，如上图中右下角的紫色菱形所示。 请你按照 降序 返回 grid 中三个最大的 互不相同的菱形和 。如果不同的和少于三个，则将它们全部返回。 示例 1： [https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-ex1.png] 输入：grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]] 输出：[228,216,211] 解释：最大的三个菱形和如上图所示。 - 蓝色：20 + 3 + 200 + 5 = 228 - 红色：200 + 2 + 10 + 4 = 216 - 绿色：5 + 200 + 4 + 2 = 211 示例 2： [https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-ex2.png] 输入：grid = [[1,2,3],[4,5,6],[7,8,9]] 输出：[20,9,8] 解释：最大的三个菱形和如上图所示。 - 蓝色：4 + 2 + 6 + 8 = 20 - 红色：9 （右下角红色的面积为 0 的菱形） - 绿色：8 （下方中央面积为 0 的菱形） 示例 3： 输入：grid = [[7,7,7]] 输出：[7] 解释：所有三个可能的菱形和都相同，所以返回 [7] 。 提示： * m == grid.length * n == grid[i].length * 1 <= m, n <= 100 * 1 <= grid[i][j] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和计算菱形和，并使用最大堆维护前三大的菱形和。

算法步骤:
1. 计算前缀和数组。
2. 遍历所有可能的菱形中心点和边长，计算菱形和并更新最大堆。
3. 从最大堆中取出前三大的菱形和。

关键点:
- 使用前缀和优化菱形和的计算。
- 使用最大堆维护前三大的菱形和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * min(m, n))，其中 m 和 n 分别是矩阵的行数和列数。
空间复杂度: O(m * n)，用于存储前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq

def get_biggest_three(grid: List[List[int]]) -> List[int]:
    def get_prefix_sum(grid):
        m, n = len(grid), len(grid[0])
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sum[i][j] = grid[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
        return prefix_sum

    def get_rhombus_sum(prefix_sum, center, side_length):
        if side_length == 0:
            return grid[center[0]][center[1]]
        
        top, bottom = center[0] - side_length, center[0] + side_length
        left, right = center[1] - side_length, center[1] + side_length
        
        if top < 0 or bottom >= len(grid) or left < 0 or right >= len(grid[0]):
            return 0
        
        top_left = (top, center[1])
        top_right = (top, right)
        bottom_left = (bottom, left)
        bottom_right = (bottom, center[1])
        
        sum_top = prefix_sum[top + 1][right + 1] - prefix_sum[top + 1][center[1]] - prefix_sum[top][right + 1] + prefix_sum[top][center[1]]
        sum_bottom = prefix_sum[bottom + 1][center[1] + 1] - prefix_sum[bottom + 1][left] - prefix_sum[bottom][center[1] + 1] + prefix_sum[bottom][left]
        sum_left = prefix_sum[center[0] + 1][left + 1] - prefix_sum[center[0] + 1][center[1]] - prefix_sum[top + 1][left + 1] + prefix_sum[top + 1][center[1]]
        sum_right = prefix_sum[bottom + 1][right + 1] - prefix_sum[bottom + 1][center[1]] - prefix_sum[center[0] + 1][right + 1] + prefix_sum[center[0] + 1][center[1]]
        
        return sum_top + sum_bottom + sum_left + sum_right

    m, n = len(grid), len(grid[0])
    prefix_sum = get_prefix_sum(grid)
    max_heap = []
    
    for i in range(m):
        for j in range(n):
            for k in range(min(m, n) // 2 + 1):
                rhombus_sum = get_rhombus_sum(prefix_sum, (i, j), k)
                if rhombus_sum > 0:
                    heapq.heappush(max_heap, -rhombus_sum)
                    if len(max_heap) > 3:
                        heapq.heappop(max_heap)
    
    result = [-heapq.heappop(max_heap) for _ in range(len(max_heap))]
    return sorted(result, reverse=True)

Solution = create_solution(get_biggest_three)