# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1572
标题: Subrectangle Queries
难度: medium
链接: https://leetcode.cn/problems/subrectangle-queries/
题目类型: 设计、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1476. 子矩形查询 - 请你实现一个类 SubrectangleQueries ，它的构造函数的参数是一个 rows x cols 的矩形（这里用整数矩阵表示），并支持以下两种操作： 1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) * 用 newValue 更新以 (row1,col1) 为左上角且以 (row2,col2) 为右下角的子矩形。 2. getValue(int row, int col) * 返回矩形中坐标 (row,col) 的当前值。 示例 1： 输入： ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"] [[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]] 输出： [null,1,null,5,5,null,10,5] 解释： SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]]); // 初始的 (4x3) 矩形如下： // 1 2 1 // 4 3 4 // 3 2 1 // 1 1 1 subrectangleQueries.getValue(0, 2); // 返回 1 subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5); // 此次更新后矩形变为： // 5 5 5 // 5 5 5 // 5 5 5 // 5 5 5 subrectangleQueries.getValue(0, 2); // 返回 5 subrectangleQueries.getValue(3, 1); // 返回 5 subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10); // 此次更新后矩形变为： // 5 5 5 // 5 5 5 // 5 5 5 // 10 10 10 subrectangleQueries.getValue(3, 1); // 返回 10 subrectangleQueries.getValue(0, 2); // 返回 5 示例 2： 输入： ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"] [[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]] 输出： [null,1,null,100,100,null,20] 解释： SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]]); subrectangleQueries.getValue(0, 0); // 返回 1 subrectangleQueries.updateSubrectangle(0, 0, 2, 2, 100); subrectangleQueries.getValue(0, 0); // 返回 100 subrectangleQueries.getValue(2, 2); // 返回 100 subrectangleQueries.updateSubrectangle(1, 1, 2, 2, 20); subrectangleQueries.getValue(2, 2); // 返回 20 提示： * 最多有 500 次updateSubrectangle 和 getValue 操作。 * 1 <= rows, cols <= 100 * rows == rectangle.length * cols == rectangle[i].length * 0 <= row1 <= row2 < rows * 0 <= col1 <= col2 < cols * 1 <= newValue, rectangle[i][j] <= 10^9 * 0 <= row < rows * 0 <= col < cols
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个列表来存储所有更新操作，每次获取值时从最新的更新操作开始查找。

算法步骤:
1. 初始化时，将给定的矩形存储在类变量中。
2. 在 updateSubrectangle 方法中，将更新操作存储在一个列表中。
3. 在 getValue 方法中，从最新的更新操作开始查找，如果找到则返回新值，否则返回初始矩形中的值。

关键点:
- 使用列表存储更新操作，避免每次都修改整个矩形。
- 从最新的更新操作开始查找，确保获取到的是最新的值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) for getValue, O(1) for updateSubrectangle
空间复杂度: O(n) where n is the number of update operations
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.updates = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.updates.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        for row1, col1, row2, col2, newValue in reversed(self.updates):
            if row1 <= row <= row2 and col1 <= col <= col2:
                return newValue
        return self.rectangle[row][col]

# Example usage
# subrectangleQueries = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
# subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5)
# print(subrectangleQueries.getValue(0, 2))  # Output: 5
# subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10)
# print(subrectangleQueries.getValue(3, 1))  # Output: 10
# print(subrectangleQueries.getValue(0, 2))  # Output: 5

# Utility function to create a solution instance
def create_solution(rectangle: List[List[int]]) -> SubrectangleQueries:
    return SubrectangleQueries(rectangle)

# Example usage with the utility function
# subrectangleQueries = create_solution([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
# subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5)
# print(subrectangleQueries.getValue(0, 2))  # Output: 5
# subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10)
# print(subrectangleQueries.getValue(3, 1))  # Output: 10
# print(subrectangleQueries.getValue(0, 2))  # Output: 5