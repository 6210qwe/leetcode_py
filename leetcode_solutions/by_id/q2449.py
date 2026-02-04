# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2449
标题: Maximum Number of Robots Within Budget
难度: hard
链接: https://leetcode.cn/problems/maximum-number-of-robots-within-budget/
题目类型: 队列、数组、二分查找、前缀和、滑动窗口、单调队列、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2398. 预算内的最多机器人数目 - 你有 n 个机器人，给你两个下标从 0 开始的整数数组 chargeTimes 和 runningCosts ，两者长度都为 n 。第 i 个机器人充电时间为 chargeTimes[i] 单位时间，花费 runningCosts[i] 单位时间运行。再给你一个整数 budget 。 运行 k 个机器人 总开销 是 max(chargeTimes) + k * sum(runningCosts) ，其中 max(chargeTimes) 是这 k 个机器人中最大充电时间，sum(runningCosts) 是这 k 个机器人的运行时间之和。 请你返回在 不超过 budget 的前提下，你 最多 可以运行的 连续 的机器人数目为多少。 示例 1： 输入：chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25 输出：3 解释： 可以在 budget 以内运行所有单个机器人或者连续运行 2 个机器人。 选择前 3 个机器人，可以得到答案最大值 3 。总开销是 max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24 ，小于 25 。 可以看出无法在 budget 以内连续运行超过 3 个机器人，所以我们返回 3 。 示例 2： 输入：chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19 输出：0 解释：即使运行任何一个单个机器人，还是会超出 budget，所以我们返回 0 。 提示： * chargeTimes.length == runningCosts.length == n * 1 <= n <= 5 * 104 * 1 <= chargeTimes[i], runningCosts[i] <= 105 * 1 <= budget <= 1015
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和双端队列来维护当前窗口内的最大充电时间和运行成本的前缀和。

算法步骤:
1. 初始化前缀和数组 `prefix_sum`，用于存储 `runningCosts` 的前缀和。
2. 使用双端队列 `deque` 来维护当前窗口内的最大充电时间。
3. 使用滑动窗口遍历数组，计算当前窗口的总开销，并检查是否超过预算。
4. 如果当前窗口的总开销不超过预算，更新结果并扩展窗口；否则，收缩窗口。
5. 返回最大窗口大小。

关键点:
- 使用双端队列来高效地维护当前窗口内的最大充电时间。
- 使用前缀和数组来快速计算当前窗口的运行成本之和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import deque

def maximumRobots(chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
    n = len(chargeTimes)
    prefix_sum = [0] * (n + 1)
    
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + runningCosts[i]
    
    def get_running_cost(start, end):
        return prefix_sum[end + 1] - prefix_sum[start]
    
    max_robots = 0
    left = 0
    deque_max = deque()
    
    for right in range(n):
        while deque_max and chargeTimes[deque_max[-1]] <= chargeTimes[right]:
            deque_max.pop()
        deque_max.append(right)
        
        while deque_max and chargeTimes[deque_max[0]] + (right - left + 1) * get_running_cost(left, right) > budget:
            if deque_max[0] == left:
                deque_max.popleft()
            left += 1
        
        max_robots = max(max_robots, right - left + 1)
    
    return max_robots

Solution = create_solution(maximumRobots)