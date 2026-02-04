# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1514
标题: Minimum Value to Get Positive Step by Step Sum
难度: easy
链接: https://leetcode.cn/problems/minimum-value-to-get-positive-step-by-step-sum/
题目类型: 数组、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1413. 逐步求和得到正数的最小值 - 给你一个整数数组 nums 。你可以选定任意的 正数 startValue 作为初始值。 你需要从左到右遍历 nums 数组，并将 startValue 依次累加上 nums 数组中的值。 请你在确保累加和始终大于等于 1 的前提下，选出一个最小的 正数 作为 startValue 。 示例 1： 输入：nums = [-3,2,-3,4,2] 输出：5 解释：如果你选择 startValue = 4，在第三次累加时，和小于 1 。 累加求和 startValue = 4 | startValue = 5 | nums (4 -3 ) = 1 | (5 -3 ) = 2 | -3 (1 +2 ) = 3 | (2 +2 ) = 4 | 2 (3 -3 ) = 0 | (4 -3 ) = 1 | -3 (0 +4 ) = 4 | (1 +4 ) = 5 | 4 (4 +2 ) = 6 | (5 +2 ) = 7 | 2 示例 2： 输入：nums = [1,2] 输出：1 解释：最小的 startValue 需要是正数。 示例 3： 输入：nums = [1,-2,-3] 输出：5 提示： * 1 <= nums.length <= 100 * -100 <= nums[i] <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 计算前缀和的最小值，然后根据这个最小值来确定 startValue。

算法步骤:
1. 初始化一个变量 `prefix_sum` 为 0，用于记录当前的前缀和。
2. 初始化一个变量 `min_prefix_sum` 为 0，用于记录前缀和的最小值。
3. 遍历数组 `nums`，更新 `prefix_sum` 和 `min_prefix_sum`。
4. 根据 `min_prefix_sum` 计算 `startValue`，如果 `min_prefix_sum` 小于 0，则 `startValue` 为 `1 - min_prefix_sum`，否则 `startValue` 为 1。

关键点:
- 通过计算前缀和的最小值来确定所需的最小 `startValue`。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组 `nums` 的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
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
    函数式接口 - 计算逐步求和得到正数的最小值
    """
    prefix_sum = 0
    min_prefix_sum = 0
    
    for num in nums:
        prefix_sum += num
        min_prefix_sum = min(min_prefix_sum, prefix_sum)
    
    # 如果 min_prefix_sum 小于 0，则 startValue 为 1 - min_prefix_sum，否则 startValue 为 1
    return 1 - min_prefix_sum if min_prefix_sum < 0 else 1


Solution = create_solution(solution_function_name)