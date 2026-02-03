# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 731
标题: My Calendar II
难度: medium
链接: https://leetcode.cn/problems/my-calendar-ii/
题目类型: 设计、线段树、数组、二分查找、有序集合、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
731. 我的日程安排表 II - 实现一个程序来存放你的日程安排。如果要添加的时间内不会导致三重预订时，则可以存储这个新的日程安排。 当三个日程安排有一些时间上的交叉时（例如三个日程安排都在同一时间内），就会产生 三重预订。 事件能够用一对整数 startTime 和 endTime 表示，在一个半开区间的时间 [startTime, endTime) 上预定。实数 x 的范围为 startTime <= x < endTime。 实现 MyCalendarTwo 类： * MyCalendarTwo() 初始化日历对象。 * boolean book(int startTime, int endTime) 如果可以将日程安排成功添加到日历中而不会导致三重预订，返回 true。否则，返回 false 并且不要将该日程安排添加到日历中。 示例 1： 输入： ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"] [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]] 输出： [null, true, true, true, false, true, true] 解释： MyCalendarTwo myCalendarTwo = new MyCalendarTwo(); myCalendarTwo.book(10, 20); // 返回 True，能够预定该日程。 myCalendarTwo.book(50, 60); // 返回 True，能够预定该日程。 myCalendarTwo.book(10, 40); // 返回 True，该日程能够被重复预定。 myCalendarTwo.book(5, 15); // 返回 False，该日程导致了三重预定，所以不能预定。 myCalendarTwo.book(5, 10); // 返回 True，能够预定该日程，因为它不使用已经双重预订的时间 10。 myCalendarTwo.book(25, 55); // 返回 True，能够预定该日程，因为时间段 [25, 40) 将被第三个日程重复预定，时间段 [40, 50) 将被单独预定，而时间段 [50, 55) 将被第二个日程重复预定。 提示： * 0 <= start < end <= 109 * 最多调用 book 1000 次。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
