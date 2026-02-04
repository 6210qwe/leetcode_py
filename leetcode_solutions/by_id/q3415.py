# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3415
标题: Check if Grid Satisfies Conditions
难度: easy
链接: https://leetcode.cn/problems/check-if-grid-satisfies-conditions/
题目类型: 数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3142. 判断矩阵是否满足条件 - 给你一个大小为 m x n 的二维矩阵 grid 。你需要判断每一个格子 grid[i][j] 是否满足： * 如果它下面的格子存在，那么它需要等于它下面的格子，也就是 grid[i][j] == grid[i + 1][j] 。 * 如果它右边的格子存在，那么它需要不等于它右边的格子，也就是 grid[i][j] != grid[i][j + 1] 。 如果 所有 格子都满足以上条件，那么返回 true ，否则返回 false 。 示例 1： 输入：grid = [[1,0,2],[1,0,2]] 输出：true 解释： [https://assets.leetcode.com/uploads/2024/04/15/examplechanged.png] 网格图中所有格子都符合条件。 示例 2： 输入：grid = [[1,1,1],[0,0,0]] 输出：false 解释： [https://assets.leetcode.com/uploads/2024/03/27/example21.png] 同一行中的格子值都相等。 示例 3： 输入：grid = [[1],[2],[3]] 输出：false 解释： [https://assets.leetcode.com/uploads/2024/03/31/changed.png] 同一列中的格子值不相等。 提示： * 1 <= n, m <= 10 * 0 <= grid[i][j] <= 9
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 逐行逐列检查每个格子是否满足给定条件。

算法步骤:
1. 遍历每一行和每一列，检查每个格子是否满足条件。
2. 如果某个格子不满足条件，则返回 False。
3. 如果所有格子都满足条件，则返回 True。

关键点:
- 检查每个格子时，需要同时考虑其下方和右侧的格子。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(grid: List[List[int]]) -> bool:
    """
    函数式接口 - 判断矩阵是否满足条件
    """
    m, n = len(grid), len(grid[0])
    
    for i in range(m):
        for j in range(n):
            # 检查下方格子是否存在且是否相等
            if i < m - 1 and grid[i][j] != grid[i + 1][j]:
                return False
            # 检查右侧格子是否存在且是否不相等
            if j < n - 1 and grid[i][j] == grid[i][j + 1]:
                return False
    
    return True


Solution = create_solution(solution_function_name)