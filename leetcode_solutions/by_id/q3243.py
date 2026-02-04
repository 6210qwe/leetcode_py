# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3243
标题: Count the Number of Powerful Integers
难度: hard
链接: https://leetcode.cn/problems/count-the-number-of-powerful-integers/
题目类型: 数学、字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2999. 统计强大整数的数目 - 给你三个整数 start ，finish 和 limit 。同时给你一个下标从 0 开始的字符串 s ，表示一个 正 整数。 如果一个 正 整数 x 末尾部分是 s （换句话说，s 是 x 的 后缀），且 x 中的每个数位至多是 limit ，那么我们称 x 是 强大的 。 请你返回区间 [start..finish] 内强大整数的 总数目 。 如果一个字符串 x 是 y 中某个下标开始（包括 0 ），到下标为 y.length - 1 结束的子字符串，那么我们称 x 是 y 的一个后缀。比方说，25 是 5125 的一个后缀，但不是 512 的后缀。 示例 1： 输入：start = 1, finish = 6000, limit = 4, s = "124" 输出：5 解释：区间 [1..6000] 内的强大数字为 124 ，1124 ，2124 ，3124 和 4124 。这些整数的各个数位都 <= 4 且 "124" 是它们的后缀。注意 5124 不是强大整数，因为第一个数位 5 大于 4 。 这个区间内总共只有这 5 个强大整数。 示例 2： 输入：start = 15, finish = 215, limit = 6, s = "10" 输出：2 解释：区间 [15..215] 内的强大整数为 110 和 210 。这些整数的各个数位都 <= 6 且 "10" 是它们的后缀。 这个区间总共只有这 2 个强大整数。 示例 3： 输入：start = 1000, finish = 2000, limit = 4, s = "3000" 输出：0 解释：区间 [1000..2000] 内的整数都小于 3000 ，所以 "3000" 不可能是这个区间内任何整数的后缀。 提示： * 1 <= start <= finish <= 1015 * 1 <= limit <= 9 * 1 <= s.length <= floor(log10(finish)) + 1 * s 数位中每个数字都小于等于 limit 。 * s 不包含任何前导 0 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用数位动态规划 (DP) 来计算满足条件的强大整数的数量。

算法步骤:
1. 将 `start` 和 `finish` 转换为字符串形式，方便逐位处理。
2. 定义一个 DP 函数，用于计算在给定限制条件下，从当前位开始的有效数字数量。
3. 通过递归和记忆化搜索来计算有效数字的数量。
4. 处理边界情况，确保 `start` 和 `finish` 之间的所有数字都被考虑。

关键点:
- 使用递归和记忆化搜索来避免重复计算。
- 逐位处理数字，确保每个数位不超过 `limit`。
- 处理前缀和后缀的匹配。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(d * 10 * d) = O(d^2)，其中 d 是 `finish` 的位数。
空间复杂度: O(d * 10 * d) = O(d^2)，由于使用了记忆化搜索。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_powerful_integers(start: int, finish: int, limit: int, s: str) -> int:
    """
    计算区间 [start, finish] 内的强大整数的数量。
    """
    def dp(pos: int, is_limit: bool, is_prefix: bool, is_suffix: bool) -> int:
        if pos == len(finish_str):
            return 1 if is_suffix else 0
        if not is_limit and not is_prefix and (pos, is_suffix) in memo:
            return memo[(pos, is_suffix)]
        
        res = 0
        up = int(finish_str[pos]) if is_limit else 9
        for digit in range(0, up + 1):
            if digit > limit:
                continue
            next_is_limit = is_limit and digit == up
            next_is_prefix = is_prefix and digit == int(start_str[pos])
            next_is_suffix = is_suffix or (pos >= len(s) and s[-len(finish_str) + pos] == str(digit))
            res += dp(pos + 1, next_is_limit, next_is_prefix, next_is_suffix)
        
        if not is_limit and not is_prefix:
            memo[(pos, is_suffix)] = res
        return res
    
    start_str = str(start - 1)
    finish_str = str(finish)
    memo = {}
    return dp(0, True, True, False)


Solution = create_solution(count_powerful_integers)