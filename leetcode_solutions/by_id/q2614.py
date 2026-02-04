# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2614
标题: Maximum Count of Positive Integer and Negative Integer
难度: easy
链接: https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/
题目类型: 数组、二分查找、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2529. 正整数和负整数的最大计数 - 给你一个按 非递减顺序 排列的数组 nums ，返回正整数数目和负整数数目中的最大值。 * 换句话讲，如果 nums 中正整数的数目是 pos ，而负整数的数目是 neg ，返回 pos 和 neg二者中的最大值。 注意：0 既不是正整数也不是负整数。 示例 1： 输入：nums = [-2,-1,-1,1,2,3] 输出：3 解释：共有 3 个正整数和 3 个负整数。计数得到的最大值是 3 。 示例 2： 输入：nums = [-3,-2,-1,0,0,1,2] 输出：3 解释：共有 2 个正整数和 3 个负整数。计数得到的最大值是 3 。 示例 3： 输入：nums = [5,20,66,1314] 输出：4 解释：共有 4 个正整数和 0 个负整数。计数得到的最大值是 4 。 提示： * 1 <= nums.length <= 2000 * -2000 <= nums[i] <= 2000 * nums 按 非递减顺序 排列。 进阶：你可以设计并实现时间复杂度为 O(log(n)) 的算法解决此问题吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来找到第一个非负数的位置，从而确定正数和负数的数量。

算法步骤:
1. 使用二分查找找到第一个非负数的位置。
2. 计算负数的数量和正数的数量。
3. 返回两者中的最大值。

关键点:
- 二分查找的时间复杂度为 O(log n)，可以高效地找到第一个非负数的位置。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n)
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
    函数式接口 - 使用二分查找找到第一个非负数的位置，从而确定正数和负数的数量。
    """
    def binary_search_left(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    # 找到第一个非负数的位置
    first_non_negative_index = binary_search_left(nums, 0)

    # 计算负数的数量
    negative_count = first_non_negative_index

    # 计算正数的数量
    positive_count = len(nums) - first_non_negative_index - (nums[first_non_negative_index] == 0)

    # 返回两者中的最大值
    return max(negative_count, positive_count)


Solution = create_solution(solution_function_name)