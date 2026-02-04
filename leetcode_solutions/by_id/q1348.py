# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1348
标题: Maximum Score Of Spliced Array
难度: hard
链接: https://leetcode.cn/problems/maximum-score-of-spliced-array/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2321. 拼接数组的最大分数 - 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，长度都是 n 。 你可以选择两个整数 left 和 right ，其中 0 <= left <= right < n ，接着 交换 两个子数组 nums1[left...right] 和 nums2[left...right] 。 * 例如，设 nums1 = [1,2,3,4,5] 和 nums2 = [11,12,13,14,15] ，整数选择 left = 1 和 right = 2，那么 nums1 会变为 [1,12,13,4,5] 而 nums2 会变为 [11,2,3,14,15] 。 你可以选择执行上述操作 一次 或不执行任何操作。 数组的 分数 取 sum(nums1) 和 sum(nums2) 中的最大值，其中 sum(arr) 是数组 arr 中所有元素之和。 返回 可能的最大分数 。 子数组 是数组中连续的一个元素序列。arr[left...right] 表示子数组包含 nums 中下标 left 和 right 之间的元素（含 下标 left 和 right 对应元素）。 示例 1： 输入：nums1 = [60,60,60], nums2 = [10,90,10] 输出：210 解释：选择 left = 1 和 right = 1 ，得到 nums1 = [60,90,60] 和 nums2 = [10,60,10] 。 分数为 max(sum(nums1), sum(nums2)) = max(210, 80) = 210 。 示例 2： 输入：nums1 = [20,40,20,70,30], nums2 = [50,20,50,40,20] 输出：220 解释：选择 left = 3 和 right = 4 ，得到 nums1 = [20,40,20,40,20] 和 nums2 = [50,20,50,70,30] 。 分数为 max(sum(nums1), sum(nums2)) = max(140, 220) = 220 。 示例 3： 输入：nums1 = [7,11,13], nums2 = [1,1,1] 输出：31 解释：选择不交换任何子数组。 分数为 max(sum(nums1), sum(nums2)) = max(31, 3) = 31 。 提示： * n == nums1.length == nums2.length * 1 <= n <= 105 * 1 <= nums1[i], nums2[i] <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来找到可以交换的最大子数组差值，并将其加到原始数组的总和上。

算法步骤:
1. 计算 nums1 和 nums2 的初始总和。
2. 使用动态规划计算可以交换的最大子数组差值。
3. 更新最大分数。

关键点:
- 动态规划的状态转移方程是 dp[i] = max(dp[i-1] + diff, diff)，其中 diff = nums2[i] - nums1[i]。
- 通过两次遍历分别计算从左到右和从右到左的最大子数组差值。
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


def solution_function_name(nums1: List[int], nums2: List[int]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    n = len(nums1)
    sum1 = sum(nums1)
    sum2 = sum(nums2)

    # 从左到右计算最大子数组差值
    max_diff_left_to_right = 0
    current_diff = 0
    for i in range(n):
        diff = nums2[i] - nums1[i]
        current_diff = max(current_diff + diff, diff)
        max_diff_left_to_right = max(max_diff_left_to_right, current_diff)

    # 从右到左计算最大子数组差值
    max_diff_right_to_left = 0
    current_diff = 0
    for i in range(n - 1, -1, -1):
        diff = nums1[i] - nums2[i]
        current_diff = max(current_diff + diff, diff)
        max_diff_right_to_left = max(max_diff_right_to_left, current_diff)

    # 更新最大分数
    max_score = max(sum1 + max_diff_left_to_right, sum2 + max_diff_right_to_left)
    return max_score


Solution = create_solution(solution_function_name)