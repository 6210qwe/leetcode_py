# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1851
标题: Maximum Number of Events That Can Be Attended II
难度: hard
链接: https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended-ii/
题目类型: 数组、二分查找、动态规划、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1751. 最多可以参加的会议数目 II - 给你一个 events 数组，其中 events[i] = [startDayi, endDayi, valuei] ，表示第 i 个会议在 startDayi 天开始，第 endDayi 天结束，如果你参加这个会议，你能得到价值 valuei 。同时给你一个整数 k 表示你能参加的最多会议数目。 你同一时间只能参加一个会议。如果你选择参加某个会议，那么你必须 完整 地参加完这个会议。会议结束日期是包含在会议内的，也就是说你不能同时参加一个开始日期与另一个结束日期相同的两个会议。 请你返回能得到的会议价值 最大和 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/02/06/screenshot-2021-01-11-at-60048-pm.png] 输入：events = [[1,2,4],[3,4,3],[2,3,1]], k = 2 输出：7 解释：选择绿色的活动会议 0 和 1，得到总价值和为 4 + 3 = 7 。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/02/06/screenshot-2021-01-11-at-60150-pm.png] 输入：events = [[1,2,4],[3,4,3],[2,3,10]], k = 2 输出：10 解释：参加会议 2 ，得到价值和为 10 。 你没法再参加别的会议了，因为跟会议 2 有重叠。你 不 需要参加满 k 个会议。 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/02/06/screenshot-2021-01-11-at-60703-pm.png] 输入：events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3 输出：9 解释：尽管会议互不重叠，你只能参加 3 个会议，所以选择价值最大的 3 个会议。 提示： * 1 <= k <= events.length * 1 <= k * events.length <= 106 * 1 <= startDayi <= endDayi <= 109 * 1 <= valuei <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和二分查找来解决这个问题。

算法步骤:
1. 按照会议的结束时间对会议进行排序。
2. 使用动态规划数组 dp[i][j] 表示前 i 个会议中选择 j 个会议的最大价值。
3. 对于每个会议，使用二分查找找到最后一个结束时间小于当前会议开始时间的会议索引。
4. 更新 dp 数组。

关键点:
- 动态规划状态转移方程：dp[i][j] = max(dp[i-1][j], dp[prev][j-1] + value)
- 二分查找用于快速找到最后一个结束时间小于当前会议开始时间的会议索引。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * k * log n)，其中 n 是 events 的长度，k 是最大会议数量。排序的时间复杂度是 O(n log n)，每次更新 dp 数组需要 O(k) 时间，并且需要进行二分查找 O(log n)。
空间复杂度: O(n * k)，dp 数组的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import bisect

def max_value(events: List[List[int]], k: int) -> int:
    """
    函数式接口 - 返回最多可以参加的会议价值最大和
    """
    # 按结束时间排序
    events.sort(key=lambda x: x[1])
    
    n = len(events)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            # 二分查找找到最后一个结束时间小于当前会议开始时间的会议索引
            prev = bisect.bisect_left([e[1] for e in events], events[i-1][0]) - 1
            dp[i][j] = max(dp[i-1][j], dp[prev+1][j-1] + events[i-1][2])
    
    return dp[n][k]

Solution = create_solution(max_value)