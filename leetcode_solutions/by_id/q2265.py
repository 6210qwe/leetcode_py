# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2265
标题: Partition Array According to Given Pivot
难度: medium
链接: https://leetcode.cn/problems/partition-array-according-to-given-pivot/
题目类型: 数组、双指针、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2161. 根据给定数字划分数组 - 给你一个下标从 0 开始的整数数组 nums 和一个整数 pivot 。请你将 nums 重新排列，使得以下条件均成立： * 所有小于 pivot 的元素都出现在所有大于 pivot 的元素 之前 。 * 所有等于 pivot 的元素都出现在小于和大于 pivot 的元素 中间 。 * 小于 pivot 的元素之间和大于 pivot 的元素之间的 相对顺序 不发生改变。 * 更正式的，考虑每一对 pi，pj ，pi 是初始时位置 i 元素的新位置，pj 是初始时位置 j 元素的新位置。如果 i < j 且两个元素 都 小于（或大于）pivot，那么 pi < pj 。 请你返回重新排列 nums 数组后的结果数组。 示例 1： 输入：nums = [9,12,5,10,14,3,10], pivot = 10 输出：[9,5,3,10,10,12,14] 解释： 元素 9 ，5 和 3 小于 pivot ，所以它们在数组的最左边。 元素 12 和 14 大于 pivot ，所以它们在数组的最右边。 小于 pivot 的元素的相对位置和大于 pivot 的元素的相对位置分别为 [9, 5, 3] 和 [12, 14] ，它们在结果数组中的相对顺序需要保留。 示例 2： 输入：nums = [-3,4,3,2], pivot = 2 输出：[-3,2,4,3] 解释： 元素 -3 小于 pivot ，所以在数组的最左边。 元素 4 和 3 大于 pivot ，所以它们在数组的最右边。 小于 pivot 的元素的相对位置和大于 pivot 的元素的相对位置分别为 [-3] 和 [4, 3] ，它们在结果数组中的相对顺序需要保留。 提示： * 1 <= nums.length <= 105 * -106 <= nums[i] <= 106 * pivot 等于 nums 中的一个元素。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用三个列表分别存储小于、等于和大于 pivot 的元素，最后将这三个列表合并。

算法步骤:
1. 初始化三个空列表：less_than_pivot, equal_to_pivot, greater_than_pivot。
2. 遍历输入数组 nums，根据元素与 pivot 的比较结果，将其分别添加到相应的列表中。
3. 最后将这三个列表按顺序合并成一个结果数组并返回。

关键点:
- 保持小于和大于 pivot 的元素的相对顺序不变。
- 使用三个列表来分别存储不同范围的元素，最后合并。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 nums 的长度。我们只需要遍历一次数组。
空间复杂度: O(n)，我们需要额外的空间来存储三个列表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def partition_array(nums: List[int], pivot: int) -> List[int]:
    """
    函数式接口 - 根据给定的 pivot 对数组进行划分
    """
    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []

    for num in nums:
        if num < pivot:
            less_than_pivot.append(num)
        elif num == pivot:
            equal_to_pivot.append(num)
        else:
            greater_than_pivot.append(num)

    return less_than_pivot + equal_to_pivot + greater_than_pivot


Solution = create_solution(partition_array)