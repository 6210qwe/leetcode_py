# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2015
标题: Determine Whether Matrix Can Be Obtained By Rotation
难度: easy
链接: https://leetcode.cn/problems/determine-whether-matrix-can-be-obtained-by-rotation/
题目类型: 数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1886. 判断矩阵经轮转后是否一致 - 给你两个大小为 n x n 的二进制矩阵 mat 和 target 。现 以 90 度顺时针轮转 矩阵 mat 中的元素 若干次 ，如果能够使 mat 与 target 一致，返回 true ；否则，返回 false 。 示例 1： [https://assets.leetcode.com/uploads/2021/05/20/grid3.png] 输入：mat = [[0,1],[1,0]], target = [[1,0],[0,1]] 输出：true 解释：顺时针轮转 90 度一次可以使 mat 和 target 一致。 示例 2： [https://assets.leetcode.com/uploads/2021/05/20/grid4.png] 输入：mat = [[0,1],[1,1]], target = [[1,0],[0,1]] 输出：false 解释：无法通过轮转矩阵中的元素使 equal 与 target 一致。 示例 3： [https://assets.leetcode.com/uploads/2021/05/26/grid4.png] 输入：mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]] 输出：true 解释：顺时针轮转 90 度两次可以使 mat 和 target 一致。 提示： * n == mat.length == target.length * n == mat[i].length == target[i].length * 1 <= n <= 10 * mat[i][j] 和 target[i][j] 不是 0 就是 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过最多四次 90 度顺时针旋转来检查 mat 是否可以变成 target。

算法步骤:
1. 定义一个函数 `rotate_90` 来实现 90 度顺时针旋转。
2. 最多进行四次旋转，每次旋转后检查 mat 是否等于 target。
3. 如果在某次旋转后 mat 等于 target，则返回 True。
4. 如果四次旋转后 mat 仍不等于 target，则返回 False。

关键点:
- 通过四次 90 度旋转可以覆盖所有可能的旋转情况。
- 每次旋转后直接比较矩阵是否相等。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def rotate_90(matrix: List[List[int]]) -> None:
    """
    90 度顺时针旋转矩阵
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp

def solution_function_name(mat: List[List[int]], target: List[List[int]]) -> bool:
    """
    函数式接口 - 判断矩阵经轮转后是否一致
    """
    for _ in range(4):
        if mat == target:
            return True
        rotate_90(mat)
    return False

Solution = create_solution(solution_function_name)