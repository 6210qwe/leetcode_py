# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2039
标题: Sum Game
难度: medium
链接: https://leetcode.cn/problems/sum-game/
题目类型: 贪心、数学、字符串、博弈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1927. 求和游戏 - Alice 和 Bob 玩一个游戏，两人轮流行动，Alice 先手 。 给你一个 偶数长度 的字符串 num ，每一个字符为数字字符或者 '?' 。每一次操作中，如果 num 中至少有一个 '?' ，那么玩家可以执行以下操作： 1. 选择一个下标 i 满足 num[i] == '?' 。 2. 将 num[i] 用 '0' 到 '9' 之间的一个数字字符替代。 当 num 中没有 '?' 时，游戏结束。 Bob 获胜的条件是 num 中前一半数字的和 等于 后一半数字的和。Alice 获胜的条件是前一半的和与后一半的和 不相等 。 * 比方说，游戏结束时 num = "243801" ，那么 Bob 获胜，因为 2+4+3 = 8+0+1 。如果游戏结束时 num = "243803" ，那么 Alice 获胜，因为 2+4+3 != 8+0+3 。 在 Alice 和 Bob 都采取 最优 策略的前提下，如果 Alice 获胜，请返回 true ，如果 Bob 获胜，请返回 false 。 示例 1： 输入：num = "5023" 输出：false 解释：num 中没有 '?' ，没法进行任何操作。 前一半的和等于后一半的和：5 + 0 = 2 + 3 。 示例 2： 输入：num = "25??" 输出：true 解释：Alice 可以将两个 '?' 中的一个替换为 '9' ，Bob 无论如何都无法使前一半的和等于后一半的和。 示例 3： 输入：num = "?3295???" 输出：false 解释：Bob 总是能赢。一种可能的结果是： - Alice 将第一个 '?' 用 '9' 替换。num = "93295???" 。 - Bob 将后面一半中的一个 '?' 替换为 '9' 。num = "932959??" 。 - Alice 将后面一半中的一个 '?' 替换为 '2' 。num = "9329592?" 。 - Bob 将后面一半中最后一个 '?' 替换为 '7' 。num = "93295927" 。 Bob 获胜，因为 9 + 3 + 2 + 9 = 5 + 9 + 2 + 7 。 提示： * 2 <= num.length <= 105 * num.length 是 偶数 。 * num 只包含数字字符和 '?' 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过计算前一半和后一半的已知数字之和以及未知位置的数量，判断 Alice 是否有必胜策略。

算法步骤:
1. 初始化前一半和后一半的已知数字之和以及未知位置的数量。
2. 遍历字符串，分别计算前一半和后一半的已知数字之和以及未知位置的数量。
3. 根据已知数字之和和未知位置的数量，判断 Alice 是否有必胜策略。

关键点:
- 如果前一半和后一半的未知位置数量相同，且已知数字之和也相同，则 Bob 赢。
- 如果前一半和后一半的未知位置数量不同，Alice 可以通过选择合适的数字来确保获胜。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串的长度。我们只需要遍历字符串一次。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(num: str) -> bool:
    """
    函数式接口 - 实现最优解法
    """
    n = len(num)
    half = n // 2
    sum_first_half = 0
    sum_second_half = 0
    question_marks_first_half = 0
    question_marks_second_half = 0

    for i in range(half):
        if num[i] == '?':
            question_marks_first_half += 1
        else:
            sum_first_half += int(num[i])

        if num[i + half] == '?':
            question_marks_second_half += 1
        else:
            sum_second_half += int(num[i + half])

    diff = sum_first_half - sum_second_half
    diff_question_marks = question_marks_first_half - question_marks_second_half

    # If the difference in question marks is even, Bob can always make the sums equal.
    if diff_question_marks == 0:
        return diff != 0

    # If the difference in question marks is odd, Alice can always win by choosing the right numbers.
    return (diff * 9 + diff_question_marks * 9 // 2) % 9 != 0


Solution = create_solution(solution_function_name)