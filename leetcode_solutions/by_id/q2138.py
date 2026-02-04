# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2138
标题: Sum of Beauty in the Array
难度: medium
链接: https://leetcode.cn/problems/sum-of-beauty-in-the-array/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2012. 数组美丽值求和 - 给你一个下标从 0 开始的整数数组 nums 。对于每个下标 i（1 <= i <= nums.length - 2），nums[i] 的 美丽值 等于： * 2，对于所有 0 <= j < i 且 i < k <= nums.length - 1 ，满足 nums[j] < nums[i] < nums[k] * 1，如果满足 nums[i - 1] < nums[i] < nums[i + 1] ，且不满足前面的条件 * 0，如果上述条件全部不满足 返回符合 1 <= i <= nums.length - 2 的所有 nums[i] 的 美丽值的总和 。 示例 1： 输入：nums = [1,2,3] 输出：2 解释：对于每个符合范围 1 <= i <= 1 的下标 i : - nums[1] 的美丽值等于 2 示例 2： 输入：nums = [2,4,6,4] 输出：1 解释：对于每个符合范围 1 <= i <= 2 的下标 i : - nums[1] 的美丽值等于 1 - nums[2] 的美丽值等于 0 示例 3： 输入：nums = [3,2,1] 输出：0 解释：对于每个符合范围 1 <= i <= 1 的下标 i : - nums[1] 的美丽值等于 0 提示： * 3 <= nums.length <= 105 * 1 <= nums[i] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个辅助数组来记录每个位置左侧的最大值和右侧的最小值，从而可以在 O(1) 时间内判断 nums[i] 是否满足条件。

算法步骤:
1. 初始化两个辅助数组 left_max 和 right_min。
2. 填充 left_max 数组，使其在每个位置 i 处存储从 0 到 i-1 的最大值。
3. 填充 right_min 数组，使其在每个位置 i 处存储从 i+1 到 n-1 的最小值。
4. 遍历 nums 数组，根据 left_max 和 right_min 数组计算每个位置 i 的美丽值，并累加到结果中。

关键点:
- 使用两个辅助数组来快速判断 nums[i] 是否满足条件。
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


def sum_of_beauty(nums: List[int]) -> int:
    """
    函数式接口 - 计算数组的美丽值总和
    """
    n = len(nums)
    if n < 3:
        return 0

    # 辅助数组，left_max[i] 存储从 0 到 i-1 的最大值
    left_max = [0] * n
    left_max[0] = nums[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], nums[i])

    # 辅助数组，right_min[i] 存储从 i+1 到 n-1 的最小值
    right_min = [0] * n
    right_min[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], nums[i])

    # 计算美丽值总和
    beauty_sum = 0
    for i in range(1, n - 1):
        if left_max[i - 1] < nums[i] < right_min[i + 1]:
            beauty_sum += 2
        elif nums[i - 1] < nums[i] < nums[i + 1]:
            beauty_sum += 1

    return beauty_sum


Solution = create_solution(sum_of_beauty)