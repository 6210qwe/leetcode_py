# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2267
标题: Minimum Difference in Sums After Removal of Elements
难度: hard
链接: https://leetcode.cn/problems/minimum-difference-in-sums-after-removal-of-elements/
题目类型: 数组、动态规划、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2163. 删除元素后和的最小差值 - 给你一个下标从 0 开始的整数数组 nums ，它包含 3 * n 个元素。 你可以从 nums 中删除 恰好 n 个元素，剩下的 2 * n 个元素将会被分成两个 相同大小 的部分。 * 前面 n 个元素属于第一部分，它们的和记为 sumfirst 。 * 后面 n 个元素属于第二部分，它们的和记为 sumsecond 。 两部分和的 差值 记为 sumfirst - sumsecond 。 * 比方说，sumfirst = 3 且 sumsecond = 2 ，它们的差值为 1 。 * 再比方，sumfirst = 2 且 sumsecond = 3 ，它们的差值为 -1 。 请你返回删除 n 个元素之后，剩下两部分和的 差值的最小值 是多少。 示例 1： 输入：nums = [3,1,2] 输出：-1 解释：nums 有 3 个元素，所以 n = 1 。 所以我们需要从 nums 中删除 1 个元素，并将剩下的元素分成两部分。 - 如果我们删除 nums[0] = 3 ，数组变为 [1,2] 。两部分和的差值为 1 - 2 = -1 。 - 如果我们删除 nums[1] = 1 ，数组变为 [3,2] 。两部分和的差值为 3 - 2 = 1 。 - 如果我们删除 nums[2] = 2 ，数组变为 [3,1] 。两部分和的差值为 3 - 1 = 2 。 两部分和的最小差值为 min(-1,1,2) = -1 。 示例 2： 输入：nums = [7,9,5,8,1,3] 输出：1 解释：n = 2 。所以我们需要删除 2 个元素，并将剩下元素分为 2 部分。 如果我们删除元素 nums[2] = 5 和 nums[3] = 8 ，剩下元素为 [7,9,1,3] 。和的差值为 (7+9) - (1+3) = 12 。 为了得到最小差值，我们应该删除 nums[1] = 9 和 nums[4] = 1 ，剩下的元素为 [7,5,8,3] 。和的差值为 (7+5) - (8+3) = 1 。 观察可知，最优答案为 1 。 提示： * nums.length == 3 * n * 1 <= n <= 105 * 1 <= nums[i] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个最大堆和两个最小堆来维护前 n 个元素和后 n 个元素的最大和最小值。

算法步骤:
1. 将数组分成两部分，前 2n 个元素和后 2n 个元素。
2. 对于前 2n 个元素，使用一个最大堆来维护前 n 个最小值的和，使用一个最小堆来维护前 n 个最大值的和。
3. 对于后 2n 个元素，使用一个最大堆来维护后 n 个最小值的和，使用一个最小堆来维护后 n 个最大值的和。
4. 遍历前 2n 个元素，更新最大堆和最小堆，并计算当前的差值。
5. 遍历后 2n 个元素，更新最大堆和最小堆，并计算当前的差值。
6. 返回最小的差值。

关键点:
- 使用堆来高效地维护前 n 个最小值和最大值的和。
- 通过遍历和更新堆来计算最小的差值。
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
import heapq

def minimum_difference(nums: List[int]) -> int:
    n = len(nums) // 3
    left_max_heap = []
    left_min_heap = []
    right_max_heap = []
    right_min_heap = []

    # 初始化前 2n 个元素的堆
    for i in range(2 * n):
        if i < n:
            heapq.heappush(left_max_heap, -nums[i])
            heapq.heappush(right_min_heap, nums[i])
        else:
            heapq.heappush(left_min_heap, nums[i])
            heapq.heappush(right_max_heap, -nums[i])

    # 计算初始的和
    left_sum = -sum(left_max_heap)
    right_sum = sum(right_min_heap)

    min_diff = left_sum - right_sum

    # 遍历前 2n 个元素
    for i in range(2 * n, 3 * n):
        # 更新右半部分的堆
        if nums[i] < -right_max_heap[0]:
            right_sum += nums[i] + right_max_heap[0]
            heapq.heapreplace(right_max_heap, -nums[i])
        else:
            heapq.heappush(right_min_heap, nums[i])
            right_sum += nums[i]

        # 更新左半部分的堆
        if -left_max_heap[0] > nums[i - 2 * n]:
            left_sum += -left_max_heap[0] - nums[i - 2 * n]
            heapq.heapreplace(left_max_heap, -nums[i - 2 * n])
        else:
            heapq.heappush(left_min_heap, nums[i - 2 * n])
            left_sum -= nums[i - 2 * n]

        # 计算当前的差值
        min_diff = min(min_diff, left_sum - right_sum)

    return min_diff

Solution = create_solution(minimum_difference)