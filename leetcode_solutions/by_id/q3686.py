# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3686
标题: Count Beautiful Splits in an Array
难度: medium
链接: https://leetcode.cn/problems/count-beautiful-splits-in-an-array/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3388. 统计数组中的美丽分割 - 给你一个整数数组 nums 。 如果数组 nums 的一个分割满足以下条件，我们称它是一个 美丽 分割： 1. 数组 nums 分为三段 非空子数组：nums1 ，nums2 和 nums3 ，三个数组 nums1 ，nums2 和 nums3 按顺序连接可以得到 nums 。 2. 子数组 nums1 是子数组 nums2 的 前缀 或者 nums2 是 nums3 的 前缀。 请你返回满足以上条件的分割 数目 。 子数组 指的是一个数组里一段连续 非空 的元素。 前缀 指的是一个数组从头开始到中间某个元素结束的子数组。 示例 1： 输入：nums = [1,1,2,1] 输出：2 解释： 美丽分割如下： 1. nums1 = [1] ，nums2 = [1,2] ，nums3 = [1] 。 2. nums1 = [1] ，nums2 = [1] ，nums3 = [2,1] 。 示例 2： 输入：nums = [1,2,3,4] 输出：0 解释： 没有美丽分割。 提示： * 1 <= nums.length <= 5000 * 0 <= nums[i] <= 50
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针和哈希表来记录前缀和后缀匹配情况。

算法步骤:
1. 初始化两个指针 i 和 j，分别指向 nums1 和 nums2 的起始位置。
2. 使用一个哈希表 prefix_count 来记录 nums1 的前缀出现次数。
3. 遍历数组，更新哈希表并检查当前前缀是否与 nums2 的前缀或 nums3 的前缀匹配。
4. 计算美丽分割的数量。

关键点:
- 使用哈希表记录前缀出现次数，减少重复计算。
- 双指针遍历数组，确保每个可能的分割都被检查。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是数组长度。最坏情况下需要检查所有可能的分割。
空间复杂度: O(n)，哈希表存储前缀出现次数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_beautiful_splits(nums: List[int]) -> int:
    """
    函数式接口 - 统计数组中的美丽分割
    """
    n = len(nums)
    beautiful_splits = 0

    for i in range(1, n - 1):
        prefix_count = {}
        for j in range(i):
            prefix = tuple(nums[:j + 1])
            if prefix in prefix_count:
                prefix_count[prefix] += 1
            else:
                prefix_count[prefix] = 1

        for k in range(i, n - 1):
            suffix = tuple(nums[k + 1:])
            if suffix in prefix_count:
                beautiful_splits += prefix_count[suffix]

            prefix = tuple(nums[i:k + 1])
            if prefix in prefix_count:
                beautiful_splits += prefix_count[prefix]

    return beautiful_splits


Solution = create_solution(count_beautiful_splits)