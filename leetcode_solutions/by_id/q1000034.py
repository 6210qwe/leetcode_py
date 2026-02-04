# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000034
标题: Number Of 2s In Range LCCI
难度: hard
链接: https://leetcode.cn/problems/number-of-2s-in-range-lcci/
题目类型: 递归、数学、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 17.06. 2出现的次数 - 编写一个方法，计算从 0 到 n (含 n) 中数字 2 出现的次数。 示例： 输入：25 输出：9 解释：(2, 12, 20, 21, 22, 23, 24, 25)(注意 22 应该算作两次) 提示： * n <= 10^9
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用数学方法逐位计算2出现的次数

算法步骤:
1. 将数字n转换为字符串，方便逐位处理。
2. 对于每一位，计算当前位为2时的贡献。
3. 计算高位和低位对当前位的影响。

关键点:
- 通过分解每一位来避免直接遍历所有数字。
- 使用数学公式计算每一位上2出现的次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_digit_two(n: int) -> int:
    """
    计算从 0 到 n (含 n) 中数字 2 出现的次数
    """
    def count_2s_at_position(n: int, position: int) -> int:
        power_of_10 = 10 ** position
        next_power_of_10 = power_of_10 * 10
        right = n % power_of_10

        round_down = n - n % next_power_of_10
        round_up = round_down + next_power_of_10

        digit = (n // power_of_10) % 10

        if digit < 2:
            return round_down // 10
        elif digit == 2:
            return round_down // 10 + right + 1
        else:
            return round_up // 10

    total_count = 0
    num_digits = len(str(n))

    for i in range(num_digits):
        total_count += count_2s_at_position(n, i)

    return total_count


Solution = create_solution(count_digit_two)