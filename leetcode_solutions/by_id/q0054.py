# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 54
标题: Spiral Matrix
难度: medium
链接: https://leetcode.cn/problems/spiral-matrix/
题目类型: 数组、矩阵、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
54. 螺旋矩阵 - 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。 示例 1： [https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg] 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]] 输出：[1,2,3,6,9,8,7,4,5] 示例 2： [https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg] 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] 输出：[1,2,3,4,8,12,11,10,9,5,6,7] 提示： * m == matrix.length * n == matrix[i].length * 1 <= m, n <= 10 * -100 <= matrix[i][j] <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 模拟螺旋遍历，使用四个边界变量控制遍历方向

算法步骤:
1. 初始化四个边界：top=0, bottom=m-1, left=0, right=n-1
2. 按照右->下->左->上的顺序遍历：
   - 向右：从left到right，遍历完top行，top++
   - 向下：从top到bottom，遍历完right列，right--
   - 向左：从right到left，遍历完bottom行，bottom--
   - 向上：从bottom到top，遍历完left列，left++
3. 重复直到所有元素都被遍历

关键点:
- 使用边界变量控制遍历范围
- 每次遍历完一行或一列后，更新对应的边界
- 注意边界条件：确保不重复遍历
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m*n) - 需要遍历矩阵中的每个元素
空间复杂度: O(1) - 只使用常数额外空间（不包括结果数组）
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    函数式接口 - 模拟螺旋遍历
    
    实现思路:
    使用四个边界变量控制遍历方向，按照右->下->左->上的顺序遍历矩阵。
    
    Args:
        matrix: m行n列的矩阵
        
    Returns:
        按顺时针螺旋顺序排列的矩阵元素列表
        
    Example:
        >>> spiral_order([[1,2,3],[4,5,6],[7,8,9]])
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
    """
    if not matrix or not matrix[0]:
        return []
    
    result = []
    m, n = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, m - 1, 0, n - 1
    
    while top <= bottom and left <= right:
        # 向右
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        
        # 向下
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # 向左（需要检查是否还有行）
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
        
        # 向上（需要检查是否还有列）
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(spiral_order)
