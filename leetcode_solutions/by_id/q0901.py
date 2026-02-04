# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 901
标题: Advantage Shuffle
难度: medium
链接: https://leetcode.cn/problems/advantage-shuffle/
题目类型: 贪心、数组、双指针、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
870. 优势洗牌 - 给定两个长度相等的数组 nums1 和 nums2，nums1 相对于 nums2 的优势可以用满足 nums1[i] > nums2[i] 的索引 i 的数目来描述。 返回 nums1 的 任意 排列，使其相对于 nums2 的优势最大化。 示例 1： 输入：nums1 = [2,7,11,15], nums2 = [1,10,4,11] 输出：[2,11,7,15] 示例 2： 输入：nums1 = [12,24,8,32], nums2 = [13,25,32,11] 输出：[24,32,8,12] 提示： * 1 <= nums1.length <= 105 * nums2.length == nums1.length * 0 <= nums1[i], nums2[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和双指针来实现。首先对 nums1 进行排序，然后对 nums2 进行降序排序，并记录其原始索引。遍历 nums2，对于每个元素，如果 nums1 中的最大值大于当前 nums2 元素，则将其分配给该位置；否则，将 nums1 中的最小值分配给该位置。

算法步骤:
1. 对 nums1 进行排序。
2. 对 nums2 进行降序排序，并记录其原始索引。
3. 使用双指针遍历 nums1 和 nums2，根据条件分配 nums1 中的元素。

关键点:
- 通过排序和双指针确保尽可能多的优势匹配。
- 记录 nums2 的原始索引以保持结果的正确顺序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 nums1 和 nums2 的长度。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，需要额外的空间来存储排序后的 nums2 及其原始索引。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def advantage_count(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    函数式接口 - 实现优势洗牌
    """
    # 对 nums1 进行排序
    nums1.sort()
    
    # 对 nums2 进行降序排序，并记录其原始索引
    sorted_nums2 = sorted(enumerate(nums2), key=lambda x: -x[1])
    
    # 初始化结果数组
    result = [0] * len(nums1)
    
    # 使用双指针遍历 nums1 和 nums2
    left, right = 0, len(nums1) - 1
    for index, value in sorted_nums2:
        if nums1[right] > value:
            result[index] = nums1[right]
            right -= 1
        else:
            result[index] = nums1[left]
            left += 1
    
    return result


Solution = create_solution(advantage_count)