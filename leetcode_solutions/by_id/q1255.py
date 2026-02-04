# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1255
标题: Reverse Subarray To Maximize Array Value
难度: hard
链接: https://leetcode.cn/problems/reverse-subarray-to-maximize-array-value/
题目类型: 贪心、数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1330. 翻转子数组得到最大的数组值 - 给你一个整数数组 nums 。「数组值」定义为所有满足 0 <= i < nums.length-1 的 |nums[i]-nums[i+1]| 的和。 你可以选择给定数组的任意子数组，并将该子数组翻转。但你只能执行这个操作 一次 。 请你找到可行的最大 数组值 。 示例 1： 输入：nums = [2,3,1,5,4] 输出：10 解释：通过翻转子数组 [3,1,5] ，数组变成 [2,5,1,3,4] ，数组值为 10 。 示例 2： 输入：nums = [2,4,9,24,2,1,10] 输出：68 提示： * 2 <= nums.length <= 3*104 * -105 <= nums[i] <= 105 * 答案保证在 32 位整数范围内。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过贪心算法找到能够最大化数组值的子数组翻转。

算法步骤:
1. 计算原始数组的初始值。
2. 遍历所有可能的子数组，计算翻转后的数组值增量。
3. 选择使数组值增量最大的子数组进行翻转。
4. 返回最大数组值。

关键点:
- 利用差分数组来简化计算。
- 通过遍历所有可能的子数组，找到最佳翻转位置。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)
空间复杂度: O(1)
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
    函数式接口 - 通过翻转子数组来最大化数组值
    """
    n = len(nums)
    original_value = sum(abs(nums[i] - nums[i + 1]) for i in range(n - 1))
    
    max_increase = 0
    for i in range(n):
        for j in range(i + 1, n):
            # 计算翻转子数组 [i, j] 后的增量
            if i > 0:
                increase = abs(nums[i - 1] - nums[j]) - abs(nums[i - 1] - nums[i])
            else:
                increase = 0
            if j < n - 1:
                increase += abs(nums[i] - nums[j + 1]) - abs(nums[j] - nums[j + 1])
            
            max_increase = max(max_increase, increase)
    
    return original_value + max_increase


Solution = create_solution(solution_function_name)