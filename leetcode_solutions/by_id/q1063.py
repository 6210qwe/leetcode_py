# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1063
标题: Best Sightseeing Pair
难度: medium
链接: https://leetcode.cn/problems/best-sightseeing-pair/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1014. 最佳观光组合 - 给你一个正整数数组 values，其中 values[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的 距离 为 j - i。 一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去 它们两者之间的距离。 返回一对观光景点能取得的最高分。 示例 1： 输入：values = [8,1,5,2,6] 输出：11 解释：i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11 示例 2： 输入：values = [1,2] 输出：2 提示： * 2 <= values.length <= 5 * 104 * 1 <= values[i] <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来记录每个位置的最大值，并在遍历过程中更新最大得分。

算法步骤:
1. 初始化两个变量：`max_i_plus_val` 用于记录 `values[i] + i` 的最大值，`max_score` 用于记录当前的最大得分。
2. 遍历数组，对于每个 `j`，计算 `values[j] + j` 并与 `max_i_plus_val` 结合，更新 `max_score`。
3. 更新 `max_i_plus_val` 为 `values[j] + j` 和 `max_i_plus_val` 中的较大值。
4. 返回 `max_score`。

关键点:
- 通过维护 `max_i_plus_val` 来减少重复计算，从而提高效率。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度，因为只需要一次遍历。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(values: List[int]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    max_i_plus_val = 0
    max_score = float('-inf')
    
    for j in range(len(values)):
        max_score = max(max_score, max_i_plus_val + values[j] - j)
        max_i_plus_val = max(max_i_plus_val, values[j] + j)
    
    return max_score


Solution = create_solution(solution_function_name)