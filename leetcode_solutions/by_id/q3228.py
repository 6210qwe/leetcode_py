# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3228
标题: Maximum Size of a Set After Removals
难度: medium
链接: https://leetcode.cn/problems/maximum-size-of-a-set-after-removals/
题目类型: 贪心、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3002. 移除后集合的最多元素数 - 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，它们的长度都是偶数 n 。 你必须从 nums1 中移除 n / 2 个元素，同时从 nums2 中也移除 n / 2 个元素。移除之后，你将 nums1 和 nums2 中剩下的元素插入到集合 s 中。 返回集合 s可能的 最多 包含多少元素。 示例 1： 输入：nums1 = [1,2,1,2], nums2 = [1,1,1,1] 输出：2 解释：从 nums1 和 nums2 中移除两个 1 。移除后，数组变为 nums1 = [2,2] 和 nums2 = [1,1] 。因此，s = {1,2} 。 可以证明，在移除之后，集合 s 最多可以包含 2 个元素。 示例 2： 输入：nums1 = [1,2,3,4,5,6], nums2 = [2,3,2,3,2,3] 输出：5 解释：从 nums1 中移除 2、3 和 6 ，同时从 nums2 中移除两个 3 和一个 2 。移除后，数组变为 nums1 = [1,4,5] 和 nums2 = [2,3,2] 。因此，s = {1,2,3,4,5} 。 可以证明，在移除之后，集合 s 最多可以包含 5 个元素。 示例 3： 输入：nums1 = [1,1,2,2,3,3], nums2 = [4,4,5,5,6,6] 输出：6 解释：从 nums1 中移除 1、2 和 3 ，同时从 nums2 中移除 4、5 和 6 。移除后，数组变为 nums1 = [1,2,3] 和 nums2 = [4,5,6] 。因此，s = {1,2,3,4,5,6} 。 可以证明，在移除之后，集合 s 最多可以包含 6 个元素。 提示： * n == nums1.length == nums2.length * 1 <= n <= 2 * 104 * n是偶数。 * 1 <= nums1[i], nums2[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，优先保留唯一元素，再考虑重叠元素。

算法步骤:
1. 计算 nums1 和 nums2 的交集和并集。
2. 从 nums1 和 nums2 中分别移除 n/2 个元素，优先移除不在交集中的元素。
3. 计算剩余元素的并集大小。

关键点:
- 优先移除不在交集中的元素，以最大化最终集合的大小。
- 使用集合操作来高效计算交集和并集。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def maximum_set_size(nums1: List[int], nums2: List[int]) -> int:
    """
    函数式接口 - 计算移除后集合的最大元素数
    """
    n = len(nums1)
    set1 = set(nums1)
    set2 = set(nums2)
    intersection = set1 & set2
    unique1 = set1 - intersection
    unique2 = set2 - intersection
    
    # 优先移除不在交集中的元素
    remove_from_unique1 = min(len(unique1), n // 2)
    remove_from_unique2 = min(len(unique2), n // 2)
    
    # 更新剩余的唯一元素
    remaining_unique1 = len(unique1) - remove_from_unique1
    remaining_unique2 = len(unique2) - remove_from_unique2
    
    # 计算需要从交集中移除的元素数量
    remove_from_intersection = max(0, (n // 2 - remove_from_unique1) + (n // 2 - remove_from_unique2))
    
    # 计算最终集合的大小
    return remaining_unique1 + remaining_unique2 + (len(intersection) - remove_from_intersection)


Solution = create_solution(maximum_set_size)