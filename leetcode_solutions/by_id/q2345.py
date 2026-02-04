# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2345
标题: Minimum Number of Operations to Convert Time
难度: easy
链接: https://leetcode.cn/problems/minimum-number-of-operations-to-convert-time/
题目类型: 贪心、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2224. 转化时间需要的最少操作数 - 给你两个字符串 current 和 correct ，表示两个 24 小时制时间 。 24 小时制时间 按 "HH:MM" 进行格式化，其中 HH 在 00 和 23 之间，而 MM 在 00 和 59 之间。最早的 24 小时制时间为 00:00 ，最晚的是 23:59 。 在一步操作中，你可以将 current 这个时间增加 1、5、15 或 60 分钟。你可以执行这一操作 任意 次数。 返回将 current 转化为 correct 需要的 最少操作数 。 示例 1： 输入：current = "02:30", correct = "04:35" 输出：3 解释： 可以按下述 3 步操作将 current 转换为 correct ： - 为 current 加 60 分钟，current 变为 "03:30" 。 - 为 current 加 60 分钟，current 变为 "04:30" 。 - 为 current 加 5 分钟，current 变为 "04:35" 。 可以证明，无法用少于 3 步操作将 current 转化为 correct 。 示例 2： 输入：current = "11:00", correct = "11:01" 输出：1 解释：只需要为 current 加一分钟，所以最小操作数是 1 。 提示： * current 和 correct 都符合 "HH:MM" 格式 * current <= correct
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，优先使用大单位的时间增量（60, 15, 5, 1）来减少操作次数。

算法步骤:
1. 将 current 和 correct 转换为分钟数。
2. 计算两者之间的分钟差。
3. 依次尝试使用 60, 15, 5, 1 分钟的增量，计算所需的操作次数。

关键点:
- 优先使用大单位的时间增量可以确保操作次数最少。
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


def solution_function_name(current: str, correct: str) -> int:
    """
    函数式接口 - 实现
    """
    # 将时间转换为分钟数
    def time_to_minutes(time: str) -> int:
        hours, minutes = map(int, time.split(':'))
        return hours * 60 + minutes

    # 计算当前时间和正确时间之间的分钟差
    diff = time_to_minutes(correct) - time_to_minutes(current)

    # 优先使用大单位的时间增量
    operations = 0
    for increment in [60, 15, 5, 1]:
        operations += diff // increment
        diff %= increment

    return operations


Solution = create_solution(solution_function_name)