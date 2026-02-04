# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 633
标题: Sum of Square Numbers
难度: medium
链接: https://leetcode.cn/problems/sum-of-square-numbers/
题目类型: 数学、双指针、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
633. 平方数之和 - 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。 示例 1： 输入：c = 5 输出：true 解释：1 * 1 + 2 * 2 = 5 示例 2： 输入：c = 3 输出：false 提示： * 0 <= c <= 231 - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针法来解决这个问题。一个指针从 0 开始，另一个指针从 sqrt(c) 开始，逐步向中间移动，检查是否满足 a^2 + b^2 = c。

算法步骤:
1. 初始化两个指针 left 和 right，left 为 0，right 为 int(sqrt(c))。
2. 当 left <= right 时，计算 left^2 + right^2 的值：
   - 如果等于 c，返回 True。
   - 如果小于 c，增加 left 指针。
   - 如果大于 c，减少 right 指针。
3. 如果遍历完所有可能的组合仍未找到满足条件的 a 和 b，返回 False。

关键点:
- 使用双指针可以有效地减少搜索范围，时间复杂度为 O(sqrt(c))。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(sqrt(c))
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(c: int) -> bool:
    """
    函数式接口 - 判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c。
    """
    if c < 0:
        return False

    left, right = 0, int(c ** 0.5)
    while left <= right:
        current_sum = left * left + right * right
        if current_sum == c:
            return True
        elif current_sum < c:
            left += 1
        else:
            right -= 1
    return False


Solution = create_solution(solution_function_name)