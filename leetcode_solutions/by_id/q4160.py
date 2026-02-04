# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4160
标题: Maximum Sum of Three Numbers Divisible by Three
难度: medium
链接: https://leetcode.cn/problems/maximum-sum-of-three-numbers-divisible-by-three/
题目类型: 贪心、数组、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3780. 能被 3 整除的三元组最大和 - 给你一个整数数组 nums。你的任务是从 nums 中选择 恰好三个 整数，使得它们的和能被 3 整除。 返回这类三元组可能产生的 最大 和。如果不存在这样的三元组，返回 0。 示例 1: 输入: nums = [4,2,3,1] 输出: 9 解释: 总和能被 3 整除的有效三元组为： * (4, 2, 3)，和为 4 + 2 + 3 = 9。 * (2, 3, 1)，和为 2 + 3 + 1 = 6。 因此，答案是 9。 示例 2: 输入: nums = [2,1,5] 输出: 0 解释: 没有三元组的和能被 3 整除，所以答案是 0。 提示: * 3 <= nums.length <= 105 * 1 <= nums[i] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，通过分类讨论不同余数的情况来找到最大和。

算法步骤:
1. 将数组按元素对 3 取余的结果分为三类：余数为 0、1 和 2。
2. 对每一类进行降序排序。
3. 讨论以下几种情况：
   - 三个余数为 0 的数。
   - 两个余数为 1 和一个余数为 2 的数。
   - 两个余数为 2 和一个余数为 1 的数。
4. 计算每种情况的最大和，并返回其中的最大值。

关键点:
- 通过对数组进行分类和排序，可以有效地找到满足条件的最大和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是数组的长度。主要由排序操作决定。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_sum_divisible_by_three(nums: List[int]) -> int:
    """
    函数式接口 - 找到能被 3 整除的三元组最大和
    """
    # 分类存储余数为 0, 1, 2 的数
    remainder_0 = []
    remainder_1 = []
    remainder_2 = []

    for num in nums:
        if num % 3 == 0:
            remainder_0.append(num)
        elif num % 3 == 1:
            remainder_1.append(num)
        else:
            remainder_2.append(num)

    # 对每一类进行降序排序
    remainder_0.sort(reverse=True)
    remainder_1.sort(reverse=True)
    remainder_2.sort(reverse=True)

    # 计算每种情况的最大和
    max_sum = 0

    # 三个余数为 0 的数
    if len(remainder_0) >= 3:
        max_sum = max(max_sum, sum(remainder_0[:3]))

    # 两个余数为 1 和一个余数为 2 的数
    if len(remainder_1) >= 2 and len(remainder_2) >= 1:
        max_sum = max(max_sum, sum(remainder_1[:2]) + remainder_2[0])

    # 两个余数为 2 和一个余数为 1 的数
    if len(remainder_2) >= 2 and len(remainder_1) >= 1:
        max_sum = max(max_sum, sum(remainder_2[:2]) + remainder_1[0])

    return max_sum


Solution = create_solution(max_sum_divisible_by_three)