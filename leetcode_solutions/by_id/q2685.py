# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2685
标题: First Completely Painted Row or Column
难度: medium
链接: https://leetcode.cn/problems/first-completely-painted-row-or-column/
题目类型: 数组、哈希表、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2661. 找出叠涂元素 - 给你一个下标从 0 开始的整数数组 arr 和一个 m x n 的整数 矩阵 mat 。arr 和 mat 都包含范围 [1，m * n] 内的 所有 整数。 从下标 0 开始遍历 arr 中的每个下标 i ，并将包含整数 arr[i] 的 mat 单元格涂色。 请你找出 arr 中第一个使得 mat 的某一行或某一列都被涂色的元素，并返回其下标 i 。 示例 1： image explanation for example 1 [https://assets.leetcode.com/uploads/2023/01/18/grid1.jpg] 输入：arr = [1,3,4,2], mat = [[1,4],[2,3]] 输出：2 解释：遍历如上图所示，arr[2] 在矩阵中的第一行或第二列上都被涂色。 示例 2： image explanation for example 2 [https://assets.leetcode.com/uploads/2023/01/18/grid2.jpg] 输入：arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]] 输出：3 解释：遍历如上图所示，arr[3] 在矩阵中的第二列上都被涂色。 提示： * m == mat.length * n = mat[i].length * arr.length == m * n * 1 <= m, n <= 105 * 1 <= m * n <= 105 * 1 <= arr[i], mat[r][c] <= m * n * arr 中的所有整数 互不相同 * mat 中的所有整数 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
