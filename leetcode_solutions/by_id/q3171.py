# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3171
标题: Minimum Equal Sum of Two Arrays After Replacing Zeros
难度: medium
链接: https://leetcode.cn/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/
题目类型: 贪心、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2918. 数组的最小相等和 - 给你两个由正整数和 0 组成的数组 nums1 和 nums2 。 你必须将两个数组中的 所有 0 替换为 严格 正整数，并且满足两个数组中所有元素的和 相等 。 返回 最小 相等和 ，如果无法使两数组相等，则返回 -1 。 示例 1： 输入：nums1 = [3,2,0,1,0], nums2 = [6,5,0] 输出：12 解释：可以按下述方式替换数组中的 0 ： - 用 2 和 4 替换 nums1 中的两个 0 。得到 nums1 = [3,2,2,1,4] 。 - 用 1 替换 nums2 中的一个 0 。得到 nums2 = [6,5,1] 。 两个数组的元素和相等，都等于 12 。可以证明这是可以获得的最小相等和。 示例 2： 输入：nums1 = [2,0,2,0], nums2 = [1,4] 输出：-1 解释：无法使两个数组的和相等。 提示： * 1 <= nums1.length, nums2.length <= 105 * 0 <= nums1[i], nums2[i] <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 计算两个数组的初始和，并考虑将 0 替换为 1 后的和。如果一个数组的和加上其 0 的数量小于另一个数组的和，则无法使两个数组的和相等。否则，返回两个数组中较大的和。

算法步骤:
1. 计算 nums1 和 nums2 的初始和 sum1 和 sum2。
2. 计算 nums1 和 nums2 中 0 的数量 zero_count1 和 zero_count2。
3. 如果 sum1 + zero_count1 < sum2 或 sum2 + zero_count2 < sum1，则返回 -1。
4. 否则，返回 max(sum1 + zero_count1, sum2 + zero_count2)。

关键点:
- 将 0 替换为 1 是最优选择，因为 1 是最小的正整数。
- 只需比较两个数组在替换 0 为 1 后的和，取较大值即可。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 和 m 分别是 nums1 和 nums2 的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimum_equal_sum(nums1: List[int], nums2: List[int]) -> int:
    """
    函数式接口 - 计算两个数组的最小相等和
    """
    sum1 = sum(nums1)
    sum2 = sum(nums2)
    
    zero_count1 = nums1.count(0)
    zero_count2 = nums2.count(0)
    
    if sum1 + zero_count1 < sum2 or sum2 + zero_count2 < sum1:
        return -1
    
    return max(sum1 + zero_count1, sum2 + zero_count2)


Solution = create_solution(minimum_equal_sum)