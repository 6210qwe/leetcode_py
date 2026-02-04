# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1033
标题: Broken Calculator
难度: medium
链接: https://leetcode.cn/problems/broken-calculator/
题目类型: 贪心、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
991. 坏了的计算器 - 在显示着数字 startValue 的坏计算器上，我们可以执行以下两种操作： * 双倍（Double）：将显示屏上的数字乘 2； * 递减（Decrement）：将显示屏上的数字减 1 。 给定两个整数 startValue 和 target 。返回显示数字 target 所需的最小操作数。 示例 1： 输入：startValue = 2, target = 3 输出：2 解释：先进行双倍运算，然后再进行递减运算 {2 -> 4 -> 3}. 示例 2： 输入：startValue = 5, target = 8 输出：2 解释：先递减，再双倍 {5 -> 4 -> 8}. 示例 3： 输入：startValue = 3, target = 10 输出：3 解释：先双倍，然后递减，再双倍 {3 -> 6 -> 5 -> 10}. 提示： * 1 <= startValue, target <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 从 target 反向推导到 startValue，通过贪心算法减少操作次数。

算法步骤:
1. 如果 target 大于 startValue，则优先使用除以 2 的操作，因为这样可以更快地接近 startValue。
2. 如果 target 是奇数，则需要先加 1 再除以 2。
3. 当 target 小于等于 startValue 时，直接用减法操作将 startValue 减到 target。

关键点:
- 从 target 反向推导到 startValue，优先使用除以 2 的操作。
- 如果 target 是奇数，则先加 1 再除以 2。
- 当 target 小于等于 startValue 时，直接用减法操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log(target))
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def broken_calculator(startValue: int, target: int) -> int:
    """
    函数式接口 - 返回显示数字 target 所需的最小操作数
    """
    operations = 0
    while target > startValue:
        if target % 2 == 0:
            target //= 2
        else:
            target += 1
        operations += 1
    return operations + (startValue - target)


Solution = create_solution(broken_calculator)