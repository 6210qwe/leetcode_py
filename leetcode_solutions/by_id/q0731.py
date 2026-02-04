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
核心思想: 使用两个列表分别记录单次预订和双重预订的区间。每次预订时，检查新预订是否会与现有的双重预订区间冲突，如果会则返回 False。否则，更新单次预订和双重预订的区间。

算法步骤:
1. 初始化两个列表 `single_booked` 和 `double_booked`，分别记录单次预订和双重预订的区间。
2. 在 `book` 方法中，遍历 `double_booked` 列表，检查新预订是否与现有的双重预订区间冲突。如果有冲突，返回 False。
3. 遍历 `single_booked` 列表，检查新预订是否与现有的单次预订区间有重叠。如果有重叠，将重叠部分记录到 `double_booked` 列表中。
4. 将新预订的区间添加到 `single_booked` 列表中，并返回 True。

关键点:
- 使用两个列表分别记录单次预订和双重预订的区间。
- 检查新预订是否会与现有的双重预订区间冲突。
- 更新单次预订和双重预订的区间。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是 `book` 方法的调用次数。每次调用 `book` 方法时，需要遍历 `single_booked` 和 `double_booked` 列表。
空间复杂度: O(n)，其中 n 是 `book` 方法的调用次数。需要存储所有的单次预订和双重预订的区间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class MyCalendarTwo:

    def __init__(self):
        self.single_booked = []
        self.double_booked = []

    def book(self, start: int, end: int) -> bool:
        # 检查新预订是否会与现有的双重预订区间冲突
        for s, e in self.double_booked:
            if start < e and end > s:
                return False
        
        # 更新双重预订的区间
        for s, e in self.single_booked:
            if start < e and end > s:
                self.double_booked.append((max(start, s), min(end, e)))
        
        # 更新单次预订的区间
        self.single_booked.append((start, end))
        return True


Solution = create_solution(MyCalendarTwo)