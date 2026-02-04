# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3260
标题: Divide an Array Into Subarrays With Minimum Cost II
难度: hard
链接: https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/
题目类型: 数组、哈希表、滑动窗口、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3013. 将数组分成最小总代价的子数组 II - 给你一个下标从 0 开始长度为 n 的整数数组 nums 和两个 正 整数 k 和 dist 。 一个数组的 代价 是数组中的 第一个 元素。比方说，[1,2,3] 的代价为 1 ，[3,4,1] 的代价为 3 。 你需要将 nums 分割成 k 个 连续且互不相交 的子数组，满足 第二 个子数组与第 k 个子数组中第一个元素的下标距离 不超过 dist 。换句话说，如果你将 nums 分割成子数组 nums[0..(i1 - 1)], nums[i1..(i2 - 1)], ..., nums[ik-1..(n - 1)] ，那么它需要满足 ik-1 - i1 <= dist 。 请你返回这些子数组的 最小 总代价。 示例 1： 输入：nums = [1,3,2,6,4,2], k = 3, dist = 3 输出：5 解释：将数组分割成 3 个子数组的最优方案是：[1,3] ，[2,6,4] 和 [2] 。这是一个合法分割，因为 ik-1 - i1 等于 5 - 2 = 3 ，等于 dist 。总代价为 nums[0] + nums[2] + nums[5] ，也就是 1 + 2 + 2 = 5 。 5 是分割成 3 个子数组的最小总代价。 示例 2： 输入：nums = [10,1,2,2,2,1], k = 4, dist = 3 输出：15 解释：将数组分割成 4 个子数组的最优方案是：[10] ，[1] ，[2] 和 [2,2,1] 。这是一个合法分割，因为 ik-1 - i1 等于 3 - 1 = 2 ，小于 dist 。总代价为 nums[0] + nums[1] + nums[2] + nums[3] ，也就是 10 + 1 + 2 + 2 = 15 。 分割 [10] ，[1] ，[2,2,2] 和 [1] 不是一个合法分割，因为 ik-1 和 i1 的差为 5 - 1 = 4 ，大于 dist 。 15 是分割成 4 个子数组的最小总代价。 示例 3： 输入：nums = [10,8,18,9], k = 3, dist = 1 输出：36 解释：将数组分割成 4 个子数组的最优方案是：[10] ，[8] 和 [18,9] 。这是一个合法分割，因为 ik-1 - i1 等于 2 - 1 = 1 ，等于 dist 。总代价为 nums[0] + nums[1] + nums[2] ，也就是 10 + 8 + 18 = 36 。 分割 [10] ，[8,18] 和 [9] 不是一个合法分割，因为 ik-1 和 i1 的差为 3 - 1 = 2 ，大于 dist 。 36 是分割成 3 个子数组的最小总代价。 提示： * 3 <= n <= 105 * 1 <= nums[i] <= 109 * 3 <= k <= n * k - 2 <= dist <= n - 2
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和优先队列来维护当前窗口内的最小值，并确保窗口大小不超过 dist。

算法步骤:
1. 初始化一个大顶堆和一个小顶堆，分别用于维护当前窗口内的最小值和最大值。
2. 初始化一个变量 `min_cost` 来记录最小总代价。
3. 遍历数组，使用滑动窗口技术，确保窗口大小不超过 dist。
4. 在每次移动窗口时，更新大顶堆和小顶堆，并计算当前窗口内的最小值。
5. 更新 `min_cost`，并返回最终结果。

关键点:
- 使用大顶堆和小顶堆来高效地维护当前窗口内的最小值。
- 滑动窗口技术确保窗口大小不超过 dist。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log k)，其中 n 是数组长度，k 是子数组数量。每次插入和删除堆的时间复杂度为 O(log k)。
空间复杂度: O(k)，堆的大小最多为 k。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import heapq

def solution_function_name(nums: List[int], k: int, dist: int) -> int:
    n = len(nums)
    min_cost = float('inf')
    
    # 大顶堆和小顶堆
    max_heap = []
    min_heap = []
    
    # 初始窗口
    for i in range(1, k):
        heapq.heappush(max_heap, -nums[i])
        heapq.heappush(min_heap, nums[i])
    
    # 计算初始窗口的最小值
    min_sum = sum(nums[i] for i in range(1, k))
    
    for i in range(k - 1, n):
        if i - (k - 2) > dist:
            # 移除超出窗口范围的元素
            if -max_heap[0] == nums[i - dist - 1]:
                heapq.heappop(max_heap)
            else:
                min_sum += nums[i - dist - 1]
                while min_heap and min_heap[0] != nums[i - dist - 1]:
                    heapq.heappop(min_heap)
                heapq.heappop(min_heap)
        
        # 添加新元素到窗口
        if i < n:
            heapq.heappush(max_heap, -nums[i])
            heapq.heappush(min_heap, nums[i])
            min_sum += nums[i]
        
        # 更新最小总代价
        min_cost = min(min_cost, nums[0] + min_sum + -max_heap[0])
        
        # 调整堆
        while max_heap and -max_heap[0] > min_heap[0]:
            max_val = -heapq.heappop(max_heap)
            min_val = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -min_val)
            heapq.heappush(min_heap, max_val)
            min_sum += max_val - min_val
    
    return min_cost

Solution = create_solution(solution_function_name)