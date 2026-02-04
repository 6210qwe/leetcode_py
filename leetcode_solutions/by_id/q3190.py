# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3190
标题: Minimum Operations to Maximize Last Elements in Arrays
难度: medium
链接: https://leetcode.cn/problems/minimum-operations-to-maximize-last-elements-in-arrays/
题目类型: 数组、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2934. 最大化数组末位元素的最少操作次数 - 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，这两个数组的长度都是 n 。 你可以执行一系列 操作（可能不执行）。 在每次操作中，你可以选择一个在范围 [0, n - 1] 内的下标 i ，并交换 nums1[i] 和 nums2[i] 的值。 你的任务是找到满足以下条件所需的 最小 操作次数： * nums1[n - 1] 等于 nums1 中所有元素的 最大值 ，即 nums1[n - 1] = max(nums1[0], nums1[1], ..., nums1[n - 1]) 。 * nums2[n - 1] 等于 nums2 中所有元素的 最大值 ，即 nums2[n - 1] = max(nums2[0], nums2[1], ..., nums2[n - 1]) 。 以整数形式，表示并返回满足上述 全部 条件所需的 最小 操作次数，如果无法同时满足两个条件，则返回 -1 。 示例 1： 输入：nums1 = [1,2,7]，nums2 = [4,5,3] 输出：1 解释：在这个示例中，可以选择下标 i = 2 执行一次操作。 交换 nums1[2] 和 nums2[2] 的值，nums1 变为 [1,2,3] ，nums2 变为 [4,5,7] 。 同时满足两个条件。 可以证明，需要执行的最小操作次数为 1 。 因此，答案是 1 。 示例 2： 输入：nums1 = [2,3,4,5,9]，nums2 = [8,8,4,4,4] 输出：2 解释：在这个示例中，可以执行以下操作： 首先，选择下标 i = 4 执行操作。 交换 nums1[4] 和 nums2[4] 的值，nums1 变为 [2,3,4,5,4] ，nums2 变为 [8,8,4,4,9] 。 然后，选择下标 i = 3 执行操作。 交换 nums1[3] 和 nums2[3] 的值，nums1 变为 [2,3,4,4,4] ，nums2 变为 [8,8,4,5,9] 。 同时满足两个条件。 可以证明，需要执行的最小操作次数为 2 。 因此，答案是 2 。 示例 3： 输入：nums1 = [1,5,4]，nums2 = [2,5,3] 输出：-1 解释：在这个示例中，无法同时满足两个条件。 因此，答案是 -1 。 提示： * 1 <= n == nums1.length == nums2.length <= 1000 * 1 <= nums1[i] <= 109 * 1 <= nums2[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过枚举和贪心算法来找到最小的操作次数。

算法步骤:
1. 计算 nums1 和 nums2 的最后一个元素。
2. 检查是否可以通过交换使 nums1 和 nums2 的最后一个元素分别为各自数组的最大值。
3. 如果可以，计算所需的操作次数；否则返回 -1。

关键点:
- 通过枚举和贪心算法来找到最小的操作次数。
- 保证最后一次操作后，两个数组的最后一个元素分别是各自数组的最大值。
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


def minimum_operations_to_maximize_last_elements(nums1: List[int], nums2: List[int]) -> int:
    """
    函数式接口 - 找到最大化数组末位元素的最少操作次数
    """
    n = len(nums1)
    last1, last2 = nums1[-1], nums2[-1]
    max1, max2 = max(nums1), max(nums2)

    if last1 < max2 or last2 < max1:
        return -1

    # Count the number of operations needed to make last1 and last2 the maximum values in their respective arrays
    operations = 0
    for i in range(n - 1):
        if nums1[i] > last1 and nums2[i] > last2:
            return -1
        if nums1[i] > last1:
            operations += 1
        if nums2[i] > last2:
            operations += 1

    return operations


Solution = create_solution(minimum_operations_to_maximize_last_elements)