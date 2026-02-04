# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100309
标题: 数字 1 的个数
难度: hard
链接: https://leetcode.cn/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/
题目类型: 递归、数学、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 162. 数字 1 的个数 - 给定一个整数 num，计算所有小于等于 num 的非负整数中数字 1 出现的个数。 示例 1： 输入：num = 0 输出：0 示例 2： 输入：num = 13 输出：6 提示： * 0 <= num < 109 注意：本题与主站 233 题相同：https://leetcode.cn/problems/number-of-digit-one/ [https://leetcode.cn/problems/number-of-digit-one/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过递归和数学方法计算数字 1 出现的次数。

算法步骤:
1. 将数字 n 按位分解，分为高位 high 和低位 low。
2. 计算当前位为 1 的情况下的贡献。
3. 递归计算高位和低位的贡献。

关键点:
- 通过递归将问题分解为子问题。
- 通过数学方法计算当前位为 1 的情况下的贡献。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 每次递归处理一位数字。
空间复杂度: O(log n) - 递归调用栈的深度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_digit_one(n: int) -> int:
    """
    计算所有小于等于 n 的非负整数中数字 1 出现的个数。
    """
    if n <= 0:
        return 0
    if n < 10:
        return 1

    # 获取最高位的数字
    high = n // 10
    # 获取当前位的数字
    cur = n % 10
    # 获取当前位的权重
    weight = 1
    while high >= 10:
        weight *= 10
        high //= 10

    # 当前位为 0 的情况
    if cur == 0:
        return count_digit_one(n - cur - weight) + high * weight
    # 当前位为 1 的情况
    elif cur == 1:
        return count_digit_one(n - cur - weight) + high * weight + (n % weight) + 1
    # 当前位大于 1 的情况
    else:
        return count_digit_one(n - cur - weight) + high * weight + weight

Solution = create_solution(count_digit_one)