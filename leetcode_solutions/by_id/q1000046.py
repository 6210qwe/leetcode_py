# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000046
标题: Max Submatrix LCCI
难度: hard
链接: https://leetcode.cn/problems/max-submatrix-lcci/
题目类型: 数组、动态规划、矩阵、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 17.24. 最大子矩阵 - 给定一个正整数、负整数和 0 组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。 返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，r2, c2 分别代表右下角的行号和列号。若有多个满足条件的子矩阵，返回任意一个均可。 注意：本题相对书上原题稍作改动 示例： 输入： [ [-1,0], [0,-1] ] 输出：[0,1,0,1] 解释：输入中标粗的元素即为输出所表示的矩阵 说明： * 1 <= matrix.length, matrix[0].length <= 200
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Kadane's 算法来解决一维最大子数组和问题，并将其扩展到二维矩阵。

算法步骤:
1. 对于每一行，计算从该行开始的所有可能的高度累加数组。
2. 对于每个高度累加数组，使用 Kadane's 算法找到最大子数组和及其起始和结束位置。
3. 记录所有子矩阵中的最大和及其对应的坐标。

关键点:
- 将二维问题转化为多个一维问题，通过逐行累加高度来构建新的数组。
- 使用 Kadane's 算法高效地找到一维数组中的最大子数组和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(N^2 * M)，其中 N 是矩阵的行数，M 是矩阵的列数。
空间复杂度: O(M)，用于存储高度累加数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_submatrix(matrix: List[List[int]]) -> List[int]:
    """
    函数式接口 - 找出元素总和最大的子矩阵
    """
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    max_sum = float('-inf')
    result = [0, 0, 0, 0]

    for top in range(rows):
        height = [0] * cols
        for bottom in range(top, rows):
            for col in range(cols):
                height[col] += matrix[bottom][col]
            
            # 使用 Kadane's 算法找到当前高度累加数组的最大子数组和
            current_sum = 0
            left = 0
            for right in range(cols):
                if current_sum <= 0:
                    current_sum = height[right]
                    left = right
                else:
                    current_sum += height[right]
                
                if current_sum > max_sum:
                    max_sum = current_sum
                    result = [top, left, bottom, right]

    return result


Solution = create_solution(max_submatrix)