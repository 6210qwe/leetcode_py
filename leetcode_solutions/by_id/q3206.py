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
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
