# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 715
标题: Range Module
难度: hard
链接: https://leetcode.cn/problems/range-module/
题目类型: 设计、线段树、有序集合
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
715. Range 模块 - Range模块是跟踪数字范围的模块。设计一个数据结构来跟踪表示为 半开区间 的范围并查询它们。 半开区间 [left, right) 表示所有 left <= x < right 的实数 x 。 实现 RangeModule 类: * RangeModule() 初始化数据结构的对象。 * void addRange(int left, int right) 添加 半开区间 [left, right)，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，应当添加在区间 [left, right) 中尚未跟踪的任何数字到该区间中。 * boolean queryRange(int left, int right) 只有在当前正在跟踪区间 [left, right) 中的每一个实数时，才返回 true ，否则返回 false 。 * void removeRange(int left, int right) 停止跟踪 半开区间 [left, right) 中当前正在跟踪的每个实数。 示例 1： 输入 ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"] [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]] 输出 [null, null, null, true, false, true] 解释 RangeModule rangeModule = new RangeModule(); rangeModule.addRange(10, 20); rangeModule.removeRange(14, 16); rangeModule.queryRange(10, 14); 返回 true （区间 [10, 14) 中的每个数都正在被跟踪） rangeModule.queryRange(13, 15); 返回 false（未跟踪区间 [13, 15) 中像 14, 14.03, 14.17 这样的数字） rangeModule.queryRange(16, 17); 返回 true （尽管执行了删除操作，区间 [16, 17) 中的数字 16 仍然会被跟踪） 提示： * 1 <= left < right <= 109 * 在单个测试用例中，对 addRange 、 queryRange 和 removeRange 的调用总数不超过 104 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用有序集合 (SortedList) 来维护区间，通过二分查找和合并/分割区间来实现高效的操作。

算法步骤:
1. 初始化一个空的有序集合。
2. 对于 `addRange` 操作，找到需要合并的区间，并进行合并。
3. 对于 `queryRange` 操作，使用二分查找来判断区间是否完全包含在已有的区间内。
4. 对于 `removeRange` 操作，找到需要分割的区间，并进行分割。

关键点:
- 使用 `SortedList` 来维护区间，保证区间的有序性。
- 通过二分查找来快速定位区间。
- 合并和分割区间时，注意边界条件的处理。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) 对于每次操作，其中 n 是区间的数量。
空间复杂度: O(n) 用于存储区间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from sortedcontainers import SortedList
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class RangeModule:

    def __init__(self):
        self.intervals = SortedList()

    def addRange(self, left: int, right: int) -> None:
        # 找到需要合并的区间
        i = self.intervals.bisect_left((left, right))
        while i < len(self.intervals) and self.intervals[i][0] <= right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            self.intervals.pop(i)
        
        self.intervals.add((left, right))

    def queryRange(self, left: int, right: int) -> bool:
        # 使用二分查找来判断区间是否完全包含在已有的区间内
        i = self.intervals.bisect_left((left, float('inf')))
        if i == 0:
            return False
        return self.intervals[i-1][0] <= left and right <= self.intervals[i-1][1]

    def removeRange(self, left: int, right: int) -> None:
        # 找到需要分割的区间
        i = self.intervals.bisect_left((left, right))
        while i < len(self.intervals) and self.intervals[i][0] < right:
            if self.intervals[i][1] <= left:
                break
            if self.intervals[i][0] >= left:
                self.intervals[i] = (right, self.intervals[i][1])
                break
            else:
                self.intervals.add((self.intervals[i][0], left))
                if self.intervals[i][1] > right:
                    self.intervals.add((right, self.intervals[i][1]))
                self.intervals.remove(self.intervals[i])

Solution = create_solution(RangeModule)