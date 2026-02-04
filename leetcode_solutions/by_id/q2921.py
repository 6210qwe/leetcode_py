# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2921
标题: Count Stepping Numbers in Range
难度: hard
链接: https://leetcode.cn/problems/count-stepping-numbers-in-range/
题目类型: 字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2801. 统计范围内的步进数字数目 - 给你两个正整数 low 和 high ，都用字符串表示，请你统计闭区间 [low, high] 内的 步进数字 数目。 如果一个整数相邻数位之间差的绝对值都 恰好 是 1 ，那么这个数字被称为 步进数字 。 请你返回一个整数，表示闭区间 [low, high] 之间步进数字的数目。 由于答案可能很大，请你将它对 109 + 7 取余 后返回。 注意：步进数字不能有前导 0 。 示例 1： 输入：low = "1", high = "11" 输出：10 解释：区间 [1,11] 内的步进数字为 1 ，2 ，3 ，4 ，5 ，6 ，7 ，8 ，9 和 10 。总共有 10 个步进数字。所以输出为 10 。 示例 2： 输入：low = "90", high = "101" 输出：2 解释：区间 [90,101] 内的步进数字为 98 和 101 。总共有 2 个步进数字。所以输出为 2 。 提示： * 1 <= int(low) <= int(high) < 10100 * 1 <= low.length, high.length <= 100 * low 和 high 只包含数字。 * low 和 high 都不含前导 0 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和记忆化搜索来生成步进数字，并检查它们是否在给定范围内。

算法步骤:
1. 定义一个递归函数 `count`，用于生成长度为 `n` 的步进数字，并使用记忆化技术来避免重复计算。
2. 在递归函数中，考虑当前数字的前一位和后一位之间的差值是否为 1。
3. 使用辅助函数 `is_valid` 来检查生成的数字是否在给定范围内。
4. 计算并返回结果。

关键点:
- 使用记忆化搜索来减少重复计算。
- 通过递归生成步进数字，并检查其是否在给定范围内。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(10 * 2 * n)，其中 n 是数字的最大长度（100），因为每个位置有 10 种可能的数字，且每个数字有两种可能的步进方向。
空间复杂度: O(n)，递归调用栈的深度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from functools import lru_cache

MOD = 10**9 + 7

def is_valid(num: str, low: str, high: str) -> bool:
    return low <= num <= high and all(abs(int(num[i]) - int(num[i+1])) == 1 for i in range(len(num) - 1))

@lru_cache(None)
def count(n: int, last_digit: int, is_limited: bool, has_started: bool, low: str, high: str) -> int:
    if n == 0:
        return 1 if has_started else 0
    
    total = 0
    start = 0 if has_started else 1
    end = int(high[-n]) if is_limited else 9
    
    for digit in range(start, end + 1):
        if not has_started or abs(digit - last_digit) == 1:
            next_is_limited = is_limited and digit == end
            next_has_started = has_started or digit > 0
            total += count(n - 1, digit, next_is_limited, next_has_started, low, high)
    
    return total % MOD

def solution_function_name(low: str, high: str) -> int:
    """
    函数式接口 - 统计范围内的步进数字数目
    """
    return (count(len(high), -1, True, False, low, high) - count(len(low) - 1, -1, True, False, low, high) + is_valid(low, low, high)) % MOD

Solution = create_solution(solution_function_name)