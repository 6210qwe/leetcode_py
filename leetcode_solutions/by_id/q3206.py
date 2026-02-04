# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3206
标题: Find Common Elements Between Two Arrays
难度: easy
链接: https://leetcode.cn/problems/find-common-elements-between-two-arrays/
题目类型: 数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2956. 找到两个数组中的公共元素 - 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，它们分别含有 n 和 m 个元素。请你计算以下两个数值： * answer1：使得 nums1[i] 在 nums2 中出现的下标 i 的数量。 * answer2：使得 nums2[i] 在 nums1 中出现的下标 i 的数量。 返回 [answer1, answer2]。 示例 1： 输入：nums1 = [2,3,2], nums2 = [1,2] 输出：[2,1] 解释： [https://assets.leetcode.com/uploads/2024/05/26/3488_find_common_elements_between_two_arrays-t1.gif] 示例 2： 输入：nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6] 输出：[3,4] 解释： nums1 中下标在 1，2，3 的元素在 nums2 中也存在。所以 answer1 为 3。 nums2 中下标在 0，1，3，4 的元素在 nums1 中也存在。所以 answer2 为 4。 示例 3： 输入：nums1 = [3,4,2,3], nums2 = [1,5] 输出：[0,0] 解释： nums1 和 nums2 中没有相同的数字，所以答案是 [0,0]。 提示： * n == nums1.length * m == nums2.length * 1 <= n, m <= 100 * 1 <= nums1[i], nums2[i] <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表来记录每个数组中元素的出现情况，然后通过比较两个哈希表来计算公共元素的数量。

算法步骤:
1. 创建两个哈希表，分别记录 nums1 和 nums2 中每个元素的出现次数。
2. 遍历 nums1，统计每个元素在 nums2 中出现的次数，累加到 answer1。
3. 遍历 nums2，统计每个元素在 nums1 中出现的次数，累加到 answer2。

关键点:
- 使用哈希表可以高效地统计元素出现次数，并且可以在 O(1) 时间内查找元素。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 和 m 分别是 nums1 和 nums2 的长度。我们需要遍历两个数组来构建哈希表，并再次遍历来计算公共元素的数量。
空间复杂度: O(n + m)，用于存储两个哈希表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_common_elements(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    函数式接口 - 找到两个数组中的公共元素
    """
    # 创建两个哈希表，分别记录 nums1 和 nums2 中每个元素的出现次数
    count_nums1 = {}
    count_nums2 = {}

    for num in nums1:
        count_nums1[num] = count_nums1.get(num, 0) + 1

    for num in nums2:
        count_nums2[num] = count_nums2.get(num, 0) + 1

    # 计算 answer1 和 answer2
    answer1 = sum(min(count_nums1[num], count_nums2.get(num, 0)) for num in count_nums1)
    answer2 = sum(min(count_nums2[num], count_nums1.get(num, 0)) for num in count_nums2)

    return [answer1, answer2]


Solution = create_solution(find_common_elements)