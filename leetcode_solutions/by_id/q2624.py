# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2624
标题: Difference Between Element Sum and Digit Sum of an Array
难度: easy
链接: https://leetcode.cn/problems/difference-between-element-sum-and-digit-sum-of-an-array/
题目类型: 数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2535. 数组元素和与数字和的绝对差 - 给你一个正整数数组 nums 。 * 元素和 是 nums 中的所有元素相加求和。 * 数字和 是 nums 中每一个元素的每一数位（重复数位需多次求和）相加求和。 返回 元素和 与 数字和 的绝对差。 注意：两个整数 x 和 y 的绝对差定义为 |x - y| 。 示例 1： 输入：nums = [1,15,6,3] 输出：9 解释： nums 的元素和是 1 + 15 + 6 + 3 = 25 。 nums 的数字和是 1 + 1 + 5 + 6 + 3 = 16 。 元素和与数字和的绝对差是 |25 - 16| = 9 。 示例 2： 输入：nums = [1,2,3,4] 输出：0 解释： nums 的元素和是 1 + 2 + 3 + 4 = 10 。 nums 的数字和是 1 + 2 + 3 + 4 = 10 。 元素和与数字和的绝对差是 |10 - 10| = 0 。 提示： * 1 <= nums.length <= 2000 * 1 <= nums[i] <= 2000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 计算数组的元素和与数字和，然后返回它们的绝对差。

算法步骤:
1. 初始化两个变量 `element_sum` 和 `digit_sum` 分别用于存储元素和和数字和。
2. 遍历数组 `nums`，累加每个元素到 `element_sum`。
3. 对于每个元素，将其每一位数字累加到 `digit_sum`。
4. 返回 `element_sum` 和 `digit_sum` 的绝对差。

关键点:
- 使用整数除法和取模操作来提取每个数字的每一位。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * d)，其中 n 是数组长度，d 是数组中最大数字的位数。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def difference_between_element_sum_and_digit_sum(nums: List[int]) -> int:
    """
    计算数组的元素和与数字和的绝对差。
    """
    element_sum = 0
    digit_sum = 0

    for num in nums:
        element_sum += num
        while num > 0:
            digit_sum += num % 10
            num //= 10

    return abs(element_sum - digit_sum)


Solution = create_solution(difference_between_element_sum_and_digit_sum)