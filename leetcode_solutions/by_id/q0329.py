# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 329
标题: Longest Increasing Path in a Matrix
难度: hard
链接: https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/
题目类型: 深度优先搜索、广度优先搜索、图、拓扑排序、记忆化搜索、数组、动态规划、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
329. 矩阵中的最长递增路径 - 给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。 对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。 示例 1： [https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg] 输入：matrix = [[9,9,4],[6,6,8],[2,1,1]] 输出：4 解释：最长递增路径为 [1, 2, 6, 9]。 示例 2： [https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg] 输入：matrix = [[3,4,5],[3,2,6],[2,2,1]] 输出：4 解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。 示例 3： 输入：matrix = [[1]] 输出：1 提示： * m == matrix.length * n == matrix[i].length * 1 <= m, n <= 200 * 0 <= matrix[i][j] <= 231 - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 记忆化DFS，对每个位置计算最长递增路径

算法步骤:
1. 对每个位置，DFS搜索四个方向
2. 如果下一个位置值更大，递归计算
3. 使用记忆化避免重复计算

关键点:
- 记忆化DFS
- 时间复杂度O(m*n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m*n) - 每个位置访问一次
空间复杂度: O(m*n) - 记忆化数组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def longest_increasing_path(matrix: List[List[int]]) -> int:
    """
    函数式接口 - 矩阵中的最长递增路径
    
    实现思路:
    记忆化DFS：对每个位置计算最长递增路径。
    
    Args:
        matrix: 整数矩阵
        
    Returns:
        最长递增路径长度
        
    Example:
        >>> longest_increasing_path([[9,9,4],[6,6,8],[2,1,1]])
        4
    """
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    memo = [[0] * n for _ in range(m)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(i: int, j: int) -> int:
        """DFS计算最长路径"""
        if memo[i][j] > 0:
            return memo[i][j]
        
        max_path = 1
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                max_path = max(max_path, 1 + dfs(ni, nj))
        
        memo[i][j] = max_path
        return max_path
    
    result = 0
    for i in range(m):
        for j in range(n):
            result = max(result, dfs(i, j))
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(longest_increasing_path)
