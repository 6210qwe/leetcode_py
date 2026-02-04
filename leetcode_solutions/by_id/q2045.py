# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2045
标题: Cutting Ribbons
难度: medium
链接: https://leetcode.cn/problems/cutting-ribbons/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定一个整数数组 ribbons，其中 ribbons[i] 表示第 i 条丝带的长度。你需要将这些丝带切成 k 段，每段长度相同且尽可能长。返回可以得到的最大长度。
如果无法切出 k 段，则返回 0。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来确定最大可能的长度。

算法步骤:
1. 确定二分查找的范围：最小值为 0，最大值为 ribbons 中的最大值。
2. 在二分查找的过程中，计算当前中间值 mid 作为可能的最大长度。
3. 对于每个 ribbon，计算可以切成多少段，累加总段数。
4. 如果总段数大于等于 k，说明可以切成更长的段，调整左边界；否则，调整右边界。
5. 最终返回右边界作为结果。

关键点:
- 使用二分查找来高效地找到最大可能的长度。
- 计算每个 ribbon 可以切成多少段时，使用整除操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log m)，其中 n 是 ribbons 的长度，m 是 ribbons 中的最大值。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(ribbons: List[int], k: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    def can_cut(length: int) -> bool:
        total_pieces = 0
        for ribbon in ribbons:
            total_pieces += ribbon // length
        return total_pieces >= k

    left, right = 0, max(ribbons)
    while left < right:
        mid = (left + right + 1) // 2
        if can_cut(mid):
            left = mid
        else:
            right = mid - 1
    return left


Solution = create_solution(solution_function_name)