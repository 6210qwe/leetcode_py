# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3496
标题: Minimum Number of Seconds to Make Mountain Height Zero
难度: medium
链接: https://leetcode.cn/problems/minimum-number-of-seconds-to-make-mountain-height-zero/
题目类型: 贪心、数组、数学、二分查找、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3296. 移山所需的最少秒数 - 给你一个整数 mountainHeight 表示山的高度。 同时给你一个整数数组 workerTimes，表示工人们的工作时间（单位：秒）。 工人们需要 同时 进行工作以 降低 山的高度。对于工人 i : * 山的高度降低 x，需要花费 workerTimes[i] + workerTimes[i] * 2 + ... + workerTimes[i] * x 秒。例如： * 山的高度降低 1，需要 workerTimes[i] 秒。 * 山的高度降低 2，需要 workerTimes[i] + workerTimes[i] * 2 秒，依此类推。 返回一个整数，表示工人们使山的高度降低到 0 所需的 最少 秒数。 示例 1： 输入： mountainHeight = 4, workerTimes = [2,1,1] 输出： 3 解释： 将山的高度降低到 0 的一种方式是： * 工人 0 将高度降低 1，花费 workerTimes[0] = 2 秒。 * 工人 1 将高度降低 2，花费 workerTimes[1] + workerTimes[1] * 2 = 3 秒。 * 工人 2 将高度降低 1，花费 workerTimes[2] = 1 秒。 因为工人同时工作，所需的最少时间为 max(2, 3, 1) = 3 秒。 示例 2： 输入： mountainHeight = 10, workerTimes = [3,2,2,4] 输出： 12 解释： * 工人 0 将高度降低 2，花费 workerTimes[0] + workerTimes[0] * 2 = 9 秒。 * 工人 1 将高度降低 3，花费 workerTimes[1] + workerTimes[1] * 2 + workerTimes[1] * 3 = 12 秒。 * 工人 2 将高度降低 3，花费 workerTimes[2] + workerTimes[2] * 2 + workerTimes[2] * 3 = 12 秒。 * 工人 3 将高度降低 2，花费 workerTimes[3] + workerTimes[3] * 2 = 12 秒。 所需的最少时间为 max(9, 12, 12, 12) = 12 秒。 示例 3： 输入： mountainHeight = 5, workerTimes = [1] 输出： 15 解释： 这个示例中只有一个工人，所以答案是 workerTimes[0] + workerTimes[0] * 2 + workerTimes[0] * 3 + workerTimes[0] * 4 + workerTimes[0] * 5 = 15 秒。 提示： * 1 <= mountainHeight <= 105 * 1 <= workerTimes.length <= 104 * 1 <= workerTimes[i] <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和二分查找来找到最小的时间。

算法步骤:
1. 定义一个辅助函数 `can_finish` 来判断在给定时间内是否可以将山的高度降低到 0。
2. 使用二分查找来找到最小的时间，使得所有工人在该时间内可以将山的高度降低到 0。

关键点:
- 辅助函数 `can_finish` 通过计算每个工人在给定时间内可以降低的高度来判断是否可以完成任务。
- 二分查找的范围是从 1 到 `mountainHeight * min(workerTimes)`。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log(max_height * min_time))，其中 n 是 workerTimes 的长度，max_height 是 mountainHeight，min_time 是 workerTimes 中的最小值。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def can_finish(mountain_height: int, time: int, worker_times: List[int]) -> bool:
    total_reduced = 0
    for worker_time in worker_times:
        # 计算当前工人在给定时间内可以降低的高度
        reduced = 0
        while (reduced + 1) * worker_time <= time:
            reduced += 1
        total_reduced += reduced
        if total_reduced >= mountain_height:
            return True
    return False

def minimum_seconds_to_make_mountain_height_zero(mountain_height: int, worker_times: List[int]) -> int:
    left, right = 1, mountain_height * min(worker_times)
    while left < right:
        mid = (left + right) // 2
        if can_finish(mountain_height, mid, worker_times):
            right = mid
        else:
            left = mid + 1
    return left

Solution = create_solution(minimum_seconds_to_make_mountain_height_zero)