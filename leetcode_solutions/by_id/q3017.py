# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3017
标题: Number of Beautiful Integers in the Range
难度: hard
链接: https://leetcode.cn/problems/number-of-beautiful-integers-in-the-range/
题目类型: 数学、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2827. 范围中美丽整数的数目 - 给你正整数 low ，high 和 k 。 如果一个数满足以下两个条件，那么它是 美丽的 ： * 偶数数位的数目与奇数数位的数目相同。 * 这个整数可以被 k 整除。 请你返回范围 [low, high] 中美丽整数的数目。 示例 1： 输入：low = 10, high = 20, k = 3 输出：2 解释：给定范围中有 2 个美丽数字：[12,18] - 12 是美丽整数，因为它有 1 个奇数数位和 1 个偶数数位，而且可以被 k = 3 整除。 - 18 是美丽整数，因为它有 1 个奇数数位和 1 个偶数数位，而且可以被 k = 3 整除。 以下是一些不是美丽整数的例子： - 16 不是美丽整数，因为它不能被 k = 3 整除。 - 15 不是美丽整数，因为它的奇数数位和偶数数位的数目不相等。 给定范围内总共有 2 个美丽整数。 示例 2： 输入：low = 1, high = 10, k = 1 输出：1 解释：给定范围中有 1 个美丽数字：[10] - 10 是美丽整数，因为它有 1 个奇数数位和 1 个偶数数位，而且可以被 k = 1 整除。 给定范围内总共有 1 个美丽整数。 示例 3： 输入：low = 5, high = 5, k = 2 输出：0 解释：给定范围中有 0 个美丽数字。 - 5 不是美丽整数，因为它的奇数数位和偶数数位的数目不相等。 提示： * 0 < low <= high <= 109 * 0 < k <= 20
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来计算在给定范围内满足条件的美丽整数的数量。

算法步骤:
1. 定义一个递归函数 `dp` 来计算从当前位到最高位的美丽整数数量。
2. 使用记忆化搜索来避免重复计算。
3. 在递归过程中，维护当前数字的奇数位和偶数位的数量，并检查是否满足美丽整数的条件。
4. 使用前缀和来快速计算当前数字对 k 的余数。
5. 最终返回在 [low, high] 范围内的美丽整数数量。

关键点:
- 使用记忆化搜索来优化递归过程。
- 通过前缀和来快速计算当前数字对 k 的余数。
- 递归过程中维护奇数位和偶数位的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(10^d * d)，其中 d 是数字的最大位数（最多 10 位）。
空间复杂度: O(10^d * d)，用于记忆化搜索的缓存。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def count_beautiful_integers(low: int, high: int, k: int) -> int:
    def is_beautiful(num: int) -> bool:
        odd_count = even_count = 0
        while num > 0:
            digit = num % 10
            if digit % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
            num //= 10
        return odd_count == even_count and (num % k == 0)

    def dp(pos: int, has_odd: bool, has_even: bool, is_limit: bool, is_num: bool, mod: int) -> int:
        if pos == len(high_digits):
            return int(is_num and has_odd == has_even and mod == 0)
        if not is_limit and is_num and (has_odd, has_even, mod) in memo[pos]:
            return memo[pos][(has_odd, has_even, mod)]
        
        res = 0
        if not is_num:
            res = dp(pos + 1, False, False, False, False, 0)
        
        start = 0 if is_num else 1
        end = high_digits[pos] if is_limit else 9
        
        for digit in range(start, end + 1):
            next_is_limit = is_limit and digit == high_digits[pos]
            next_has_odd = has_odd or digit % 2 == 1
            next_has_even = has_even or digit % 2 == 0
            next_mod = (mod * 10 + digit) % k
            res += dp(pos + 1, next_has_odd, next_has_even, next_is_limit, True, next_mod)
        
        if is_num:
            memo[pos][(has_odd, has_even, mod)] = res
        
        return res

    def solve(num: int) -> int:
        nonlocal high_digits, memo
        high_digits = []
        while num > 0:
            high_digits.append(num % 10)
            num //= 10
        high_digits.reverse()
        memo = [{} for _ in range(len(high_digits) + 1)]
        return dp(0, False, False, True, False, 0)

    return solve(high) - solve(low - 1)

Solution = create_solution(count_beautiful_integers)