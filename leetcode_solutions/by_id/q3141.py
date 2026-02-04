# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3141
标题: Minimum Size Subarray in Infinite Array
难度: medium
链接: https://leetcode.cn/problems/minimum-size-subarray-in-infinite-array/
题目类型: 数组、哈希表、前缀和、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2875. 无限数组的最短子数组 - 给你一个下标从 0 开始的数组 nums 和一个整数 target 。 下标从 0 开始的数组 infinite_nums 是通过无限地将 nums 的元素追加到自己之后生成的。 请你从 infinite_nums 中找出满足 元素和 等于 target 的 最短 子数组，并返回该子数组的长度。如果不存在满足条件的子数组，返回 -1 。 示例 1： 输入：nums = [1,2,3], target = 5 输出：2 解释：在这个例子中 infinite_nums = [1,2,3,1,2,3,1,2,...] 。 区间 [1,2] 内的子数组的元素和等于 target = 5 ，且长度 length = 2 。 可以证明，当元素和等于目标值 target = 5 时，2 是子数组的最短长度。 示例 2： 输入：nums = [1,1,1,2,3], target = 4 输出：2 解释：在这个例子中 infinite_nums = [1,1,1,2,3,1,1,1,2,3,1,1,...]. 区间 [4,5] 内的子数组的元素和等于 target = 4 ，且长度 length = 2 。 可以证明，当元素和等于目标值 target = 4 时，2 是子数组的最短长度。 示例 3： 输入：nums = [2,4,6,8], target = 3 输出：-1 解释：在这个例子中 infinite_nums = [2,4,6,8,2,4,6,8,...] 。 可以证明，不存在元素和等于目标值 target = 3 的子数组。 提示： * 1 <= nums.length <= 105 * 1 <= nums[i] <= 105 * 1 <= target <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和前缀和来找到最短子数组。

算法步骤:
1. 计算数组 `nums` 的总和 `total_sum`。
2. 如果 `target` 大于 `total_sum`，则需要考虑多个 `nums` 的拼接。
3. 使用滑动窗口和前缀和来找到满足条件的最短子数组。
4. 如果找不到满足条件的子数组，返回 -1。

关键点:
- 使用滑动窗口来维护当前子数组的和。
- 使用前缀和来快速计算子数组的和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_size_subarray(nums: List[int], target: int) -> int:
    """
    函数式接口 - 找到满足元素和等于 target 的最短子数组长度
    """
    n = len(nums)
    total_sum = sum(nums)
    if target > total_sum:
        repeat = (target // total_sum) + 1
        nums = nums * repeat
        n = len(nums)

    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(n):
        current_sum += nums[right]
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else -1


Solution = create_solution(min_size_subarray)