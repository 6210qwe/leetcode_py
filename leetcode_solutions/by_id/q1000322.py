# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000322
标题: 我的日程安排表 I
难度: medium
链接: https://leetcode.cn/problems/fi9suh/
题目类型: 设计、线段树、二分查找、有序集合
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 058. 我的日程安排表 I - 请实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内没有其他安排，则可以存储这个新的日程安排。 MyCalendar 有一个 book(int start, int end)方法。它意味着在 start 到 end 时间内增加一个日程安排，注意，这里的时间是半开区间，即 [start, end), 实数 x 的范围为， start <= x < end。 当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生重复预订。 每次调用 MyCalendar.book方法时，如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 true。否则，返回 false 并且不要将该日程安排添加到日历中。 请按照以下步骤调用 MyCalendar 类: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end) 示例 1： 输入: ["MyCalendar","book","book","book"] [[],[10,20],[15,25],[20,30]] 输出: [null,true,false,true] 解释: MyCalendar myCalendar = new MyCalendar(); MyCalendar.book(10, 20); // returns true MyCalendar.book(15, 25); // returns false ，第二个日程安排不能添加到日历中，因为时间 15 已经被第一个日程安排预定了 MyCalendar.book(20, 30); // returns true ，第三个日程安排可以添加到日历中，因为第一个日程安排并不包含时间 20 提示： * 每个测试用例，调用 MyCalendar.book 函数最多不超过 1000次。 * 0 <= start < end <= 109 注意：本题与主站 729 题相同： https://leetcode.cn/problems/my-calendar-i/ [https://leetcode.cn/problems/my-calendar-i/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用有序列表来存储日程安排，并通过二分查找来检查新日程是否与已有日程冲突。

算法步骤:
1. 初始化一个空的有序列表 `events` 来存储日程安排。
2. 在 `book` 方法中，使用二分查找找到插入位置。
3. 检查插入位置前后的日程是否有重叠，如果有则返回 `False`。
4. 如果没有重叠，则将新日程插入有序列表并返回 `True`。

关键点:
- 使用 `bisect_left` 和 `bisect_right` 来确定插入位置和检查重叠。
- 有序列表 `events` 保持日程按开始时间排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 二分查找的时间复杂度。
空间复杂度: O(n) - 存储所有日程安排的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import bisect

class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        # 找到 start 应该插入的位置
        i = bisect.bisect_right(self.events, (start, end))
        
        # 检查插入位置前后的日程是否有重叠
        if i > 0 and self.events[i-1][1] > start:
            return False
        if i < len(self.events) and self.events[i][0] < end:
            return False
        
        # 插入新日程
        self.events.insert(i, (start, end))
        return True


# 测试
if __name__ == "__main__":
    calendar = MyCalendar()
    print(calendar.book(10, 20))  # True
    print(calendar.book(15, 25))  # False
    print(calendar.book(20, 30))  # True