# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2714
标题: Left and Right Sum Differences
难度: easy
链接: https://leetcode.cn/problems/left-and-right-sum-differences/
题目类型: 数组、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2574. 左右元素和的差值 - 给你一个下标从 0 开始的长度为 n 的整数数组 nums。 定义两个数组 leftSum 和 rightSum，其中： * leftSum[i] 是数组 nums 中下标 i 左侧元素之和。如果不存在对应的元素，leftSum[i] = 0 。 * rightSum[i] 是数组 nums 中下标 i 右侧元素之和。如果不存在对应的元素，rightSum[i] = 0 。 返回长度为 n 数组 answer，其中 answer[i] = |leftSum[i] - rightSum[i]|。 示例 1： 输入：nums = [10,4,8,3] 输出：[15,1,11,22] 解释：数组 leftSum 为 [0,10,14,22] 且数组 rightSum 为 [15,11,3,0] 。 数组 answer 为 [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22] 。 示例 2： 输入：nums = [1] 输出：[0] 解释：数组 leftSum 为 [0] 且数组 rightSum 为 [0] 。 数组 answer 为 [|0 - 0|] = [0] 。 提示： * 1 <= nums.length <= 1000 * 1 <= nums[i] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和来计算 leftSum 和 rightSum，从而在 O(n) 时间内完成计算。

算法步骤:
1. 计算数组 nums 的前缀和 pre_sum。
2. 初始化 leftSum 和 rightSum 数组。
3. 通过前缀和计算每个位置的 leftSum 和 rightSum。
4. 计算每个位置的 |leftSum[i] - rightSum[i]| 并存储在结果数组中。

关键点:
- 使用前缀和可以在 O(n) 时间内计算 leftSum 和 rightSum。
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


def left_right_sum_diff(nums: List[int]) -> List[int]:
    """
    函数式接口 - 计算左右元素和的差值
    """
    n = len(nums)
    if n == 1:
        return [0]

    # 计算前缀和
    pre_sum = [0] * (n + 1)
    for i in range(n):
        pre_sum[i + 1] = pre_sum[i] + nums[i]

    # 初始化 leftSum 和 rightSum 数组
    left_sum = [0] * n
    right_sum = [0] * n

    # 计算 leftSum 和 rightSum
    for i in range(n):
        left_sum[i] = pre_sum[i]
        right_sum[i] = pre_sum[n] - pre_sum[i + 1]

    # 计算结果
    result = [abs(left_sum[i] - right_sum[i]) for i in range(n)]
    return result


Solution = create_solution(left_right_sum_diff)