# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1699
标题: Number of Ways Where Square of Number Is Equal to Product of Two Numbers
难度: medium
链接: https://leetcode.cn/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/
题目类型: 数组、哈希表、数学、双指针
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1577. 数的平方等于两数乘积的方法数 - 给你两个整数数组 nums1 和 nums2 ，请你返回根据以下规则形成的三元组的数目（类型 1 和类型 2 ）： * 类型 1：三元组 (i, j, k) ，如果 nums1[i]2 == nums2[j] * nums2[k] 其中 0 <= i < nums1.length 且 0 <= j < k < nums2.length * 类型 2：三元组 (i, j, k) ，如果 nums2[i]2 == nums1[j] * nums1[k] 其中 0 <= i < nums2.length 且 0 <= j < k < nums1.length 示例 1： 输入：nums1 = [7,4], nums2 = [5,2,8,9] 输出：1 解释：类型 1：(1,1,2), nums1[1]^2 = nums2[1] * nums2[2] (4^2 = 2 * 8) 示例 2： 输入：nums1 = [1,1], nums2 = [1,1,1] 输出：9 解释：所有三元组都符合题目要求，因为 1^2 = 1 * 1 类型 1：(0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2), nums1[i]^2 = nums2[j] * nums2[k] 类型 2：(0,0,1), (1,0,1), (2,0,1), nums2[i]^2 = nums1[j] * nums1[k] 示例 3： 输入：nums1 = [7,7,8,3], nums2 = [1,2,9,7] 输出：2 解释：有两个符合题目要求的三元组 类型 1：(3,0,2), nums1[3]^2 = nums2[0] * nums2[2] 类型 2：(3,0,1), nums2[3]^2 = nums1[0] * nums1[1] 示例 4： 输入：nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18] 输出：0 解释：不存在符合题目要求的三元组 提示： * 1 <= nums1.length, nums2.length <= 1000 * 1 <= nums1[i], nums2[i] <= 10^5
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表来记录每个数的平方根出现的次数，然后通过遍历数组来查找符合条件的三元组。

算法步骤:
1. 计算 nums1 中每个数的平方，并使用哈希表记录这些平方值。
2. 遍历 nums2 的所有可能的 (j, k) 对，检查它们的乘积是否在哈希表中。如果存在，则累加相应的计数。
3. 对于类型 2 的三元组，重复上述步骤，但这次计算 nums2 中每个数的平方，并检查 nums1 中的 (j, k) 对。

关键点:
- 使用哈希表来存储平方值及其出现次数，以实现快速查找。
- 通过双重循环遍历数组，找到符合条件的 (j, k) 对。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 + m^2)，其中 n 是 nums1 的长度，m 是 nums2 的长度。
空间复杂度: O(n + m)，用于存储哈希表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_triplets(nums1: List[int], nums2: List[int]) -> int:
    def count_type1(nums1: List[int], nums2: List[int]) -> int:
        square_count = {}
        for num in nums1:
            square = num * num
            if square not in square_count:
                square_count[square] = 0
            square_count[square] += 1

        count = 0
        for j in range(len(nums2)):
            for k in range(j + 1, len(nums2)):
                product = nums2[j] * nums2[k]
                if product in square_count:
                    count += square_count[product]

        return count

    return count_type1(nums1, nums2) + count_type1(nums2, nums1)


Solution = create_solution(count_triplets)