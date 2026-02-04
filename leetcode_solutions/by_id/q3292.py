# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3292
标题: Earliest Second to Mark Indices I
难度: medium
链接: https://leetcode.cn/problems/earliest-second-to-mark-indices-i/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3048. 标记所有下标的最早秒数 I - 给你两个下标从 1 开始的整数数组 nums 和 changeIndices ，数组的长度分别为 n 和 m 。 一开始，nums 中所有下标都是未标记的，你的任务是标记 nums 中 所有 下标。 从第 1 秒到第 m 秒（包括 第 m 秒），对于每一秒 s ，你可以执行以下操作 之一 ： * 选择范围 [1, n] 中的一个下标 i ，并且将 nums[i] 减少 1 。 * 如果 nums[changeIndices[s]] 等于 0 ，标记 下标 changeIndices[s] 。 * 什么也不做。 请你返回范围 [1, m] 中的一个整数，表示最优操作下，标记 nums 中 所有 下标的 最早秒数 ，如果无法标记所有下标，返回 -1 。 示例 1： 输入：nums = [2,2,0], changeIndices = [2,2,2,2,3,2,2,1] 输出：8 解释：这个例子中，我们总共有 8 秒。按照以下操作标记所有下标： 第 1 秒：选择下标 1 ，将 nums[1] 减少 1 。nums 变为 [1,2,0] 。 第 2 秒：选择下标 1 ，将 nums[1] 减少 1 。nums 变为 [0,2,0] 。 第 3 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [0,1,0] 。 第 4 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [0,0,0] 。 第 5 秒，标​​​​​记 changeIndices[5] ，也就是标记下标 3 ，因为 nums[3] 等于 0 。 第 6 秒，标​​​​​记 changeIndices[6] ，也就是标记下标 2 ，因为 nums[2] 等于 0 。 第 7 秒，什么也不做。 第 8 秒，标记 changeIndices[8] ，也就是标记下标 1 ，因为 nums[1] 等于 0 。 现在所有下标已被标记。 最早可以在第 8 秒标记所有下标。 所以答案是 8 。 示例 2： 输入：nums = [1,3], changeIndices = [1,1,1,2,1,1,1] 输出：6 解释：这个例子中，我们总共有 7 秒。按照以下操作标记所有下标： 第 1 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [1,2] 。 第 2 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [1,1] 。 第 3 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [1,0] 。 第 4 秒：标​​​​​记 changeIndices[4] ，也就是标记下标 2 ，因为 nums[2] 等于 0 。 第 5 秒：选择下标 1 ，将 nums[1] 减少 1 。nums 变为 [0,0] 。 第 6 秒：标​​​​​记 changeIndices[6] ，也就是标记下标 1 ，因为 nums[1] 等于 0 。 现在所有下标已被标记。 最早可以在第 6 秒标记所有下标。 所以答案是 6 。 示例 3： Input: nums = [0,1], changeIndices = [2,2,2] Output: -1 Explanation: 这个例子中，无法标记所有下标，因为下标 1 不在 changeIndices 中。 所以答案是 -1 。 提示： * 1 <= n == nums.length <= 2000 * 0 <= nums[i] <= 109 * 1 <= m == changeIndices.length <= 2000 * 1 <= changeIndices[i] <= n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找和贪心算法来确定最早可以标记所有下标的秒数。

算法步骤:
1. 初始化左右边界，left 为 1，right 为 m。
2. 在每次二分查找的过程中，计算中间值 mid。
3. 检查在 mid 秒内是否可以标记所有下标：
   - 使用一个计数器记录每个下标在 mid 秒内的出现次数。
   - 使用一个列表记录每个下标最后一次出现的时间。
   - 从后向前遍历 changeIndices，尝试标记下标并减少 nums 的值。
   - 如果所有下标都被标记，则更新右边界 right；否则更新左边界 left。
4. 返回 left 作为结果。

关键点:
- 使用二分查找来缩小时间范围。
- 贪心算法确保在尽可能早的时间内标记所有下标。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m log m)，其中 m 是 changeIndices 的长度。二分查找的时间复杂度为 O(log m)，每次检查的时间复杂度为 O(m)。
空间复杂度: O(n)，其中 n 是 nums 的长度。需要额外的空间来存储每个下标的出现次数和最后一次出现的时间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def earliest_second_to_mark_indices(nums: List[int], changeIndices: List[int]) -> int:
    n, m = len(nums), len(changeIndices)
    
    def can_mark_all_in_time(mid: int) -> bool:
        count = [0] * (n + 1)
        last_seen = [-1] * (n + 1)
        
        for i in range(mid):
            idx = changeIndices[i]
            count[idx] += 1
            last_seen[idx] = i
        
        operations_needed = 0
        for i in range(1, n + 1):
            if count[i] == 0:
                return False
            operations_needed += nums[i - 1] + 1
        
        for i in range(mid - 1, -1, -1):
            idx = changeIndices[i]
            if count[idx] > 0 and nums[idx - 1] >= 0:
                operations_needed -= 1
                if operations_needed == 0:
                    return True
                count[idx] -= 1
                nums[idx - 1] -= 1
                if nums[idx - 1] < 0:
                    return False
        return False
    
    left, right = 1, m
    while left < right:
        mid = (left + right) // 2
        if can_mark_all_in_time(mid):
            right = mid
        else:
            left = mid + 1
    
    return left if can_mark_all_in_time(left) else -1

Solution = create_solution(earliest_second_to_mark_indices)