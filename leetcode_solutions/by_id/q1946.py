# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1946
标题: Minimum Absolute Sum Difference
难度: medium
链接: https://leetcode.cn/problems/minimum-absolute-sum-difference/
题目类型: 数组、二分查找、有序集合、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1818. 绝对差值和 - 给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。 数组 nums1 和 nums2 的 绝对差值和 定义为所有 |nums1[i] - nums2[i]|（0 <= i < n）的 总和（下标从 0 开始）。 你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。 在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 109 + 7 取余 后返回。 |x| 定义为： * 如果 x >= 0 ，值为 x ，或者 * 如果 x <= 0 ，值为 -x 示例 1： 输入：nums1 = [1,7,5], nums2 = [2,3,5] 输出：3 解释：有两种可能的最优方案： - 将第二个元素替换为第一个元素：[1,7,5] => [1,1,5] ，或者 - 将第二个元素替换为第三个元素：[1,7,5] => [1,5,5] 两种方案的绝对差值和都是 |1-2| + (|1-3| 或者 |5-3|) + |5-5| = 3 示例 2： 输入：nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10] 输出：0 解释：nums1 和 nums2 相等，所以不用替换元素。绝对差值和为 0 示例 3： 输入：nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4] 输出：20 解释：将第一个元素替换为第二个元素：[1,10,4,4,2,7] => [10,10,4,4,2,7] 绝对差值和为 |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20 提示： * n == nums1.length * n == nums2.length * 1 <= n <= 105 * 1 <= nums1[i], nums2[i] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找找到最接近 nums2[i] 的元素，从而最小化绝对差值和。

算法步骤:
1. 计算初始的绝对差值和。
2. 对 nums1 进行排序，并使用二分查找找到最接近 nums2[i] 的元素。
3. 计算替换后的绝对差值和，更新最小值。
4. 返回最小绝对差值和并对 10^9 + 7 取余。

关键点:
- 使用二分查找提高查找效率。
- 通过排序和二分查找确保时间复杂度最优。
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

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_absolute_sum_diff(nums1: List[int], nums2: List[int]) -> int:
    """
    函数式接口 - 计算最小绝对差值和
    """
    n = len(nums1)
    mod = 10**9 + 7
    sorted_nums1 = sorted(nums1)
    total_diff = sum(abs(nums1[i] - nums2[i]) for i in range(n))
    max_reduction = 0

    for i in range(n):
        diff = abs(nums1[i] - nums2[i])
        # 使用二分查找找到最接近 nums2[i] 的元素
        idx = binary_search(sorted_nums1, nums2[i])
        if idx < n:
            max_reduction = max(max_reduction, diff - abs(sorted_nums1[idx] - nums2[i]))
        if idx > 0:
            max_reduction = max(max_reduction, diff - abs(sorted_nums1[idx - 1] - nums2[i]))

    return (total_diff - max_reduction) % mod


def binary_search(arr: List[int], target: int) -> int:
    """
    二分查找 - 找到大于等于 target 的最小索引
    """
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


Solution = create_solution(min_absolute_sum_diff)