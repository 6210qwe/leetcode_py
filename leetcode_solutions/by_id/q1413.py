# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1413
标题: Maximum Side Length of a Square with Sum Less than or Equal to Threshold
难度: medium
链接: https://leetcode.cn/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
题目类型: 数组、二分查找、矩阵、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1292. 元素和小于等于阈值的正方形的最大边长 - 给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。 请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/12/15/e1.png] 输入：mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4 输出：2 解释：总和小于或等于 4 的正方形的最大边长为 2，如图所示。 示例 2： 输入：mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1 输出：0 提示： * m == mat.length * n == mat[i].length * 1 <= m, n <= 300 * 0 <= mat[i][j] <= 104 * 0 <= threshold <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二维前缀和来快速计算任意子矩阵的和，并结合二分查找来找到满足条件的最大边长。

算法步骤:
1. 计算二维前缀和数组。
2. 使用二分查找来确定最大边长。
3. 对于每个可能的边长，检查是否存在一个正方形区域的和小于等于阈值。

关键点:
- 二维前缀和可以快速计算任意子矩阵的和。
- 二分查找用于高效地确定最大边长。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * log(min(m, n)))，其中 m 和 n 分别是矩阵的行数和列数。
空间复杂度: O(m * n)，用于存储前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_side_length(mat: List[List[int]], threshold: int) -> int:
    """
    返回元素总和小于或等于阈值的正方形区域的最大边长。
    """
    if not mat or not mat[0]:
        return 0

    m, n = len(mat), len(mat[0])
    prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

    # 计算二维前缀和
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix_sum[i][j] = mat[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

    # 检查是否存在一个边长为 side 的正方形区域，其和小于等于阈值
    def is_valid(side: int) -> bool:
        for i in range(side, m + 1):
            for j in range(side, n + 1):
                if (prefix_sum[i][j] - prefix_sum[i - side][j] - prefix_sum[i][j - side] + prefix_sum[i - side][j - side]) <= threshold:
                    return True
        return False

    # 二分查找最大边长
    left, right = 0, min(m, n)
    while left < right:
        mid = (left + right + 1) // 2
        if is_valid(mid):
            left = mid
        else:
            right = mid - 1

    return left


Solution = create_solution(max_side_length)