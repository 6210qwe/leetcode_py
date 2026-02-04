# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3251
标题: Maximum Area of Longest Diagonal Rectangle
难度: easy
链接: https://leetcode.cn/problems/maximum-area-of-longest-diagonal-rectangle/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3000. 对角线最长的矩形的面积 - 给你一个下标从 0 开始的二维整数数组 dimensions。 对于所有下标 i（0 <= i < dimensions.length），dimensions[i][0] 表示矩形 i 的长度，而 dimensions[i][1] 表示矩形 i 的宽度。 返回对角线最 长 的矩形的 面积 。如果存在多个对角线长度相同的矩形，返回其中面积最 大 的矩形的面积。 示例 1： 输入：dimensions = [[9,3],[8,6]] 输出：48 解释： 下标 = 0，长度 = 9，宽度 = 3。对角线长度 = sqrt(9 * 9 + 3 * 3) = sqrt(90) ≈ 9.487。 下标 = 1，长度 = 8，宽度 = 6。对角线长度 = sqrt(8 * 8 + 6 * 6) = sqrt(100) = 10。 因此，下标为 1 的矩形对角线更长，所以返回面积 = 8 * 6 = 48。 示例 2： 输入：dimensions = [[3,4],[4,3]] 输出：12 解释：两个矩形的对角线长度相同，为 5，所以最大面积 = 12。 提示： * 1 <= dimensions.length <= 100 * dimensions[i].length == 2 * 1 <= dimensions[i][0], dimensions[i][1] <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 计算每个矩形的对角线长度，并找到对角线最长且面积最大的矩形。

算法步骤:
1. 初始化变量 `max_diagonal` 和 `max_area` 分别记录当前最长的对角线长度和对应的矩形面积。
2. 遍历每个矩形，计算其对角线长度和面积。
3. 如果当前矩形的对角线长度大于 `max_diagonal`，更新 `max_diagonal` 和 `max_area`。
4. 如果当前矩形的对角线长度等于 `max_diagonal` 但面积更大，更新 `max_area`。
5. 返回 `max_area`。

关键点:
- 使用勾股定理计算对角线长度。
- 通过一次遍历找到对角线最长且面积最大的矩形。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 dimensions 的长度。我们只需要遍历一次数组。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(dimensions: List[List[int]]) -> int:
    """
    函数式接口 - 计算对角线最长的矩形的面积
    """
    max_diagonal = 0
    max_area = 0
    
    for length, width in dimensions:
        diagonal = (length ** 2 + width ** 2) ** 0.5
        area = length * width
        
        if diagonal > max_diagonal or (diagonal == max_diagonal and area > max_area):
            max_diagonal = diagonal
            max_area = area
    
    return max_area


Solution = create_solution(solution_function_name)