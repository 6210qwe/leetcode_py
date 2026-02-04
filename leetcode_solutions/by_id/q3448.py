# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3448
标题: Consecutive Available Seats II
难度: medium
链接: https://leetcode.cn/problems/consecutive-available-seats-ii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3140. 连续空余座位 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数来查找连续的空座位。

算法步骤:
1. 使用窗口函数 `LAG` 和 `LEAD` 来获取每个座位的前一个和后一个座位的状态。
2. 通过比较当前座位、前一个座位和后一个座位的状态，找出连续的空座位。
3. 返回符合条件的座位编号。

关键点:
- 使用窗口函数可以有效地处理连续性问题。
- 通过比较当前座位及其前后座位的状态，可以准确地找到连续的空座位。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是座位的数量。窗口函数的计算是线性的。
空间复杂度: O(1)，不需要额外的空间，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def solution_function_name(seat_status: List[Optional[int]]) -> List[int]:
    """
    函数式接口 - 找出连续的空座位
    :param seat_status: 座位状态列表，1 表示有人，0 表示空座
    :return: 连续空座位的起始位置列表
    """
    if not seat_status:
        return []

    n = len(seat_status)
    result = []
    prev_seat = None
    next_seat = None

    for i in range(n):
        if i > 0:
            prev_seat = seat_status[i - 1]
        if i < n - 1:
            next_seat = seat_status[i + 1]

        if seat_status[i] == 0 and (prev_seat is None or prev_seat == 1) and (next_seat is None or next_seat == 1):
            result.append(i)

    return result

Solution = create_solution(solution_function_name)