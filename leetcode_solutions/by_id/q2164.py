# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2164
标题: Two Best Non-Overlapping Events
难度: medium
链接: https://leetcode.cn/problems/two-best-non-overlapping-events/
题目类型: 数组、二分查找、动态规划、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2054. 两个最好的不重叠活动 - 给你一个下标从 0 开始的二维整数数组 events ，其中 events[i] = [startTimei, endTimei, valuei] 。第 i 个活动开始于 startTimei ，结束于 endTimei ，如果你参加这个活动，那么你可以得到价值 valuei 。你 最多 可以参加 两个时间不重叠 活动，使得它们的价值之和 最大 。 请你返回价值之和的 最大值 。 注意，活动的开始时间和结束时间是 包括 在活动时间内的，也就是说，你不能参加两个活动且它们之一的开始时间等于另一个活动的结束时间。更具体的，如果你参加一个活动，且结束时间为 t ，那么下一个活动必须在 t + 1 或之后的时间开始。 示例 1: [https://assets.leetcode.com/uploads/2026/01/03/untitled-diagramdrawio.png] 输入：events = [[1,3,2],[4,5,2],[2,4,3]] 输出：4 解释：选择绿色的活动 0 和 1 ，价值之和为 2 + 2 = 4 。 示例 2： Example 1 Diagram [https://assets.leetcode.com/uploads/2026/01/03/2054b.png] 输入：events = [[1,3,2],[4,5,2],[1,5,5]] 输出：5 解释：选择活动 2 ，价值和为 5 。 示例 3： [https://assets.leetcode.com/uploads/2026/01/03/2054c.png] 输入：events = [[1,5,3],[1,5,1],[6,6,5]] 输出：8 解释：选择活动 0 和 2 ，价值之和为 3 + 5 = 8 。 提示： * 2 <= events.length <= 105 * events[i].length == 3 * 1 <= startTimei <= endTimei <= 109 * 1 <= valuei <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和二分查找来找到两个不重叠活动的最大价值。

算法步骤:
1. 按结束时间对活动进行排序。
2. 使用一个数组 `dp` 来记录到当前活动为止的最大价值。
3. 对于每个活动，使用二分查找找到其之前结束的最后一个活动，并更新 `dp` 数组。
4. 计算最大价值。

关键点:
- 通过排序和二分查找来优化查找过程。
- 使用动态规划来记录中间结果，避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 events 的长度。排序操作的时间复杂度是 O(n log n)，二分查找的时间复杂度是 O(log n)。
空间复杂度: O(n)，用于存储 `dp` 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def maxTwoEvents(events: List[List[int]]) -> int:
    # 按结束时间排序
    events.sort(key=lambda x: x[1])
    
    n = len(events)
    dp = [0] * n
    dp[0] = events[0][2]
    
    for i in range(1, n):
        dp[i] = max(dp[i-1], events[i][2])
    
    def binary_search(start, end, target):
        while start < end:
            mid = (start + end) // 2
            if events[mid][1] < target:
                start = mid + 1
            else:
                end = mid
        return start - 1
    
    max_value = 0
    for i in range(n):
        start, end, value = events[i]
        if start > 1:
            idx = binary_search(0, i, start)
            if idx >= 0:
                max_value = max(max_value, dp[idx] + value)
        max_value = max(max_value, value)
    
    return max_value

Solution = create_solution(maxTwoEvents)