# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2539
标题: Minimum Number of Operations to Make Arrays Similar
难度: hard
链接: https://leetcode.cn/problems/minimum-number-of-operations-to-make-arrays-similar/
题目类型: 贪心、数组、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2449. 使数组相似的最少操作次数 - 给你两个正整数数组 nums 和 target ，两个数组长度相等。 在一次操作中，你可以选择两个 不同 的下标 i 和 j ，其中 0 <= i, j < nums.length ，并且： * 令 nums[i] = nums[i] + 2 且 * 令 nums[j] = nums[j] - 2 。 如果两个数组中每个元素出现的频率相等，我们称两个数组是 相似 的。 请你返回将 nums 变得与 target 相似的最少操作次数。测试数据保证 nums 一定能变得与 target 相似。 示例 1： 输入：nums = [8,12,6], target = [2,14,10] 输出：2 解释：可以用两步操作将 nums 变得与 target 相似： - 选择 i = 0 和 j = 2 ，nums = [10,12,4] 。 - 选择 i = 1 和 j = 2 ，nums = [10,14,2] 。 2 次操作是最少需要的操作次数。 示例 2： 输入：nums = [1,2,5], target = [4,1,3] 输出：1 解释：一步操作可以使 nums 变得与 target 相似： - 选择 i = 1 和 j = 2 ，nums = [1,4,3] 。 示例 3： 输入：nums = [1,1,1,1,1], target = [1,1,1,1,1] 输出：0 解释：数组 nums 已经与 target 相似。 提示： * n == nums.length == target.length * 1 <= n <= 105 * 1 <= nums[i], target[i] <= 106 * nums 一定可以变得与 target 相似。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过排序和贪心算法，计算将 nums 变得与 target 相似的最少操作次数。

算法步骤:
1. 将 nums 和 target 分别按奇偶性分成两个子数组。
2. 对每个子数组进行排序。
3. 计算两个子数组中对应位置元素的差值之和，除以 4 即为所需操作次数。

关键点:
- 通过分组和排序，确保每次操作都能最大化减少差异。
- 由于每次操作只能改变两个元素的奇偶性，因此需要分别处理奇数和偶数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是数组的长度，因为排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，需要额外的空间来存储奇偶子数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def make_arrays_similar(nums: List[int], target: List[int]) -> int:
    """
    函数式接口 - 计算将 nums 变得与 target 相似的最少操作次数
    """
    # 将 nums 和 target 分别按奇偶性分成两个子数组
    nums_odd = [num for num in nums if num % 2 != 0]
    nums_even = [num for num in nums if num % 2 == 0]
    target_odd = [num for num in target if num % 2 != 0]
    target_even = [num for num in target if num % 2 == 0]

    # 对每个子数组进行排序
    nums_odd.sort()
    nums_even.sort()
    target_odd.sort()
    target_even.sort()

    # 计算两个子数组中对应位置元素的差值之和
    operations = 0
    for i in range(len(nums_odd)):
        operations += abs(nums_odd[i] - target_odd[i])
    for i in range(len(nums_even)):
        operations += abs(nums_even[i] - target_even[i])

    # 由于每次操作可以减少 4 的差距，所以结果除以 4
    return operations // 4


Solution = create_solution(make_arrays_similar)