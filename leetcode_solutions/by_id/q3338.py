# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3338
标题: Count Submatrices with Top-Left Element and Sum Less Than k
难度: medium
链接: https://leetcode.cn/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/
题目类型: 数组、矩阵、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3070. 元素和小于等于 k 的子矩阵的数目 - 给你一个下标从 0 开始的整数矩阵 grid 和一个整数 k。 返回包含 grid 左上角元素、元素和小于或等于 k 的 子矩阵的数目。 示例 1： [https://assets.leetcode.com/uploads/2024/01/01/example1.png] 输入：grid = [[7,6,3],[6,6,1]], k = 18 输出：4 解释：如上图所示，只有 4 个子矩阵满足：包含 grid 的左上角元素，并且元素和小于或等于 18 。 示例 2： [https://assets.leetcode.com/uploads/2024/01/01/example21.png] 输入：grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20 输出：6 解释：如上图所示，只有 6 个子矩阵满足：包含 grid 的左上角元素，并且元素和小于或等于 20 。 提示： * m == grid.length * n == grid[i].length * 1 <= n, m <= 1000 * 0 <= grid[i][j] <= 1000 * 1 <= k <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二维前缀和来快速计算任意子矩阵的和。

算法步骤:
1. 计算二维前缀和数组。
2. 遍历所有可能的右下角位置，使用前缀和数组计算子矩阵的和。
3. 如果子矩阵的和小于或等于 k，则计数器加一。

关键点:
- 使用二维前缀和可以将子矩阵和的计算时间复杂度降低到 O(1)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是矩阵的行数和列数。
空间复杂度: O(m * n)，用于存储二维前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_submatrices_with_sum_less_than_k(grid: List[List[int]], k: int) -> int:
    """
    函数式接口 - 计算元素和小于等于 k 的子矩阵的数目
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

    # 计算二维前缀和
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix_sum[i][j] = grid[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

    count = 0
    # 遍历所有可能的右下角位置
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            submatrix_sum = prefix_sum[i][j]
            if submatrix_sum <= k:
                count += 1

    return count


Solution = create_solution(count_submatrices_with_sum_less_than_k)