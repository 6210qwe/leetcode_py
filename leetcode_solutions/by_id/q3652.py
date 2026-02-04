# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3652
标题: Find Sorted Submatrices With Maximum Element at Most K
难度: hard
链接: https://leetcode.cn/problems/find-sorted-submatrices-with-maximum-element-at-most-k/
题目类型: 栈、数组、矩阵、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3359. 查找最大元素不超过 K 的有序子矩阵 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用单调栈来找到每一行中每个元素作为最大值的子矩阵范围。

算法步骤:
1. 对于每一行，使用单调栈找到每个元素作为最大值的左右边界。
2. 对于每一列，使用单调栈找到每个元素作为最大值的上下边界。
3. 通过上述边界信息，计算每个元素作为最大值的子矩阵数量，并检查其是否小于等于 K。

关键点:
- 使用单调栈可以在线性时间内找到每个元素的左右/上下边界。
- 通过遍历所有可能的子矩阵，统计满足条件的子矩阵数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 和 n 分别是矩阵的行数和列数。每行和每列的处理都是线性的。
空间复杂度: O(m + n)，用于存储每一行和每一列的边界信息。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def count_submatrices(matrix: List[List[int]], k: int) -> int:
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    left_bound, right_bound = [0] * n, [n] * n
    top_bound, bottom_bound = [0] * m, [m] * m
    result = 0
    
    # 计算每一行的左右边界
    for i in range(m):
        stack = []
        for j in range(n):
            while stack and matrix[i][stack[-1]] > matrix[i][j]:
                right_bound[stack.pop()] = j
            if stack:
                left_bound[j] = stack[-1] + 1
            stack.append(j)
    
    # 计算每一列的上下边界
    for j in range(n):
        stack = []
        for i in range(m):
            while stack and matrix[stack[-1]][j] > matrix[i][j]:
                bottom_bound[stack.pop()] = i
            if stack:
                top_bound[i] = stack[-1] + 1
            stack.append(i)
    
    # 统计满足条件的子矩阵数量
    for i in range(m):
        for j in range(n):
            if matrix[i][j] <= k:
                result += (i - top_bound[i] + 1) * (bottom_bound[i] - i) * (j - left_bound[j] + 1) * (right_bound[j] - j)
    
    return result

Solution = create_solution(count_submatrices)