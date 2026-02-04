# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 732
标题: My Calendar III
难度: hard
链接: https://leetcode.cn/problems/my-calendar-iii/
题目类型: 设计、线段树、二分查找、有序集合、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
732. 我的日程安排表 III - 当 k 个日程存在一些非空交集时（即, k 个日程包含了一些相同时间），就会产生 k 次预订。 给你一些日程安排 [startTime, endTime) ，请你在每个日程安排添加后，返回一个整数 k ，表示所有先前日程安排会产生的最大 k 次预订。 实现一个 MyCalendarThree 类来存放你的日程安排，你可以一直添加新的日程安排。 * MyCalendarThree() 初始化对象。 * int book(int startTime, int endTime) 返回一个整数 k ，表示日历中存在的 k 次预订的最大值。 示例： 输入： ["MyCalendarThree", "book", "book", "book", "book", "book", "book"] [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]] 输出： [null, 1, 1, 2, 3, 3, 3] 解释： MyCalendarThree myCalendarThree = new MyCalendarThree(); myCalendarThree.book(10, 20); // 返回 1 ，第一个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。 myCalendarThree.book(50, 60); // 返回 1 ，第二个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。 myCalendarThree.book(10, 40); // 返回 2 ，第三个日程安排 [10, 40) 与第一个日程安排相交，所以最大 k 次预订是 2 次预订。 myCalendarThree.book(5, 15); // 返回 3 ，剩下的日程安排的最大 k 次预订是 3 次预订。 myCalendarThree.book(5, 10); // 返回 3 myCalendarThree.book(25, 55); // 返回 3 提示： * 0 <= startTime < endTime <= 109 * 每个测试用例，调用 book 函数最多不超过 400次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用差分数组来记录每个时间点的预订变化情况，并使用一个变量来记录当前的最大预订次数。

算法步骤:
1. 初始化一个字典 `diff` 来记录每个时间点的预订变化情况。
2. 在每次调用 `book` 方法时，更新 `diff` 字典。
3. 遍历 `diff` 字典，计算当前的最大预订次数。

关键点:
- 使用差分数组的思想来记录每个时间点的预订变化情况。
- 通过遍历 `diff` 字典来计算当前的最大预订次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是调用 `book` 方法的次数。每次调用 `book` 方法的时间复杂度为 O(n)。
空间复杂度: O(n)，用于存储 `diff` 字典。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class MyCalendarThree:

    def __init__(self):
        self.diff = {}
        self.max_bookings = 0

    def book(self, start: int, end: int) -> int:
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1
        current_bookings = 0
        for time in sorted(self.diff.keys()):
            current_bookings += self.diff[time]
            self.max_bookings = max(self.max_bookings, current_bookings)
        return self.max_bookings


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(MyCalendarThree)