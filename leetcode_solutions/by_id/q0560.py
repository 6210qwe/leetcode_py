# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 560
标题: Subarray Sum Equals K
难度: medium
链接: https://leetcode.cn/problems/subarray-sum-equals-k/
题目类型: 数组、哈希表、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
560. 和为 K 的子数组 - 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。 子数组是数组中元素的连续非空序列。 示例 1： 输入：nums = [1,1,1], k = 2 输出：2 示例 2： 输入：nums = [1,2,3], k = 3 输出：2 提示： * 1 <= nums.length <= 2 * 104 * -1000 <= nums[i] <= 1000 * -107 <= k <= 107
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和与哈希表来记录每个前缀和出现的次数，从而在 O(n) 时间内找到和为 k 的子数组。

算法步骤:
1. 初始化一个哈希表 `prefix_sum_count`，用于记录每个前缀和出现的次数。
2. 初始化变量 `current_sum` 为 0，用于记录当前的前缀和。
3. 初始化变量 `count` 为 0，用于记录和为 k 的子数组的个数。
4. 遍历数组 `nums`：
   - 更新 `current_sum`。
   - 检查 `current_sum - k` 是否在 `prefix_sum_count` 中，如果存在，则将对应的值加到 `count` 中。
   - 更新 `prefix_sum_count` 中 `current_sum` 的计数。

关键点:
- 使用哈希表来记录前缀和的出现次数，可以在 O(1) 时间内查找和更新。
- 通过 `current_sum - k` 来快速找到和为 k 的子数组。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组 `nums` 的长度。我们只需要遍历数组一次。
空间复杂度: O(n)，哈希表 `prefix_sum_count` 在最坏情况下需要存储 n 个不同的前缀和。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def subarray_sum(nums: List[int], k: int) -> int:
    """
    函数式接口 - 返回和为 k 的子数组的个数
    """
    prefix_sum_count = {0: 1}  # 初始化前缀和计数，初始值为 0 的前缀和出现 1 次
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        if (current_sum - k) in prefix_sum_count:
            count += prefix_sum_count[current_sum - k]
        prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

    return count


Solution = create_solution(subarray_sum)