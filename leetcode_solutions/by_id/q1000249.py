# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000249
标题: 二维区域和检索 - 矩阵不可变
难度: medium
链接: https://leetcode.cn/problems/O4NDxx/
题目类型: 设计、数组、矩阵、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 013. 二维区域和检索 - 矩阵不可变 - 给定一个二维矩阵 matrix，以下类型的多个请求： * 计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。 实现 NumMatrix 类： * NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化 * int sumRegion(int row1, int col1, int row2, int col2) 返回左上角 (row1, col1) 、右下角 (row2, col2) 的子矩阵的元素总和。 示例 1： [https://pic.leetcode.cn/1626332422-wUpUHT-image.png] 输入: ["NumMatrix","sumRegion","sumRegion","sumRegion"] [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]] 输出: [null, 8, 11, 12] 解释: NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]]); numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和) numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和) numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和) 提示： * m == matrix.length * n == matrix[i].length * 1 <= m, n <= 200 * -105 <= matrix[i][j] <= 105 * 0 <= row1 <= row2 < m * 0 <= col1 <= col2 < n * 最多调用 104 次 sumRegion 方法 注意：本题与主站 304 题相同： https://leetcode.cn/problems/range-sum-query-2d-immutable/ [https://leetcode.cn/problems/range-sum-query-2d-immutable/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 二维前缀和

算法步骤:
1. 在构造函数中，预处理一个二维前缀和数组 pre，大小为 (m+1) x (n+1)：
   - pre[i+1][j+1] = matrix[i][j] + pre[i][j+1] + pre[i+1][j] - pre[i][j]
   - 这样 pre[i][j] 表示原矩阵中 [0..i-1][0..j-1] 区域的和
2. 查询子矩形 [row1..row2][col1..col2] 的和时，利用前缀和差：
   - 结果 = pre[row2+1][col2+1] - pre[row1][col2+1] - pre[row2+1][col1] + pre[row1][col1]

关键点:
- 使用一圈额外边界（大小 +1）可以简化边界判断
- 构造 O(mn)，每次查询 O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度:
- 初始化: O(mn)
- 每次 sumRegion: O(1)
空间复杂度: O(mn)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.tree import TreeNode


class NumMatrix:
    """
    二维区域和检索 - 矩阵不可变
    """

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.pre = [[0]]
            return
        m, n = len(matrix), len(matrix[0])
        self.pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += matrix[i][j]
                self.pre[i + 1][j + 1] = self.pre[i][j + 1] + row_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pre = self.pre
        return (
            pre[row2 + 1][col2 + 1]
            - pre[row1][col2 + 1]
            - pre[row2 + 1][col1]
            + pre[row1][col1]
        )


# 注意：本题在 LeetCode 上直接使用 NumMatrix 类，不通过 create_solution
