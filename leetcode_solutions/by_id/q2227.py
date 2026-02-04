# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2227
标题: Sum of Subarray Ranges
难度: medium
链接: https://leetcode.cn/problems/sum-of-subarray-ranges/
题目类型: 栈、数组、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2104. 子数组范围和 - 给你一个整数数组 nums 。nums 中，子数组的 范围 是子数组中最大元素和最小元素的差值。 返回 nums 中 所有 子数组范围的 和 。 子数组是数组中一个连续 非空 的元素序列。 示例 1： 输入：nums = [1,2,3] 输出：4 解释：nums 的 6 个子数组如下所示： [1]，范围 = 最大 - 最小 = 1 - 1 = 0 [2]，范围 = 2 - 2 = 0 [3]，范围 = 3 - 3 = 0 [1,2]，范围 = 2 - 1 = 1 [2,3]，范围 = 3 - 2 = 1 [1,2,3]，范围 = 3 - 1 = 2 所有范围的和是 0 + 0 + 0 + 1 + 1 + 2 = 4 示例 2： 输入：nums = [1,3,3] 输出：4 解释：nums 的 6 个子数组如下所示： [1]，范围 = 最大 - 最小 = 1 - 1 = 0 [3]，范围 = 3 - 3 = 0 [3]，范围 = 3 - 3 = 0 [1,3]，范围 = 3 - 1 = 2 [3,3]，范围 = 3 - 3 = 0 [1,3,3]，范围 = 3 - 1 = 2 所有范围的和是 0 + 0 + 0 + 2 + 0 + 2 = 4 示例 3： 输入：nums = [4,-2,-3,4,1] 输出：59 解释：nums 中所有子数组范围的和是 59 提示： * 1 <= nums.length <= 1000 * -109 <= nums[i] <= 109 进阶：你可以设计一种时间复杂度为 O(n) 的解决方案吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用单调栈来计算每个元素作为子数组最大值和最小值的贡献。

算法步骤:
1. 计算每个元素作为子数组最大值的贡献。
2. 计算每个元素作为子数组最小值的贡献。
3. 将两个贡献相减得到最终结果。

关键点:
- 使用单调递增栈和单调递减栈来分别计算最大值和最小值的贡献。
- 每个元素的贡献可以通过其左右边界来确定。
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


def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 计算所有子数组范围的和
    """
    def sum_subarray_extremes(nums: List[int], is_max: bool) -> int:
        stack = []
        result = 0
        for i, num in enumerate(nums + [float('inf') if is_max else float('-inf')]):
            while stack and (num > nums[stack[-1]] if is_max else num < nums[stack[-1]]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                result += nums[mid] * (mid - left) * (right - mid)
            stack.append(i)
        return result

    max_sum = sum_subarray_extremes(nums, True)
    min_sum = sum_subarray_extremes(nums, False)
    return max_sum - min_sum


Solution = create_solution(solution_function_name)