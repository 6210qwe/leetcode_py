# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1165
标题: Meeting Scheduler
难度: medium
链接: https://leetcode.cn/problems/meeting-scheduler/
题目类型: 数组、双指针、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
给定两个数组 slots1 和 slots2，分别表示两个人的空闲时间。slots1[i] = [start, end] 表示第一个人从 start 到 end 有空。
同样，slots2[j] = [start, end] 表示第二个人从 start 别到 end 有空。给定一个 meetingDuration，返回两个人最早可以安排会议的时间段。
如果没有满足条件的时间段，则返回空列表。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针方法找到两个时间段的交集，并检查是否满足会议时长要求。

算法步骤:
1. 对两个时间段数组进行排序。
2. 使用双指针遍历两个数组，找到第一个满足会议时长要求的时间段。
3. 如果找到满足条件的时间段，返回该时间段；否则返回空列表。

关键点:
- 排序后使用双指针可以高效地找到交集。
- 检查每个交集时间段是否满足会议时长要求。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n + m log m)，其中 n 和 m 分别是 slots1 和 slots2 的长度，因为排序操作的时间复杂度是 O(n log n) 和 O(m log m)。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minAvailableDuration(slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
    """
    函数式接口 - 找到最早可以安排会议的时间段
    """
    # 对两个时间段数组进行排序
    slots1.sort()
    slots2.sort()

    i, j = 0, 0
    while i < len(slots1) and j < len(slots2):
        # 找到两个时间段的交集
        start = max(slots1[i][0], slots2[j][0])
        end = min(slots1[i][1], slots2[j][1])

        # 检查交集时间段是否满足会议时长要求
        if end - start >= duration:
            return [start, start + duration]

        # 移动指针
        if slots1[i][1] < slots2[j][1]:
            i += 1
        else:
            j += 1

    return []

Solution = create_solution(minAvailableDuration)