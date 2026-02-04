# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000308
标题: 矩阵中的最长递增路径
难度: hard
链接: https://leetcode.cn/problems/fpTFWP/
题目类型: 深度优先搜索、广度优先搜索、图、拓扑排序、记忆化搜索、数组、动态规划、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 112. 矩阵中的最长递增路径 - 给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。 对于每个单元格，你可以往上，下，左，右四个方向移动。 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。 示例 1： [https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg] 输入：matrix = [[9,9,4],[6,6,8],[2,1,1]] 输出：4 解释：最长递增路径为 [1, 2, 6, 9]。 示例 2： [https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg] 输入：matrix = [[3,4,5],[3,2,6],[2,2,1]] 输出：4 解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。 示例 3： 输入：matrix = [[1]] 输出：1 提示： * m == matrix.length * n == matrix[i].length * 1 <= m, n <= 200 * 0 <= matrix[i][j] <= 231 - 1 注意：本题与主站 329 题相同： https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/ [https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 并结合记忆化搜索 (Memoization) 来避免重复计算。

算法步骤:
1. 初始化一个二维数组 dp，用于存储从每个单元格开始的最长递增路径长度。
2. 定义一个递归函数 dfs(i, j)，表示从位置 (i, j) 开始的最长递增路径长度。
3. 在 dfs 函数中，如果 dp[i][j] 已经计算过，则直接返回 dp[i][j]。
4. 否则，遍历当前位置的四个方向，如果下一个位置的值大于当前值，则递归调用 dfs 函数，并更新 dp[i][j]。
5. 最后，遍历整个矩阵，找到最长的递增路径长度。

关键点:
- 使用记忆化搜索来避免重复计算，从而提高效率。
- 通过递归和回溯来找到每个单元格的最长递增路径。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是矩阵的行数和列数。每个单元格最多只会被访问一次。
空间复杂度: O(m * n)，用于存储 dp 数组和递归调用栈。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def longest_increasing_path(matrix: List[List[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    
    def dfs(i, j):
        if dp[i][j] != 0:
            return dp[i][j]
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_length = 1
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                length = 1 + dfs(ni, nj)
                max_length = max(max_length, length)
        
        dp[i][j] = max_length
        return max_length
    
    max_path = 0
    for i in range(m):
        for j in range(n):
            max_path = max(max_path, dfs(i, j))
    
    return max_path

Solution = create_solution(longest_increasing_path)