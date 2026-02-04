# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100276
标题: 寻找目标值 - 二维数组
难度: medium
链接: https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
题目类型: 数组、二分查找、分治、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 121. 寻找目标值 - 二维数组 - m*n 的二维数组 plants 记录了园林景观的植物排布情况，具有以下特性： * 每行中，每棵植物的右侧相邻植物不矮于该植物； * 每列中，每棵植物的下侧相邻植物不矮于该植物。 请判断 plants 中是否存在目标高度值 target。 示例 1： 输入：plants = [[2,3,6,8],[4,5,8,9],[5,9,10,12]], target = 8 输出：true 示例 2： 输入：plants = [[1,3,5],[2,5,7]], target = 4 输出：false 提示： * 0 <= n <= 1000 * 0 <= m <= 1000 注意：本题与主站 240 题相同：https://leetcode.cn/problems/search-a-2d-matrix-ii/ [https://leetcode.cn/problems/search-a-2d-matrix-ii/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 从右上角开始搜索，利用矩阵的有序性逐步缩小搜索范围。

算法步骤:
1. 从矩阵的右上角开始。
2. 如果当前元素等于目标值，返回 True。
3. 如果当前元素大于目标值，向左移动一列。
4. 如果当前元素小于目标值，向下移动一行。
5. 重复上述步骤直到找到目标值或超出矩阵边界。

关键点:
- 利用矩阵的有序性，每次移动都能排除一行或一列。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m + n)，其中 m 和 n 分别是矩阵的行数和列数。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(plants: List[List[int]], target: int) -> bool:
    """
    函数式接口 - 从右上角开始搜索，利用矩阵的有序性逐步缩小搜索范围。
    """
    if not plants or not plants[0]:
        return False
    
    rows, cols = len(plants), len(plants[0])
    row, col = 0, cols - 1
    
    while row < rows and col >= 0:
        if plants[row][col] == target:
            return True
        elif plants[row][col] > target:
            col -= 1
        else:
            row += 1
    
    return False


Solution = create_solution(solution_function_name)