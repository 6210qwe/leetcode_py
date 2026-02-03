# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 407
标题: Trapping Rain Water II
难度: hard
链接: https://leetcode.cn/problems/trapping-rain-water-ii/
题目类型: 广度优先搜索、数组、矩阵、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
407. 接雨水 II - 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。 示例 1: [https://assets.leetcode.com/uploads/2021/04/08/trap1-3d.jpg] 输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] 输出: 4 解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。 示例 2: [https://assets.leetcode.com/uploads/2021/04/08/trap2-3d.jpg] 输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]] 输出: 10 提示: * m == heightMap.length * n == heightMap[i].length * 1 <= m, n <= 200 * 0 <= heightMap[i][j] <= 2 * 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用优先队列（最小堆），从边界开始向内扩展，维护当前边界的最小高度

算法步骤:
1. 将边界所有点加入优先队列
2. 使用BFS从边界向内扩展
3. 对于每个访问的点，如果高度小于当前边界最小高度，可以接雨水
4. 更新边界，继续扩展

关键点:
- 使用优先队列维护边界最小高度
- 时间复杂度O(mn*log(mn))，空间复杂度O(mn)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(mn*log(mn)) - m和n分别是矩阵的行数和列数
空间复杂度: O(mn) - 优先队列和访问标记的空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq
from leetcode_solutions.utils.solution import create_solution


def trapping_rain_water_ii(heightMap: List[List[int]]) -> int:
    """
    函数式接口 - 接雨水II
    
    实现思路:
    使用优先队列（最小堆），从边界开始向内扩展，维护当前边界的最小高度。
    
    Args:
        heightMap: 二维高度图
        
    Returns:
        能接的雨水体积
        
    Example:
        >>> trapping_rain_water_ii([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])
        4
    """
    if not heightMap or not heightMap[0]:
        return 0
    
    m, n = len(heightMap), len(heightMap[0])
    if m < 3 or n < 3:
        return 0
    
    visited = [[False] * n for _ in range(m)]
    heap = []
    
    # 将边界加入优先队列
    for i in range(m):
        heapq.heappush(heap, (heightMap[i][0], i, 0))
        heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
        visited[i][0] = True
        visited[i][n-1] = True
    
    for j in range(1, n-1):
        heapq.heappush(heap, (heightMap[0][j], 0, j))
        heapq.heappush(heap, (heightMap[m-1][j], m-1, j))
        visited[0][j] = True
        visited[m-1][j] = True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = 0
    max_height = 0
    
    while heap:
        height, i, j = heapq.heappop(heap)
        max_height = max(max_height, height)
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                visited[ni][nj] = True
                if heightMap[ni][nj] < max_height:
                    result += max_height - heightMap[ni][nj]
                heapq.heappush(heap, (heightMap[ni][nj], ni, nj))
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(trapping_rain_water_ii)
