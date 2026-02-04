# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3289
标题: Earliest Second to Mark Indices II
难度: hard
链接: https://leetcode.cn/problems/earliest-second-to-mark-indices-ii/
题目类型: 贪心、数组、二分查找、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3049. 标记所有下标的最早秒数 II - 给你两个下标从 1 开始的整数数组 nums 和 changeIndices ，数组的长度分别为 n 和 m 。 一开始，nums 中所有下标都是未标记的，你的任务是标记 nums 中 所有 下标。 从第 1 秒到第 m 秒（包括 第 m 秒），对于每一秒 s ，你可以执行以下操作 之一 ： * 选择范围 [1, n] 中的一个下标 i ，并且将 nums[i] 减少 1 。 * 将 nums[changeIndices[s]] 设置成任意的 非负 整数。 * 选择范围 [1, n] 中的一个下标 i ， 满足 nums[i] 等于 0, 并 标记 下标 i 。 * 什么也不做。 请你返回范围 [1, m] 中的一个整数，表示最优操作下，标记 nums 中 所有 下标的 最早秒数 ，如果无法标记所有下标，返回 -1 。 示例 1： 输入：nums = [3,2,3], changeIndices = [1,3,2,2,2,2,3] 输出：6 解释：这个例子中，我们总共有 7 秒。按照以下操作标记所有下标： 第 1 秒：将 nums[changeIndices[1]] 变为 0 。nums 变为 [0,2,3] 。 第 2 秒：将 nums[changeIndices[2]] 变为 0 。nums 变为 [0,2,0] 。 第 3 秒：将 nums[changeIndices[3]] 变为 0 。nums 变为 [0,0,0] 。 第 4 秒：标记下标 1 ，因为 nums[1] 等于 0 。 第 5 秒：标记下标 2 ，因为 nums[2] 等于 0 。 第 6 秒：标记下标 3 ，因为 nums[3] 等于 0 。 现在所有下标已被标记。 最早可以在第 6 秒标记所有下标。 所以答案是 6 。 示例 2： 输入：nums = [0,0,1,2], changeIndices = [1,2,1,2,1,2,1,2] 输出：7 解释：这个例子中，我们总共有 8 秒。按照以下操作标记所有下标： 第 1 秒：标记下标 1 ，因为 nums[1] 等于 0 。 第 2 秒：标记下标 2 ，因为 nums[2] 等于 0 。 第 3 秒：将 nums[4] 减少 1 。nums 变为 [0,0,1,1] 。 第 4 秒：将 nums[4] 减少 1 。nums 变为 [0,0,1,0] 。 第 5 秒：将 nums[3] 减少 1 。nums 变为 [0,0,0,0] 。 第 6 秒：标记下标 3 ，因为 nums[3] 等于 0 。 第 7 秒：标记下标 4 ，因为 nums[4] 等于 0 。 现在所有下标已被标记。 最早可以在第 7 秒标记所有下标。 所以答案是 7 。 示例 3： 输入：nums = [1,2,3], changeIndices = [1,2,3] 输出：-1 解释：这个例子中，无法标记所有下标，因为我们没有足够的秒数。 所以答案是 -1 。 提示： * 1 <= n == nums.length <= 5000 * 0 <= nums[i] <= 109 * 1 <= m == changeIndices.length <= 5000 * 1 <= changeIndices[i] <= n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和二分查找来找到最早可以标记所有下标的秒数。

算法步骤:
1. 初始化一个布尔数组 `marked` 来记录每个下标是否被标记。
2. 使用二分查找来确定最早可以标记所有下标的秒数。
3. 在每次二分查找的过程中，检查当前秒数是否可以标记所有下标。
4. 如果可以标记所有下标，则更新右边界；否则，更新左边界。
5. 最后返回最早可以标记所有下标的秒数，如果无法标记所有下标，返回 -1。

关键点:
- 使用二分查找来减少时间复杂度。
- 通过贪心算法来确定每一步的最佳操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m log m)，其中 m 是 changeIndices 的长度。二分查找的时间复杂度是 O(log m)，每次检查的时间复杂度是 O(m)。
空间复杂度: O(n)，其中 n 是 nums 的长度。需要一个布尔数组来记录每个下标是否被标记。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def earliest_second_to_mark_indices(nums: List[int], change_indices: List[int]) -> int:
    """
    返回最早可以标记所有下标的秒数，如果无法标记所有下标，返回 -1。
    """
    n = len(nums)
    m = len(change_indices)

    def can_mark_all_by_second(second: int) -> bool:
        marked = [False] * n
        operations = [0] * n

        for s in range(second):
            idx = change_indices[s] - 1
            if not marked[idx]:
                if nums[idx] > 0:
                    operations[idx] += 1
                    if operations[idx] >= nums[idx]:
                        marked[idx] = True
                else:
                    marked[idx] = True

        return all(marked)

    left, right = 1, m + 1
    while left < right:
        mid = (left + right) // 2
        if can_mark_all_by_second(mid):
            right = mid
        else:
            left = mid + 1

    return left if left <= m else -1


Solution = create_solution(earliest_second_to_mark_indices)