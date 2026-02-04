# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2757
标题: Count of Integers
难度: hard
链接: https://leetcode.cn/problems/count-of-integers/
题目类型: 数学、字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2719. 统计整数数目 - 给你两个数字字符串 num1 和 num2 ，以及两个整数 max_sum 和 min_sum 。如果一个整数 x 满足以下条件，我们称它是一个好整数： * num1 <= x <= num2 * min_sum <= digit_sum(x) <= max_sum. 请你返回好整数的数目。答案可能很大，请返回答案对 109 + 7 取余后的结果。 注意，digit_sum(x) 表示 x 各位数字之和。 示例 1： 输入：num1 = "1", num2 = "12", min_sum = 1, max_sum = 8 输出：11 解释：总共有 11 个整数的数位和在 1 到 8 之间，分别是 1,2,3,4,5,6,7,8,10,11 和 12 。所以我们返回 11 。 示例 2： 输入：num1 = "1", num2 = "5", min_sum = 1, max_sum = 5 输出：5 解释：数位和在 1 到 5 之间的 5 个整数分别为 1,2,3,4 和 5 。所以我们返回 5 。 提示： * 1 <= num1 <= num2 <= 1022 * 1 <= min_sum <= max_sum <= 400
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来计算满足条件的整数数量。

算法步骤:
1. 将问题转化为计算从 0 到 num2 的满足条件的整数数量，再减去从 0 到 num1-1 的满足条件的整数数量。
2. 使用动态规划来计算从 0 到某个数的满足条件的整数数量。
3. 动态规划的状态表示为 dp[i][j][k]，其中 i 表示当前处理到第 i 位，j 表示当前数位和，k 表示是否严格小于上限。
4. 通过递归加记忆化搜索来实现动态规划。

关键点:
- 通过动态规划和记忆化搜索来避免重复计算。
- 处理边界情况，特别是当 num1 为 0 时的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(22 * 400 * 2) = O(17600)，其中 22 是数字的最大长度，400 是最大数位和，2 是是否严格小于上限的状态。
空间复杂度: O(22 * 400 * 2) = O(17600)，用于存储动态规划的状态。
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

def count_good_integers(num1: str, num2: str, min_sum: int, max_sum: int) -> int:
    @lru_cache(None)
    def dp(index: int, current_sum: int, is_limit: bool) -> int:
        if current_sum > max_sum:
            return 0
        if index == len(num):
            return 1 if min_sum <= current_sum <= max_sum else 0
        
        total = 0
        up = int(num[index]) if is_limit else 9
        for digit in range(up + 1):
            total += dp(index + 1, current_sum + digit, is_limit and digit == up)
        
        return total % MOD
    
    def count(num: str) -> int:
        return dp(0, 0, True)
    
    # 计算 [0, num2] 中的好整数数量
    count_num2 = count(num2)
    # 计算 [0, num1-1] 中的好整数数量
    count_num1_minus_1 = count(str(int(num1) - 1)) if num1 != "0" else 0
    
    return (count_num2 - count_num1_minus_1) % MOD

Solution = create_solution(count_good_integers)