# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 954
标题: Maximum Sum Circular Subarray
难度: medium
链接: https://leetcode.cn/problems/maximum-sum-circular-subarray/
题目类型: 队列、数组、分治、动态规划、单调队列
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
918. 环形子数组的最大和 - 给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。 环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i] 的前一个元素是 nums[(i - 1 + n) % n] 。 子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j] ，不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。 示例 1： 输入：nums = [1,-2,3,-2] 输出：3 解释：从子数组 [3] 得到最大和 3 示例 2： 输入：nums = [5,-3,5] 输出：10 解释：从子数组 [5,5] 得到最大和 5 + 5 = 10 示例 3： 输入：nums = [3,-2,2,-3] 输出：3 解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3 提示： * n == nums.length * 1 <= n <= 3 * 104 * -3 * 104 <= nums[i] <= 3 * 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Kadane's 算法分别找到最大子数组和最小子数组，然后通过总和减去最小子数组来处理环形情况。

算法步骤:
1. 计算数组的总和。
2. 使用 Kadane's 算法找到最大子数组和。
3. 使用 Kadane's 算法找到最小子数组和。
4. 如果最小子数组和等于总和，说明所有元素都是负数，直接返回最大子数组和。
5. 否则，返回最大子数组和和（总和 - 最小子数组和）中的较大值。

关键点:
- 处理环形子数组时，需要考虑总和减去最小子数组的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_subarray_sum_circular(nums: List[int]) -> int:
    """
    函数式接口 - 返回环形子数组的最大和
    """
    total_sum = sum(nums)
    max_sum = current_max = min_sum = current_min = nums[0]

    for num in nums[1:]:
        current_max = max(num, current_max + num)
        max_sum = max(max_sum, current_max)

        current_min = min(num, current_min + num)
        min_sum = min(min_sum, current_min)

    if min_sum == total_sum:
        return max_sum
    else:
        return max(max_sum, total_sum - min_sum)


Solution = create_solution(max_subarray_sum_circular)