# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1628
标题: Count Submatrices With All Ones
难度: medium
链接: https://leetcode.cn/problems/count-submatrices-with-all-ones/
题目类型: 栈、数组、动态规划、矩阵、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1504. 统计全 1 子矩形 - 给你一个 m x n 的二进制矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。 示例 1： [https://assets.leetcode.com/uploads/2021/10/27/ones1-grid.jpg] 输入：mat = [[1,0,1],[1,1,0],[1,1,0]] 输出：13 解释： 有 6 个 1x1 的矩形。 有 2 个 1x2 的矩形。 有 3 个 2x1 的矩形。 有 1 个 2x2 的矩形。 有 1 个 3x1 的矩形。 矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。 示例 2： [https://assets.leetcode.com/uploads/2021/10/27/ones2-grid.jpg] 输入：mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]] 输出：24 解释： 有 8 个 1x1 的子矩形。 有 5 个 1x2 的子矩形。 有 2 个 1x3 的子矩形。 有 4 个 2x1 的子矩形。 有 2 个 2x2 的子矩形。 有 2 个 3x1 的子矩形。 有 1 个 3x2 的子矩形。 矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。 提示： * 1 <= m, n <= 150 * mat[i][j] 仅包含 0 或 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和单调栈来计算每个位置的矩形数量。

算法步骤:
1. 初始化一个高度矩阵 `heights`，其中 `heights[i][j]` 表示从第 i 行到第 j 列的连续 1 的高度。
2. 对于每一行，使用单调栈来计算以该行为底的所有全 1 子矩形的数量。
3. 将每一行的结果累加得到最终结果。

关键点:
- 使用单调栈来高效计算每行的全 1 子矩形数量。
- 动态规划用于更新高度矩阵。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def countSubmatrices(mat: List[List[int]]) -> int:
    def count_rectangle(heights: List[int]) -> int:
        stack = []
        count = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                top = stack.pop()
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                count += (heights[top] - (heights[stack[-1]] if stack else 0)) * width
            stack.append(i)
        
        while stack:
            top = stack.pop()
            if not stack:
                width = len(heights)
            else:
                width = len(heights) - stack[-1] - 1
            count += (heights[top] - (heights[stack[-1]] if stack else 0)) * width
        
        return count

    m, n = len(mat), len(mat[0])
    heights = [0] * n
    result = 0

    for row in mat:
        for j in range(n):
            heights[j] = heights[j] + 1 if row[j] == 1 else 0
        result += count_rectangle(heights)

    return result

Solution = create_solution(countSubmatrices)