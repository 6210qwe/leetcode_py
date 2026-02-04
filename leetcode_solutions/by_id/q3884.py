# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3884
标题: Minimum Absolute Difference in Sliding Submatrix
难度: medium
链接: https://leetcode.cn/problems/minimum-absolute-difference-in-sliding-submatrix/
题目类型: 数组、矩阵、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3567. 子矩阵的最小绝对差 - 给你一个 m x n 的整数矩阵 grid 和一个整数 k。 对于矩阵 grid 中的每个连续的 k x k 子矩阵，计算其中任意两个 不同值 之间的 最小绝对差 。 返回一个大小为 (m - k + 1) x (n - k + 1) 的二维数组 ans，其中 ans[i][j] 表示以 grid 中坐标 (i, j) 为左上角的子矩阵的最小绝对差。 注意：如果子矩阵中的所有元素都相同，则答案为 0。 子矩阵 (x1, y1, x2, y2) 是一个由选择矩阵中所有满足 x1 <= x <= x2 且 y1 <= y <= y2 的单元格 matrix[x][y] 组成的矩阵。 示例 1： 输入： grid = [[1,8],[3,-2]], k = 2 输出： [[2]] 解释： * 只有一个可能的 k x k 子矩阵：[[1, 8], [3, -2]]。 * 子矩阵中的不同值为 [1, 8, 3, -2]。 * 子矩阵中的最小绝对差为 |1 - 3| = 2。因此，答案为 [[2]]。 示例 2： 输入： grid = [[3,-1]], k = 1 输出： [[0,0]] 解释： * 每个 k x k 子矩阵中只有一个不同的元素。 * 因此，答案为 [[0, 0]]。 示例 3： 输入： grid = [[1,-2,3],[2,3,5]], k = 2 输出： [[1,2]] 解释： * 有两个可能的 k × k 子矩阵： * 以 (0, 0) 为起点的子矩阵：[[1, -2], [2, 3]]。 * 子矩阵中的不同值为 [1, -2, 2, 3]。 * 子矩阵中的最小绝对差为 |1 - 2| = 1。 * 以 (0, 1) 为起点的子矩阵：[[-2, 3], [3, 5]]。 * 子矩阵中的不同值为 [-2, 3, 5]。 * 子矩阵中的最小绝对差为 |3 - 5| = 2。 * 因此，答案为 [[1, 2]]。 提示： * 1 <= m == grid.length <= 30 * 1 <= n == grid[i].length <= 30 * -105 <= grid[i][j] <= 105 * 1 <= k <= min(m, n)
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和有序集合来维护子矩阵中的元素，并计算最小绝对差。

算法步骤:
1. 初始化结果矩阵 `ans`。
2. 使用滑动窗口遍历每一行，维护当前窗口内的元素。
3. 对于每一行的窗口，使用有序集合来维护当前窗口内的元素，并计算最小绝对差。
4. 更新结果矩阵 `ans`。

关键点:
- 使用有序集合来高效地维护窗口内的元素及其顺序。
- 滑动窗口技术可以避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * log(k))
空间复杂度: O(k^2)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from sortedcontainers import SortedList

def min_abs_diff_in_sliding_submatrix(grid: List[List[int]], k: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    ans = [[float('inf')] * (n - k + 1) for _ in range(m - k + 1)]
    
    def get_min_diff(window):
        min_diff = float('inf')
        for i in range(1, len(window)):
            min_diff = min(min_diff, window[i] - window[i - 1])
        return min_diff if min_diff != float('inf') else 0
    
    for i in range(m - k + 1):
        window = [SortedList() for _ in range(n)]
        for j in range(i, i + k):
            for col in range(n):
                window[col].add(grid[j][col])
        
        for j in range(n - k + 1):
            current_window = SortedList()
            for col in range(j, j + k):
                current_window.update(window[col])
            ans[i][j] = get_min_diff(current_window)
            
            if j < n - k:
                for col in range(j, j + k):
                    window[col].remove(grid[i][col])
                    window[col].add(grid[i + k][col])
    
    return ans

Solution = create_solution(min_abs_diff_in_sliding_submatrix)