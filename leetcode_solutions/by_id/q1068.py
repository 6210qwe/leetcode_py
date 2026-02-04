# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1068
标题: Digit Count in Range
难度: hard
链接: https://leetcode.cn/problems/digit-count-in-range/
题目类型: 数学、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1067. 范围内的数字计数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和数学方法来计算范围内的数字计数。

算法步骤:
1. 将数字分解为各个位上的数字，并记录每个位上的数字出现的次数。
2. 使用动态规划的方法，从高位到低位逐位计算每个数字在范围内的出现次数。
3. 对于每一位，分别计算当前位为0到9时的贡献，并累加到结果中。

关键点:
- 使用动态规划来避免重复计算。
- 通过分解数字和逐位计算来减少复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(d * 10) = O(d)，其中d是数字的位数。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def count_digit_in_range(n: int, d: int) -> int:
    def count_digit_in_range_helper(n: int, d: int) -> int:
        if n == 0:
            return 0
        str_n = str(n)
        length = len(str_n)
        dp = [0] * (length + 1)
        dp[0] = 1
        for i in range(1, length):
            dp[i] = 10 * dp[i - 1]
        
        count = 0
        for i in range(length):
            high = int(str_n[:i]) if i > 0 else 0
            current = int(str_n[i])
            low = int(str_n[i + 1:]) if i < length - 1 else 0
            power = 10 ** (length - i - 1)
            
            if current > d:
                count += (high + 1) * power
            elif current == d:
                count += high * power + low + 1
            else:
                count += high * power
            
            if d == 0 and i > 0:
                count -= power
        
        return count
    
    return count_digit_in_range_helper(n, d) - count_digit_in_range_helper(d - 1, d)

Solution = create_solution(count_digit_in_range)