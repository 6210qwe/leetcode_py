# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1649
标题: Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
难度: medium
链接: https://leetcode.cn/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/
题目类型: 贪心、数组、哈希表、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1546. 和为目标值且不重叠的非空子数组的最大数目 - 给你一个数组 nums 和一个整数 target 。 请你返回 非空不重叠 子数组的最大数目，且每个子数组中数字和都为 target 。 示例 1： 输入：nums = [1,1,1,1,1], target = 2 输出：2 解释：总共有 2 个不重叠子数组（加粗数字表示） [1,1,1,1,1] ，它们的和为目标值 2 。 示例 2： 输入：nums = [-1,3,5,1,4,2,-9], target = 6 输出：2 解释：总共有 3 个子数组和为 6 。 ([5,1], [4,2], [3,5,1,4,2,-9]) 但只有前 2 个是不重叠的。 示例 3： 输入：nums = [-2,6,6,3,5,4,1,2,8], target = 10 输出：3 示例 4： 输入：nums = [0,0,0], target = 0 输出：3 提示： * 1 <= nums.length <= 10^5 * -10^4 <= nums[i] <= 10^4 * 0 <= target <= 10^6
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和和哈希表来记录和为 target 的子数组，并确保这些子数组不重叠。

算法步骤:
1. 初始化前缀和 `prefix_sum` 为 0，哈希表 `seen` 用于存储前缀和及其对应的索引。
2. 遍历数组 `nums`，计算当前前缀和 `prefix_sum`。
3. 检查 `prefix_sum - target` 是否在 `seen` 中，如果在，则找到了一个和为 `target` 的子数组。
4. 更新 `seen` 中的前缀和及其对应的索引，确保子数组不重叠。
5. 记录找到的子数组数量。

关键点:
- 使用哈希表 `seen` 来存储前缀和及其对应的索引，以便快速查找和更新。
- 确保子数组不重叠，通过更新 `seen` 中的前缀和及其对应的索引。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组 `nums` 的长度。我们只需要遍历数组一次。
空间复杂度: O(n)，哈希表 `seen` 在最坏情况下需要存储 n 个前缀和。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_non_overlapping_subarrays(nums: List[int], target: int) -> int:
    """
    函数式接口 - 返回非空不重叠子数组的最大数目，且每个子数组中数字和都为 target。
    """
    prefix_sum = 0
    seen = {0: -1}  # 前缀和为 0 的初始位置
    count = 0
    last_end = -1  # 上一个子数组的结束位置

    for i, num in enumerate(nums):
        prefix_sum += num
        if prefix_sum - target in seen and seen[prefix_sum - target] >= last_end:
            count += 1
            last_end = i
        seen[prefix_sum] = i

    return count


Solution = create_solution(max_non_overlapping_subarrays)