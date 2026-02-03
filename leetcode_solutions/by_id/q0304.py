# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 304
标题: Range Sum Query 2D - Immutable
难度: medium
链接: https://leetcode.cn/problems/range-sum-query-2d-immutable/
题目类型: 设计、数组、矩阵、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
304. 二维区域和检索 - 矩阵不可变 - 给定一个二维矩阵 matrix，以下类型的多个请求： * 计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1, col1) ，右下角 为 (row2, col2) 。 实现 NumMatrix 类： * NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化 * int sumRegion(int row1, int col1, int row2, int col2) 返回 左上角 (row1, col1) 、右下角 (row2, col2) 所描述的子矩阵的元素 总和 。 示例 1： [https://pic.leetcode.cn/1626332422-wUpUHT-image.png] 输入: ["NumMatrix","sumRegion","sumRegion","sumRegion"] [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]] 输出: [null, 8, 11, 12] 解释: NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]); numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和) numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和) numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和) 提示： * m == matrix.length * n == matrix[i].length * 1 <= m, n <= 200 * -105 <= matrix[i][j] <= 105 * 0 <= row1 <= row2 < m * 0 <= col1 <= col2 < n * 最多调用 104 次 sumRegion 方法
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二维前缀和，preSum[i][j]表示从(0,0)到(i-1,j-1)的矩形区域和

算法步骤:
1. 初始化时计算二维前缀和数组
2. sumRegion(row1, col1, row2, col2) = preSum[row2+1][col2+1] - preSum[row1][col2+1] - preSum[row2+1][col1] + preSum[row1][col1]

关键点:
- 使用二维前缀和实现O(1)查询
- 时间复杂度：初始化O(mn)，查询O(1)，空间复杂度O(mn)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 初始化O(mn)，查询O(1)
空间复杂度: O(mn) - 前缀和数组空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


class NumMatrix:
    """
    二维区域和检索 - 矩阵不可变
    """
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        self.prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                self.prefix_sum[i + 1][j + 1] = (
                    self.prefix_sum[i][j + 1] +
                    self.prefix_sum[i + 1][j] -
                    self.prefix_sum[i][j] +
                    matrix[i][j]
                )
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """返回[row1, col1]到[row2, col2]的矩形区域和"""
        return (
            self.prefix_sum[row2 + 1][col2 + 1] -
            self.prefix_sum[row1][col2 + 1] -
            self.prefix_sum[row2 + 1][col1] +
            self.prefix_sum[row1][col1]
        )


def range_sum_query_2d_immutable(matrix: List[List[int]]) -> NumMatrix:
    """
    函数式接口 - 创建二维区域和检索对象
    
    实现思路:
    使用二维前缀和，preSum[i][j]表示从(0,0)到(i-1,j-1)的矩形区域和。
    
    Args:
        matrix: 二维整数矩阵
        
    Returns:
        NumMatrix实例
        
    Example:
        >>> numMatrix = range_sum_query_2d_immutable([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
        >>> numMatrix.sumRegion(2, 1, 4, 3)
        8
    """
    return NumMatrix(matrix)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(range_sum_query_2d_immutable)
