# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2482
标题: Maximum Rows Covered by Columns
难度: medium
链接: https://leetcode.cn/problems/maximum-rows-covered-by-columns/
题目类型: 位运算、数组、回溯、枚举、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2397. 被列覆盖的最多行数 - 给你一个下标从 0 开始、大小为 m x n 的二进制矩阵 matrix ；另给你一个整数 numSelect，表示你必须从 matrix 中选择的 不同 列的数量。 如果一行中所有的 1 都被你选中的列所覆盖，则认为这一行被 覆盖 了。 形式上，假设 s = {c1, c2, ...., cnumSelect} 是你选择的列的集合。对于矩阵中的某一行 row ，如果满足下述条件，则认为这一行被集合 s 覆盖： * 对于满足 matrix[row][col] == 1 的每个单元格 matrix[row][col]（0 <= col <= n - 1），col 均存在于 s 中，或者 * row 中 不存在 值为 1 的单元格。 你需要从矩阵中选出 numSelect 个列，使集合覆盖的行数最大化。 返回一个整数，表示可以由 numSelect 列构成的集合 覆盖 的 最大行数 。 示例 1： [https://assets.leetcode.com/uploads/2022/07/14/rowscovered.png] 输入：matrix = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], numSelect = 2 输出：3 解释： 图示中显示了一种覆盖 3 行的可行办法。 选择 s = {0, 2} 。 - 第 0 行被覆盖，因为其中没有出现 1 。 - 第 1 行被覆盖，因为值为 1 的两列（即 0 和 2）均存在于 s 中。 - 第 2 行未被覆盖，因为 matrix[2][1] == 1 但是 1 未存在于 s 中。 - 第 3 行被覆盖，因为 matrix[2][2] == 1 且 2 存在于 s 中。 因此，可以覆盖 3 行。 另外 s = {1, 2} 也可以覆盖 3 行，但可以证明无法覆盖更多行。 示例 2： [https://assets.leetcode.com/uploads/2022/07/14/rowscovered2.png] 输入：matrix = [[1],[0]], numSelect = 1 输出：2 解释： 选择唯一的一列，两行都被覆盖了，因为整个矩阵都被覆盖了。 所以我们返回 2 。 提示： * m == matrix.length * n == matrix[i].length * 1 <= m, n <= 12 * matrix[i][j] 要么是 0 要么是 1 * 1 <= numSelect <= n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用位运算和回溯法来枚举所有可能的列组合，并计算每种组合能覆盖的最大行数。

算法步骤:
1. 将每一行转换为一个整数，用二进制表示该行的 1 和 0。
2. 使用回溯法枚举所有可能的列组合。
3. 对于每一种列组合，计算它能覆盖的行数。
4. 返回最大覆盖行数。

关键点:
- 使用位运算来高效地表示和操作每一行。
- 使用回溯法来枚举所有可能的列组合。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n * m)，其中 n 是列数，m 是行数。最坏情况下需要枚举所有可能的列组合。
空间复杂度: O(n + m)，递归调用栈的深度为 n，存储每一行的整数表示需要 O(m) 空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def maximum_rows_covered(matrix: List[List[int]], num_select: int) -> int:
    """
    函数式接口 - 计算可以由 numSelect 列构成的集合覆盖的最大行数
    """
    m, n = len(matrix), len(matrix[0])
    rows = [0] * m
    
    # 将每一行转换为一个整数
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                rows[i] |= (1 << j)
    
    max_covered = 0
    
    def backtrack(start: int, selected: int, count: int):
        nonlocal max_covered
        if count == num_select:
            covered = sum(1 for row in rows if (row & selected) == row)
            max_covered = max(max_covered, covered)
            return
        
        for i in range(start, n):
            if (selected & (1 << i)) == 0:
                backtrack(i + 1, selected | (1 << i), count + 1)
    
    backtrack(0, 0, 0)
    return max_covered


Solution = create_solution(maximum_rows_covered)