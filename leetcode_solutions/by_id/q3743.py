# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3743
标题: Reschedule Meetings for Maximum Free Time I
难度: medium
链接: https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-i/
题目类型: 贪心、数组、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3439. 重新安排会议得到最多空余时间 I - 给你一个整数 eventTime 表示一个活动的总时长，这个活动开始于 t = 0 ，结束于 t = eventTime 。 同时给你两个长度为 n 的整数数组 startTime 和 endTime 。它们表示这次活动中 n 个时间 没有重叠 的会议，其中第 i 个会议的时间为 [startTime[i], endTime[i]] 。 你可以重新安排 至多 k 个会议，安排的规则是将会议时间平移，且保持原来的 会议时长 ，你的目的是移动会议后 最大化 相邻两个会议之间的 最长 连续空余时间。 移动前后所有会议之间的 相对 顺序需要保持不变，而且会议时间也需要保持互不重叠。 请你返回重新安排会议以后，可以得到的 最大 空余时间。 注意，会议 不能 安排到整个活动的时间以外。 示例 1： 输入：eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5] 输出：2 解释： [https://assets.leetcode.com/uploads/2024/12/21/example0_rescheduled.png] 将 [1, 2] 的会议安排到 [2, 3] ，得到空余时间 [0, 2] 。 示例 2： 输入：eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10] 输出：6 解释： [https://assets.leetcode.com/uploads/2024/12/21/example1_rescheduled.png] 将 [2, 4] 的会议安排到 [1, 3] ，得到空余时间 [3, 9] 。 示例 3： 输入：eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5] 输出：0 解释： 活动中的所有时间都被会议安排满了。 提示： * 1 <= eventTime <= 109 * n == startTime.length == endTime.length * 2 <= n <= 105 * 1 <= k <= n * 0 <= startTime[i] < endTime[i] <= eventTime * endTime[i] <= startTime[i + 1] 其中 i 在范围 [0, n - 2] 之间。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法来最大化相邻会议之间的空余时间。通过优先移动间隔较小的会议，我们可以最大化空余时间。

算法步骤:
1. 计算每个会议的间隔时间。
2. 选择最小的 k 个间隔进行调整。
3. 通过平移会议来最大化空余时间。

关键点:
- 优先移动间隔较小的会议。
- 保持会议的相对顺序不变。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
    """
    函数式接口 - 重新安排会议以最大化空余时间
    """
    n = len(startTime)
    intervals = [(endTime[i] - startTime[i], startTime[i], endTime[i]) for i in range(n)]
    intervals.sort(key=lambda x: x[0])

    # 选择最小的 k 个间隔进行调整
    for i in range(min(k, n)):
        _, start, end = intervals[i]
        if i == 0:
            new_start = 0
        else:
            new_start = intervals[i-1][2]
        intervals[i] = (end - start, new_start, new_start + (end - start))

    # 重新计算最大空余时间
    max_gap = 0
    for i in range(1, n):
        gap = intervals[i][1] - intervals[i-1][2]
        max_gap = max(max_gap, gap)

    # 计算最后一个会议和活动结束时间之间的空余时间
    max_gap = max(max_gap, eventTime - intervals[-1][2])

    return max_gap


Solution = create_solution(solution_function_name)