# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 308
标题: Range Sum Query 2D - Mutable
难度: medium
链接: https://leetcode.cn/problems/range-sum-query-2d-mutable/
题目类型: 设计、树状数组、线段树、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
308. 二维区域和检索 - 矩阵可修改 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二维树状数组（Binary Indexed Tree）实现二维区间和查询和单点更新

算法步骤:
1. 使用二维树状数组维护二维前缀和
2. update: 更新树状数组
3. sumRegion: 使用二维前缀和计算矩形区域和

关键点:
- 使用二维树状数组实现O(logm*logn)更新和查询
- 时间复杂度：初始化O(mn)，更新和查询O(logm*logn)，空间复杂度O(mn)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 初始化O(mn)，更新和查询O(logm*logn)
空间复杂度: O(mn) - 树状数组空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


class NumMatrix:
    """
    二维区域和检索 - 矩阵可修改（使用二维树状数组）
    """
    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0]) if matrix else 0
        self.matrix = [[0] * self.n for _ in range(self.m)]
        self.tree = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        
        # 初始化树状数组
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])
    
    def _lowbit(self, x: int) -> int:
        """返回x的二进制表示中最低位的1所对应的值"""
        return x & -x
    
    def _update(self, row: int, col: int, delta: int):
        """更新树状数组"""
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.tree[i][j] += delta
                j += self._lowbit(j)
            i += self._lowbit(i)
    
    def _query(self, row: int, col: int) -> int:
        """查询从(0,0)到(row,col)的矩形区域和"""
        total = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                total += self.tree[i][j]
                j -= self._lowbit(j)
            i -= self._lowbit(i)
        return total
    
    def update(self, row: int, col: int, val: int) -> None:
        """更新矩阵元素"""
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self._update(row, col, delta)
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """返回[row1, col1]到[row2, col2]的矩形区域和"""
        return (
            self._query(row2, col2) -
            self._query(row1 - 1, col2) -
            self._query(row2, col1 - 1) +
            self._query(row1 - 1, col1 - 1)
        )


def range_sum_query_2d_mutable(matrix: List[List[int]]) -> NumMatrix:
    """
    函数式接口 - 创建二维区域和检索对象（可修改）
    
    实现思路:
    使用二维树状数组实现二维区间和查询和单点更新。
    
    Args:
        matrix: 二维整数矩阵
        
    Returns:
        NumMatrix实例
        
    Example:
        >>> numMatrix = range_sum_query_2d_mutable([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
        >>> numMatrix.sumRegion(2, 1, 4, 3)
        8
    """
    return NumMatrix(matrix)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(range_sum_query_2d_mutable)
