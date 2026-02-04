# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100185
标题: Rotate Matrix LCCI
难度: medium
链接: https://leetcode.cn/problems/rotate-matrix-lcci/
题目类型: 数组、数学、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 01.07. 旋转矩阵 - 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。 不占用额外内存空间能否做到？ 示例 1： 给定 matrix = [ [1,2,3], [4,5,6], [7,8,9] ], 原地旋转输入矩阵，使其变为: [ [7,4,1], [8,5,2], [9,6,3] ] 示例 2： 给定 matrix = [ [ 5, 1, 9,11], [ 2, 4, 8,10], [13, 3, 6, 7], [15,14,12,16] ], 原地旋转输入矩阵，使其变为: [ [15,13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7,10,11] ] 注意：本题与主站 48 题相同：https://leetcode.cn/problems/rotate-image/ [https://leetcode.cn/problems/rotate-image/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过逐层旋转来实现矩阵的 90 度旋转。

算法步骤:
1. 将矩阵分为多个层次，从外层到内层逐层旋转。
2. 对于每一层，使用四个指针（top, bottom, left, right）来控制旋转范围。
3. 在每一层中，依次交换四个角的元素，然后向内移动一层继续旋转。

关键点:
- 通过逐层旋转和四角交换，可以在 O(1) 的额外空间内完成旋转。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(N^2)，其中 N 是矩阵的边长，因为每个元素都需要访问一次。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def rotate_matrix(matrix: List[List[int]]) -> None:
    """
    函数式接口 - 旋转矩阵
    """
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # Save the top element
            top = matrix[layer][i]
            
            # Move left element to top
            matrix[layer][i] = matrix[-i - 1][layer]
            
            # Move bottom element to left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            
            # Move right element to bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
            
            # Move top element to right
            matrix[i][-layer - 1] = top

Solution = create_solution(rotate_matrix)