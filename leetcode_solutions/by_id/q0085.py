# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 85
标题: Maximal Rectangle
难度: hard
链接: https://leetcode.cn/problems/maximal-rectangle/
题目类型: 栈、数组、动态规划、矩阵、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
85. 最大矩形 - 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。 示例 1： [https://pic.leetcode.cn/1722912576-boIxpm-image.png] 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]] 输出：6 解释：最大矩形如上图所示。 示例 2： 输入：matrix = [["0"]] 输出：0 示例 3： 输入：matrix = [["1"]] 输出：1 提示： * rows == matrix.length * cols == matrix[0].length * 1 <= rows, cols <= 200 * matrix[i][j] 为 '0' 或 '1'
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 将问题转化为84题，对每一行计算最大矩形面积

算法步骤:
1. 计算每行的高度数组heights（连续1的个数）
2. 对于每一行，使用84题的单调栈方法计算最大矩形面积
3. 返回所有行中的最大面积

关键点:
- 将二维问题转化为一维问题
- 每行的高度 = 从该行向上连续1的个数
- 时间复杂度O(m*n)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m*n) - 需要遍历矩阵并计算每行的最大矩形
空间复杂度: O(n) - 存储高度数组和栈
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def maximal_rectangle(matrix: List[List[str]]) -> int:
    """
    函数式接口 - 转化为84题
    
    实现思路:
    将问题转化为84题，对每一行计算最大矩形面积。
    
    Args:
        matrix: 仅包含'0'和'1'的二维二进制矩阵
        
    Returns:
        只包含'1'的最大矩形的面积
        
    Example:
        >>> maximal_rectangle([["1","0","1","0","0"],["1","0","1","1","1"]])
        3
    """
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    max_area = 0
    
    for i in range(m):
        # 更新高度数组
        for j in range(n):
            if matrix[i][j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0
        
        # 使用单调栈计算当前行的最大矩形面积
        heights_with_padding = [0] + heights + [0]
        stack = []
        
        for k in range(len(heights_with_padding)):
            while stack and heights_with_padding[k] < heights_with_padding[stack[-1]]:
                h = heights_with_padding[stack.pop()]
                width = k - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(k)
    
    return max_area


# 自动生成Solution类（无需手动编写）
Solution = create_solution(maximal_rectangle)
