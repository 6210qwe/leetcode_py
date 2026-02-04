# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3031
标题: Construct Product Matrix
难度: medium
链接: https://leetcode.cn/problems/construct-product-matrix/
题目类型: 数组、矩阵、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2906. 构造乘积矩阵 - 给你一个下标从 0 开始、大小为 n * m 的二维整数矩阵 grid ，定义一个下标从 0 开始、大小为 n * m 的的二维矩阵 p。如果满足以下条件，则称 p 为 grid 的 乘积矩阵 ： * 对于每个元素 p[i][j] ，它的值等于除了 grid[i][j] 外所有元素的乘积。乘积对 12345 取余数。 返回 grid 的乘积矩阵。 示例 1： 输入：grid = [[1,2],[3,4]] 输出：[[24,12],[8,6]] 解释：p[0][0] = grid[0][1] * grid[1][0] * grid[1][1] = 2 * 3 * 4 = 24 p[0][1] = grid[0][0] * grid[1][0] * grid[1][1] = 1 * 3 * 4 = 12 p[1][0] = grid[0][0] * grid[0][1] * grid[1][1] = 1 * 2 * 4 = 8 p[1][1] = grid[0][0] * grid[0][1] * grid[1][0] = 1 * 2 * 3 = 6 所以答案是 [[24,12],[8,6]] 。 示例 2： 输入：grid = [[12345],[2],[1]] 输出：[[2],[0],[0]] 解释：p[0][0] = grid[0][1] * grid[0][2] = 2 * 1 = 2 p[0][1] = grid[0][0] * grid[0][2] = 12345 * 1 = 12345. 12345 % 12345 = 0 ，所以 p[0][1] = 0 p[0][2] = grid[0][0] * grid[0][1] = 12345 * 2 = 24690. 24690 % 12345 = 0 ，所以 p[0][2] = 0 所以答案是 [[2],[0],[0]] 。 提示： * 1 <= n == grid.length <= 105 * 1 <= m == grid[i].length <= 105 * 2 <= n * m <= 105 * 1 <= grid[i][j] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀积和后缀积来计算每个元素的乘积矩阵。

算法步骤:
1. 计算前缀积数组 prefix 和后缀积数组 suffix。
2. 对于每个元素 grid[i][j]，其乘积为 prefix[i][j] * suffix[i][j]。
3. 将结果对 12345 取余数。

关键点:
- 使用前缀积和后缀积可以避免重复计算，提高效率。
- 通过取模操作确保结果在合理范围内。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)
空间复杂度: O(n * m)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def construct_product_matrix(grid: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 构造乘积矩阵
    """
    n, m = len(grid), len(grid[0])
    MOD = 12345
    
    # 计算前缀积
    prefix = [[1] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i > 0:
                prefix[i][j] = (prefix[i-1][m-1] * grid[i-1][m-1]) % MOD
            if j > 0:
                prefix[i][j] = (prefix[i][j-1] * grid[i][j-1]) % MOD
    
    # 计算后缀积
    suffix = [[1] * m for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i < n-1:
                suffix[i][j] = (suffix[i+1][0] * grid[i+1][0]) % MOD
            if j < m-1:
                suffix[i][j] = (suffix[i][j+1] * grid[i][j+1]) % MOD
    
    # 计算乘积矩阵
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = (prefix[i][j] * suffix[i][j]) % MOD
    
    return result


Solution = create_solution(construct_product_matrix)