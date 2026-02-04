# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2506
标题: Minimize Maximum Value in a Grid
难度: hard
链接: https://leetcode.cn/problems/minimize-maximum-value-in-a-grid/
题目类型: 并查集、图、拓扑排序、数组、矩阵、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2371. 最小化网格中的最大值 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找和并查集来最小化网格中的最大值。

算法步骤:
1. 定义一个辅助函数 `can_form_grid`，用于判断在给定的最大值限制下，是否可以形成一个连通的网格。
2. 使用二分查找来确定最小的最大值。初始范围为网格中的最小值到最大值。
3. 在每次二分查找中，使用并查集来检查当前中间值是否可以形成连通的网格。
4. 如果可以，则缩小右边界；否则，增大左边界。
5. 最终返回左边界作为结果。

关键点:
- 使用二分查找来最小化最大值。
- 使用并查集来检查连通性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m * log(max_val - min_val))，其中 n 和 m 是网格的行数和列数，max_val 和 min_val 分别是网格中的最大值和最小值。
空间复杂度: O(n * m)，并查集需要存储每个节点的父节点信息。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.union_find import UnionFind

def can_form_grid(grid: List[List[int]], limit: int) -> bool:
    n, m = len(grid), len(grid[0])
    uf = UnionFind(n * m)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] > limit:
                continue
            index = i * m + j
            if i > 0 and grid[i - 1][j] <= limit:
                uf.union(index, (i - 1) * m + j)
            if j > 0 and grid[i][j - 1] <= limit:
                uf.union(index, i * m + (j - 1))
    
    # 检查所有可达的节点是否在一个连通块中
    root = uf.find(0)
    for i in range(n):
        for j in range(m):
            if grid[i][j] <= limit and uf.find(i * m + j) != root:
                return False
    return True

def solution_function_name(grid: List[List[int]]) -> int:
    """
    函数式接口 - 实现最小化网格中的最大值
    """
    n, m = len(grid), len(grid[0])
    min_val = min(min(row) for row in grid)
    max_val = max(max(row) for row in grid)
    
    left, right = min_val, max_val
    while left < right:
        mid = (left + right) // 2
        if can_form_grid(grid, mid):
            right = mid
        else:
            left = mid + 1
    
    return left

Solution = create_solution(solution_function_name)