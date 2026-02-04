# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 729
标题: My Calendar I
难度: medium
链接: https://leetcode.cn/problems/my-calendar-i/
题目类型: 设计、线段树、数组、二分查找、有序集合
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
729. 我的日程安排表 I - 实现一个 MyCalendar 类来存放你的日程安排。如果要添加的日程安排不会造成 重复预订 ，则可以存储这个新的日程安排。 当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生 重复预订 。 日程可以用一对整数 startTime 和 endTime 表示，这里的时间是半开区间，即 [startTime, endTime), 实数 x 的范围为， startTime <= x < endTime 。 实现 MyCalendar 类： * MyCalendar() 初始化日历对象。 * boolean book(int startTime, int endTime) 如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 true 。否则，返回 false 并且不要将该日程安排添加到日历中。 示例： 输入： ["MyCalendar", "book", "book", "book"] [[], [10, 20], [15, 25], [20, 30]] 输出： [null, true, false, true] 解释： MyCalendar myCalendar = new MyCalendar(); myCalendar.book(10, 20); // return True myCalendar.book(15, 25); // return False ，这个日程安排不能添加到日历中，因为时间 15 已经被另一个日程安排预订了。 myCalendar.book(20, 30); // return True ，这个日程安排可以添加到日历中，因为第一个日程安排预订的每个时间都小于 20 ，且不包含时间 20 。 提示： * 0 <= start < end <= 109 * 每个测试用例，调用 book 方法的次数最多不超过 1000 次。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用有序列表来存储所有已预订的时间段，并在每次预订时检查新时间段是否与已有时间段重叠。

算法步骤:
1. 初始化一个空的有序列表 `self.calendar` 来存储时间段。
2. 在 `book` 方法中，使用二分查找找到新时间段的插入位置。
3. 检查新时间段是否与前一个时间段或后一个时间段重叠，如果重叠则返回 `False`。
4. 如果没有重叠，则将新时间段插入有序列表并返回 `True`。

关键点:
- 使用 `bisect_left` 和 `bisect_right` 来确定新时间段的插入位置。
- 检查新时间段与相邻时间段是否有重叠。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 每次插入和查找操作的时间复杂度为 O(log n)，其中 n 是已预订的时间段数量。
空间复杂度: O(n) - 存储所有已预订的时间段需要 O(n) 的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from bisect import bisect_left, bisect_right

class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        # 使用二分查找找到插入位置
        i = bisect_right(self.calendar, (start, end))
        
        # 检查与前一个时间段是否有重叠
        if i > 0 and self.calendar[i-1][1] > start:
            return False
        
        # 检查与后一个时间段是否有重叠
        if i < len(self.calendar) and self.calendar[i][0] < end:
            return False
        
        # 插入新时间段
        self.calendar.insert(i, (start, end))
        return True


# 测试用例
if __name__ == "__main__":
    myCalendar = MyCalendar()
    print(myCalendar.book(10, 20))  # True
    print(myCalendar.book(15, 25))  # False
    print(myCalendar.book(20, 30))  # True