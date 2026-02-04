# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2496
标题: Count Days Spent Together
难度: easy
链接: https://leetcode.cn/problems/count-days-spent-together/
题目类型: 数学、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2409. 统计共同度过的日子数 - Alice 和 Bob 计划分别去罗马开会。 给你四个字符串 arriveAlice ，leaveAlice ，arriveBob 和 leaveBob 。Alice 会在日期 arriveAlice 到 leaveAlice 之间在城市里（日期为闭区间），而 Bob 在日期 arriveBob 到 leaveBob 之间在城市里（日期为闭区间）。每个字符串都包含 5 个字符，格式为 "MM-DD" ，对应着一个日期的月和日。 请你返回 Alice和 Bob 同时在罗马的天数。 你可以假设所有日期都在 同一个 自然年，而且 不是 闰年。每个月份的天数分别为：[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 。 示例 1： 输入：arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19" 输出：3 解释：Alice 从 8 月 15 号到 8 月 18 号在罗马。Bob 从 8 月 16 号到 8 月 19 号在罗马，他们同时在罗马的日期为 8 月 16、17 和 18 号。所以答案为 3 。 示例 2： 输入：arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31" 输出：0 解释：Alice 和 Bob 没有同时在罗马的日子，所以我们返回 0 。 提示： * 所有日期的格式均为 "MM-DD" 。 * Alice 和 Bob 的到达日期都 早于或等于 他们的离开日期。 * 题目测试用例所给出的日期均为 非闰年 的有效日期。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 将日期转换为一年中的第几天，然后计算重叠的天数。

算法步骤:
1. 定义一个函数 `date_to_day` 将日期字符串转换为一年中的第几天。
2. 计算 Alice 和 Bob 的到达和离开日期在一年中的第几天。
3. 计算重叠的天数。

关键点:
- 使用累加的方式来计算每个月的天数。
- 通过比较日期来确定重叠部分。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 日期转换和计算都是常数时间操作。
空间复杂度: O(1) - 只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def date_to_day(date: str) -> int:
    """将日期字符串转换为一年中的第几天"""
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month, day = map(int, date.split('-'))
    return sum(days_in_month[:month]) + day

def count_days_spent_together(arrive_alice: str, leave_alice: str, arrive_bob: str, leave_bob: str) -> int:
    """
    计算 Alice 和 Bob 同时在罗马的天数
    """
    alice_start = date_to_day(arrive_alice)
    alice_end = date_to_day(leave_alice)
    bob_start = date_to_day(arrive_bob)
    bob_end = date_to_day(leave_bob)

    # 计算重叠的天数
    overlap_start = max(alice_start, bob_start)
    overlap_end = min(alice_end, bob_end)
    return max(0, overlap_end - overlap_start + 1)

Solution = create_solution(count_days_spent_together)