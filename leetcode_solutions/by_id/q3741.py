# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3741
标题: Reschedule Meetings for Maximum Free Time II
难度: medium
链接: https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-ii/
题目类型: 贪心、数组、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3440. 重新安排会议得到最多空余时间 II - 给你一个整数 eventTime 表示一个活动的总时长，这个活动开始于 t = 0 ，结束于 t = eventTime 。 同时给你两个长度为 n 的整数数组 startTime 和 endTime 。它们表示这次活动中 n 个时间 没有重叠 的会议，其中第 i 个会议的时间为 [startTime[i], endTime[i]] 。 你可以重新安排 至多 一个会议，安排的规则是将会议时间平移，且保持原来的 会议时长 ，你的目的是移动会议后 最大化 最长 连续空余时间。 请你返回重新安排会议以后，可以得到的 最大 空余时间。 注意，会议 不能 安排到整个活动的时间以外，且会议之间需要保持互不重叠。 注意：重新安排会议以后，会议之间的顺序可以发生改变。 示例 1： 输入：eventTime = 5, startTime = [1,3], endTime = [2,5] 输出：2 解释： [https://assets.leetcode.com/uploads/2024/12/22/example0_rescheduled.png] 将 [1, 2] 的会议安排到 [2, 3] ，得到空余时间 [0, 2] 。 示例 2： 输入：eventTime = 10, startTime = [0,7,9], endTime = [1,8,10] 输出：7 解释： [https://assets.leetcode.com/uploads/2024/12/22/rescheduled_example0.png] 将 [0, 1] 的会议安排到 [8, 9] ，得到空余时间 [0, 7] 。 示例 3： 输入：eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10] 输出：6 解释： [https://assets.leetcode.com/uploads/2025/01/28/image3.png] 将 [3, 4] 的会议安排到 [8, 9] ，得到空余时间 [1, 7] 。 示例 4： 输入：eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5] 输出：0 解释： 活动中的所有时间都被会议安排满了。 提示： * 1 <= eventTime <= 109 * n == startTime.length == endTime.length * 2 <= n <= 105 * 0 <= startTime[i] < endTime[i] <= eventTime * endTime[i] <= startTime[i + 1] 其中 i 在范围 [0, n - 2] 之间。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 计算每个会议的初始空闲时间。
2. 尝试移动每个会议，计算移动后的最大空闲时间。

算法步骤:
1. 将所有会议按开始时间排序。
2. 计算每个会议前后的空闲时间。
3. 尝试移动每个会议，计算移动后的最大空闲时间。
4. 返回最大空闲时间。

关键点:
- 通过贪心算法找到最优解。
- 保持代码简洁和可读性。
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

from typing import List

def max_free_time(eventTime: int, startTime: List[int], endTime: List[int]) -> int:
    n = len(startTime)
    intervals = sorted(zip(startTime, endTime), key=lambda x: x[0])
    
    # Calculate initial free times
    free_times = []
    for i in range(n):
        if i == 0:
            free_times.append(intervals[i][0])
        else:
            free_times.append(intervals[i][0] - intervals[i-1][1])
    
    # Add the last free time
    free_times.append(eventTime - intervals[-1][1])
    
    # Try to move each meeting and calculate the maximum free time
    max_free = max(free_times)
    for i in range(n):
        duration = intervals[i][1] - intervals[i][0]
        
        # Move the meeting to the left
        if i > 0:
            new_free = intervals[i][0] - (intervals[i-1][1] - duration)
            max_free = max(max_free, min(new_free, free_times[i-1] + free_times[i]))
        
        # Move the meeting to the right
        if i < n - 1:
            new_free = (intervals[i+1][0] + duration) - intervals[i][1]
            max_free = max(max_free, min(new_free, free_times[i] + free_times[i+1]))
    
    return max_free

Solution = create_solution(max_free_time)