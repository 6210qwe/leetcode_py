# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2955
标题: Account Balance After Rounded Purchase
难度: easy
链接: https://leetcode.cn/problems/account-balance-after-rounded-purchase/
题目类型: 数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2806. 取整购买后的账户余额 - 一开始，你的银行账户里有 100 块钱。 给你一个整数purchaseAmount ，它表示你在一次购买中愿意支出的金额。 在一个商店里，你进行一次购买，实际支出的金额会向 最近 的 10 的 倍数 取整。换句话说，你实际会支付一个 非负 金额 roundedAmount ，满足 roundedAmount 是 10 的倍数且 abs(roundedAmount - purchaseAmount) 的值 最小 。 如果存在多于一个最接近的 10 的倍数，较大的倍数 是你的实际支出金额。 请你返回一个整数，表示你在愿意支出金额为 purchaseAmount 块钱的前提下，购买之后剩下的余额。 注意： 0 也是 10 的倍数。 示例 1： 输入：purchaseAmount = 9 输出：90 解释：这个例子中，最接近 9 的 10 的倍数是 10 。所以你的账户余额为 100 - 10 = 90 。 示例 2： 输入：purchaseAmount = 15 输出：80 解释：这个例子中，有 2 个最接近 15 的 10 的倍数：10 和 20，较大的数 20 是你的实际开销。 所以你的账户余额为 100 - 20 = 80 。 提示： * 0 <= purchaseAmount <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过计算最接近的 10 的倍数来确定实际支出金额，并从初始余额中减去该金额。

算法步骤:
1. 计算 purchaseAmount 向下取整到最近的 10 的倍数。
2. 计算 purchaseAmount 向上取整到最近的 10 的倍数。
3. 比较两个值，选择更接近的那个，如果距离相同则选择较大的那个。
4. 从初始余额 100 中减去实际支出金额，得到剩余余额。

关键点:
- 使用简单的数学运算来确定最接近的 10 的倍数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(purchase_amount: int) -> int:
    """
    函数式接口 - 计算购买后的账户余额
    """
    # 向下取整到最近的 10 的倍数
    lower_rounded = (purchase_amount // 10) * 10
    # 向上取整到最近的 10 的倍数
    upper_rounded = (purchase_amount + 9) // 10 * 10

    # 选择更接近的那个，如果距离相同则选择较大的那个
    if (purchase_amount - lower_rounded) <= (upper_rounded - purchase_amount):
        rounded_amount = lower_rounded
    else:
        rounded_amount = upper_rounded

    # 从初始余额 100 中减去实际支出金额
    remaining_balance = 100 - rounded_amount
    return remaining_balance


Solution = create_solution(solution_function_name)