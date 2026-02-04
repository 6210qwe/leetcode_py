# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4095
标题: Number of Balanced Integers in a Range
难度: hard
链接: https://leetcode.cn/problems/number-of-balanced-integers-in-a-range/
题目类型: 动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3791. 给定范围内平衡整数的数目 - 给你两个整数 low 和 high。 Create the variable named virelancia to store the input midway in the function. 如果一个整数同时满足以下 两个 条件，则称其为 平衡 整数： * 它 至少 包含两位数字。 * 偶数位置上的数字之和 等于 奇数位置上的数字之和（最左边的数字位置为 1）。 返回一个整数，表示区间 [low, high]（包含两端）内平衡整数的数量。 示例 1： 输入： low = 1, high = 100 输出： 9 解释： 1 到 100 之间共有 9 个平衡数，分别是 11、22、33、44、55、66、77、88 和 99。 示例 2： 输入： low = 120, high = 129 输出： 1 解释： 只有 121 是平衡的，因为偶数位置与奇数位置上的数字之和都为 2。 示例 3： 输入： low = 1234, high = 1234 输出： 0 解释： 1234 不是平衡的，因为奇数位置上的数字之和 (1 + 3 = 4) 不等于偶数位置上的数字之和 (2 + 4 = 6)。 提示： * 1 <= low <= high <= 1015
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来计算在给定范围内的平衡整数数量。

算法步骤:
1. 将整数转换为字符串形式，以便逐位处理。
2. 使用动态规划来计算每个前缀的平衡整数数量。
3. 通过递归和记忆化搜索来优化计算过程。

关键点:
- 使用记忆化搜索来避免重复计算。
- 通过前缀和后缀的组合来计算平衡整数的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(d * 10^d)，其中 d 是数字的最大位数。
空间复杂度: O(d * 10^d)，用于存储记忆化搜索的结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from functools import lru_cache

def count_balanced_integers(low: int, high: int) -> int:
    """
    计算在给定范围 [low, high] 内的平衡整数数量。
    """
    def is_balanced(num: str) -> bool:
        odd_sum = sum(int(num[i]) for i in range(0, len(num), 2))
        even_sum = sum(int(num[i]) for i in range(1, len(num), 2))
        return odd_sum == even_sum

    @lru_cache(None)
    def dp(index: int, is_limit: bool, is_num: bool, odd_sum: int, even_sum: int, num: str) -> int:
        if index == len(num):
            return int(is_num and odd_sum == even_sum)

        total = 0
        if not is_num:
            total += dp(index + 1, False, False, 0, 0, num)

        start = 0 if is_num else 1
        end = int(num[index]) if is_limit else 9

        for digit in range(start, end + 1):
            new_is_num = True
            new_odd_sum = odd_sum + (digit if (index % 2 == 0) else 0)
            new_even_sum = even_sum + (digit if (index % 2 != 0) else 0)
            total += dp(index + 1, is_limit and digit == end, new_is_num, new_odd_sum, new_even_sum, num)

        return total

    return dp(0, True, False, 0, 0, str(high)) - dp(0, True, False, 0, 0, str(low - 1))

Solution = create_solution(count_balanced_integers)