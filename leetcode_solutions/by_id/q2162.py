# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2162
标题: Partition Array Into Two Arrays to Minimize Sum Difference
难度: hard
链接: https://leetcode.cn/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
题目类型: 位运算、数组、双指针、二分查找、动态规划、状态压缩、有序集合
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2035. 将数组分成两个数组并最小化数组和的差 - 给你一个长度为 2 * n 的整数数组。你需要将 nums 分成 两个 长度为 n 的数组，分别求出两个数组的和，并 最小化 两个数组和之 差的绝对值 。nums 中每个元素都需要放入两个数组之一。 请你返回 最小 的数组和之差。 示例 1： example-1 [https://assets.leetcode.com/uploads/2021/10/02/ex1.png] 输入：nums = [3,9,7,3] 输出：2 解释：最优分组方案是分成 [3,9] 和 [7,3] 。 数组和之差的绝对值为 abs((3 + 9) - (7 + 3)) = 2 。 示例 2： 输入：nums = [-36,36] 输出：72 解释：最优分组方案是分成 [-36] 和 [36] 。 数组和之差的绝对值为 abs((-36) - (36)) = 72 。 示例 3： example-3 [https://assets.leetcode.com/uploads/2021/10/02/ex3.png] 输入：nums = [2,-1,0,4,-2,-9] 输出：0 解释：最优分组方案是分成 [2,4,-9] 和 [-1,0,-2] 。 数组和之差的绝对值为 abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0 。 提示： * 1 <= n <= 15 * nums.length == 2 * n * -107 <= nums[i] <= 107
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用状态压缩和二分查找来找到最接近目标和的一半的子集和。

算法步骤:
1. 将数组分为两部分，分别计算所有可能的子集和。
2. 对于每部分的子集和进行排序。
3. 使用二分查找在一部分中找到最接近另一部分子集和的补集和。
4. 计算并更新最小的差值。

关键点:
- 使用状态压缩生成所有可能的子集和。
- 通过二分查找优化查找过程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n * log(2^n))，其中 n 是数组长度的一半。
空间复杂度: O(2^n)，存储所有可能的子集和。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    n = len(nums) // 2
    total_sum = sum(nums)
    target = total_sum / 2

    def get_subsets(arr: List[int]) -> List[int]:
        subsets = [0]
        for num in arr:
            new_subsets = []
            for subset in subsets:
                new_subsets.append(subset + num)
            subsets.extend(new_subsets)
        return sorted(set(subsets))

    left_subsets = get_subsets(nums[:n])
    right_subsets = get_subsets(nums[n:])

    min_diff = float('inf')
    for left_sum in left_subsets:
        complement = target - left_sum
        pos = bisect.bisect_left(right_subsets, complement)
        if pos < len(right_subsets):
            min_diff = min(min_diff, abs(total_sum - 2 * (left_sum + right_subsets[pos])))
        if pos > 0:
            min_diff = min(min_diff, abs(total_sum - 2 * (left_sum + right_subsets[pos - 1])))

    return int(min_diff)


Solution = create_solution(solution_function_name)