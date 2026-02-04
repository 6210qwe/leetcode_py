# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2592
标题: Minimum Total Cost to Make Arrays Unequal
难度: hard
链接: https://leetcode.cn/problems/minimum-total-cost-to-make-arrays-unequal/
题目类型: 贪心、数组、哈希表、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2499. 让数组不相等的最小总代价 - 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，两者长度都为 n 。 每次操作中，你可以选择交换 nums1 中任意两个下标处的值。操作的 开销 为两个下标的 和 。 你的目标是对于所有的 0 <= i <= n - 1 ，都满足 nums1[i] != nums2[i] ，你可以进行 任意次 操作，请你返回达到这个目标的 最小 总代价。 请你返回让 nums1 和 nums2 满足上述条件的 最小总代价 ，如果无法达成目标，返回 -1 。 示例 1： 输入：nums1 = [1,2,3,4,5], nums2 = [1,2,3,4,5] 输出：10 解释： 实现目标的其中一种方法为： - 交换下标为 0 和 3 的两个值，代价为 0 + 3 = 3 。现在 nums1 = [4,2,3,1,5] 。 - 交换下标为 1 和 2 的两个值，代价为 1 + 2 = 3 。现在 nums1 = [4,3,2,1,5] 。 - 交换下标为 0 和 4 的两个值，代价为 0 + 4 = 4 。现在 nums1 = [5,3,2,1,4] 。 最后，对于每个下标 i ，都有 nums1[i] != nums2[i] 。总代价为 10 。 还有别的交换值的方法，但是无法得到代价和小于 10 的方案。 示例 2： 输入：nums1 = [2,2,2,1,3], nums2 = [1,2,2,3,3] 输出：10 解释： 实现目标的一种方法为： - 交换下标为 2 和 3 的两个值，代价为 2 + 3 = 5 。现在 nums1 = [2,2,1,2,3] 。 - 交换下标为 1 和 4 的两个值，代价为 1 + 4 = 5 。现在 nums1 = [2,3,1,2,2] 。 总代价为 10 ，是所有方案中的最小代价。 示例 3： 输入：nums1 = [1,2,2], nums2 = [1,2,2] 输出：-1 解释： 不管怎么操作，都无法满足题目要求。 所以返回 -1 。 提示： * n == nums1.length == nums2.length * 1 <= n <= 105 * 1 <= nums1[i], nums2[i] <= n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过贪心算法找到最小代价的交换方式，使得 nums1 和 nums2 在每个位置上都不相等。

算法步骤:
1. 统计 nums1 和 nums2 在每个位置上的相同元素，并记录这些位置。
2. 计算这些相同元素的频率，找到频率最高的元素。
3. 尽可能多地交换这些频率最高的元素，直到满足条件或无法再交换。
4. 如果无法满足条件，返回 -1；否则返回总代价。

关键点:
- 使用哈希表统计频率。
- 优先交换频率最高的元素。
- 交换时尽量选择代价最小的位置。
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


def min_total_cost(nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    freq = {}
    same_positions = []
    total_cost = 0
    
    # 统计相同位置的元素及其频率
    for i in range(n):
        if nums1[i] == nums2[i]:
            same_positions.append(i)
            freq[nums1[i]] = freq.get(nums1[i], 0) + 1
    
    # 找到频率最高的元素
    max_freq = max(freq.values()) if freq else 0
    most_common_element = next((k for k, v in freq.items() if v == max_freq), None)
    
    # 交换频率最高的元素
    for i in same_positions:
        if freq[nums1[i]] < max_freq or (freq[nums1[i]] == max_freq and nums1[i] == most_common_element):
            for j in range(n):
                if nums1[j] != nums2[j] and nums1[j] != nums1[i]:
                    total_cost += i + j
                    nums1[i], nums1[j] = nums1[j], nums1[i]
                    break
            else:
                return -1
    
    return total_cost


Solution = create_solution(min_total_cost)