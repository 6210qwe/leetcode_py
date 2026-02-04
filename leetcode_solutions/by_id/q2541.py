# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2541
标题: Sum of Number and Its Reverse
难度: medium
链接: https://leetcode.cn/problems/sum-of-number-and-its-reverse/
题目类型: 数学、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2443. 反转之后的数字和 - 给你一个 非负 整数 num 。如果存在某个 非负 整数 k 满足 k + reverse(k) = num ，则返回 true ；否则，返回 false 。 reverse(k) 表示 k 反转每个数位后得到的数字。 示例 1： 输入：num = 443 输出：true 解释：172 + 271 = 443 ，所以返回 true 。 示例 2： 输入：num = 63 输出：false 解释：63 不能表示为非负整数及其反转后数字之和，返回 false 。 示例 3： 输入：num = 181 输出：true 解释：140 + 041 = 181 ，所以返回 true 。注意，反转后的数字可能包含前导零。 提示： * 0 <= num <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 枚举所有可能的 k，并检查 k + reverse(k) 是否等于 num。

算法步骤:
1. 如果 num 为 0，直接返回 True。
2. 枚举从 1 到 num 的所有整数 k。
3. 对于每个 k，计算其反转值 reverse(k)。
4. 检查 k + reverse(k) 是否等于 num，如果是则返回 True。
5. 如果遍历完所有 k 都没有找到满足条件的 k，则返回 False。

关键点:
- 使用字符串反转来实现 reverse(k)。
- 通过枚举所有可能的 k 来确保不会遗漏任何情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 num 的大小。最坏情况下需要枚举从 1 到 num 的所有整数。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(num: int) -> bool:
    """
    函数式接口 - 判断是否存在某个非负整数 k 满足 k + reverse(k) = num
    """
    if num == 0:
        return True

    def reverse(x: int) -> int:
        return int(str(x)[::-1])

    for k in range(1, num):
        if k + reverse(k) == num:
            return True

    return False


Solution = create_solution(solution_function_name)