# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1881
标题: Closest Subsequence Sum
难度: hard
链接: https://leetcode.cn/problems/closest-subsequence-sum/
题目类型: 位运算、数组、双指针、动态规划、状态压缩、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1755. 最接近目标值的子序列和 - 给你一个整数数组 nums 和一个目标值 goal 。 你需要从 nums 中选出一个子序列，使子序列元素总和最接近 goal 。也就是说，如果子序列元素和为 sum ，你需要 最小化绝对差 abs(sum - goal) 。 返回 abs(sum - goal) 可能的 最小值 。 注意，数组的子序列是通过移除原始数组中的某些元素（可能全部或无）而形成的数组。 示例 1： 输入：nums = [5,-7,3,5], goal = 6 输出：0 解释：选择整个数组作为选出的子序列，元素和为 6 。 子序列和与目标值相等，所以绝对差为 0 。 示例 2： 输入：nums = [7,-9,15,-2], goal = -5 输出：1 解释：选出子序列 [7,-9,-2] ，元素和为 -4 。 绝对差为 abs(-4 - (-5)) = abs(1) = 1 ，是可能的最小值。 示例 3： 输入：nums = [1,2,3], goal = -7 输出：7 提示： * 1 <= nums.length <= 40 * -107 <= nums[i] <= 107 * -109 <= goal <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用分治法将问题分成两部分，分别计算所有可能的子序列和，然后使用双指针找到最接近目标值的子序列和。

算法步骤:
1. 将数组分成两部分，分别计算每部分的所有可能的子序列和。
2. 对两个部分的子序列和进行排序。
3. 使用双指针在两个排序后的子序列和中找到最接近目标值的组合。

关键点:
- 分治法可以有效地减少问题规模，使得每个子问题可以在合理的时间内解决。
- 双指针方法可以高效地找到最接近目标值的组合。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^(n/2) * log(2^(n/2))) = O(2^(n/2) * (n/2)) = O(n * 2^(n/2))
空间复杂度: O(2^(n/2))，用于存储两个部分的所有可能的子序列和。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def closest_subsequence_sum(nums: List[int], goal: int) -> int:
    """
    函数式接口 - 计算最接近目标值的子序列和
    """
    n = len(nums)
    half = n // 2
    
    # 生成所有可能的子序列和
    def generate_sums(arr):
        sums = {0}
        for num in arr:
            new_sums = set()
            for s in sums:
                new_sums.add(s + num)
            sums.update(new_sums)
        return sorted(sums)
    
    left_sums = generate_sums(nums[:half])
    right_sums = generate_sums(nums[half:])
    
    # 使用双指针找到最接近目标值的组合
    i, j = 0, len(right_sums) - 1
    min_diff = float('inf')
    
    while i < len(left_sums) and j >= 0:
        current_sum = left_sums[i] + right_sums[j]
        diff = abs(current_sum - goal)
        if diff < min_diff:
            min_diff = diff
        if current_sum < goal:
            i += 1
        else:
            j -= 1
    
    return min_diff


Solution = create_solution(closest_subsequence_sum)