# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1711
标题: Find Valid Matrix Given Row and Column Sums
难度: medium
链接: https://leetcode.cn/problems/find-valid-matrix-given-row-and-column-sums/
题目类型: 贪心、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1605. 给定行和列的和求可行矩阵 - 给你两个非负整数数组 rowSum 和 colSum ，其中 rowSum[i] 是二维矩阵中第 i 行元素的和， colSum[j] 是第 j 列元素的和。换言之你不知道矩阵里的每个元素，但是你知道每一行和每一列的和。 请找到大小为 rowSum.length x colSum.length 的任意 非负整数 矩阵，且该矩阵满足 rowSum 和 colSum 的要求。 请你返回任意一个满足题目要求的二维矩阵，题目保证存在 至少一个 可行矩阵。 示例 1： 输入：rowSum = [3,8], colSum = [4,7] 输出：[[3,0], [1,7]] 解释： 第 0 行：3 + 0 = 3 == rowSum[0] 第 1 行：1 + 7 = 8 == rowSum[1] 第 0 列：3 + 1 = 4 == colSum[0] 第 1 列：0 + 7 = 7 == colSum[1] 行和列的和都满足题目要求，且所有矩阵元素都是非负的。 另一个可行的矩阵为：[[1,2], [3,5]] 示例 2： 输入：rowSum = [5,7,10], colSum = [8,6,8] 输出：[[0,5,0], [6,1,0], [2,0,8]] 示例 3： 输入：rowSum = [14,9], colSum = [6,9,8] 输出：[[0,9,5], [6,0,3]] 示例 4： 输入：rowSum = [1,0], colSum = [1] 输出：[[1], [0]] 示例 5： 输入：rowSum = [0], colSum = [0] 输出：[[0]] 提示： * 1 <= rowSum.length, colSum.length <= 500 * 0 <= rowSum[i], colSum[i] <= 108 * sum(rowSum) == sum(colSum)
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，从左上角开始逐个填充矩阵，每次取当前行和列的最小值作为当前元素，并更新剩余的行和列的和。

算法步骤:
1. 初始化一个全零矩阵。
2. 从左上角开始遍历矩阵，对于每个位置 (i, j)，取 rowSum[i] 和 colSum[j] 的最小值作为当前元素。
3. 更新 rowSum[i] 和 colSum[j]，减去当前元素的值。
4. 重复步骤 2 和 3，直到遍历完整个矩阵。

关键点:
- 每次取当前行和列的最小值，确保不会超过行和列的和。
- 逐步更新行和列的和，确保最终结果满足条件。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 是 rowSum 的长度，n 是 colSum 的长度。
空间复杂度: O(m * n)，用于存储结果矩阵。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(rowSum: List[int], colSum: List[int]) -> List[List[int]]:
    """
    函数式接口 - 返回满足 rowSum 和 colSum 的非负整数矩阵
    """
    m, n = len(rowSum), len(colSum)
    matrix = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            value = min(rowSum[i], colSum[j])
            matrix[i][j] = value
            rowSum[i] -= value
            colSum[j] -= value
    
    return matrix


Solution = create_solution(solution_function_name)