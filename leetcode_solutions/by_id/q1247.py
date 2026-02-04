# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1247
标题: Decrease Elements To Make Array Zigzag
难度: medium
链接: https://leetcode.cn/problems/decrease-elements-to-make-array-zigzag/
题目类型: 贪心、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1144. 递减元素使数组呈锯齿状 - 给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。 如果符合下列情况之一，则数组 A 就是 锯齿数组： * 每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ... * 或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ... 返回将数组 nums 转换为锯齿数组所需的最小操作次数。 示例 1： 输入：nums = [1,2,3] 输出：2 解释：我们可以把 2 递减到 0，或把 3 递减到 1。 示例 2： 输入：nums = [9,6,1,6,2] 输出：4 提示： * 1 <= nums.length <= 1000 * 1 <= nums[i] <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过贪心算法，分别计算以偶数索引和奇数索引开头的锯齿数组所需的操作次数，取两者中的最小值。

算法步骤:
1. 定义一个辅助函数 `min_moves`，用于计算从某个起始位置开始构建锯齿数组所需的最小操作次数。
2. 在主函数中，分别调用 `min_moves` 计算以偶数索引和奇数索引开头的锯齿数组所需的操作次数。
3. 返回两者中的最小值。

关键点:
- 使用贪心算法，每次只考虑当前元素和其相邻元素的关系。
- 分别计算两种可能的锯齿数组（以偶数索引和奇数索引开头），取最小操作次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是数组的长度。我们需要遍历数组两次，每次遍历的时间复杂度是 O(n)。
空间复杂度: O(1)，我们只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_moves(nums: List[int], start: int) -> int:
    moves = 0
    for i in range(start, len(nums), 2):
        if i == 0:
            if nums[i] <= nums[i + 1]:
                moves += (nums[i + 1] - nums[i]) + 1
                nums[i] = nums[i + 1] + 1
        elif i == len(nums) - 1:
            if nums[i] <= nums[i - 1]:
                moves += (nums[i - 1] - nums[i]) + 1
                nums[i] = nums[i - 1] + 1
        else:
            if nums[i] <= nums[i - 1]:
                diff = (nums[i - 1] - nums[i]) + 1
                moves += diff
                nums[i] = nums[i - 1] + 1
            if nums[i] <= nums[i + 1]:
                diff = (nums[i + 1] - nums[i]) + 1
                moves += diff
                nums[i] = nums[i + 1] + 1
    return moves


def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 计算将数组转换为锯齿数组所需的最小操作次数
    """
    # 计算以偶数索引和奇数索引开头的锯齿数组所需的操作次数
    moves_even = min_moves(nums[:], 0)
    moves_odd = min_moves(nums[:], 1)
    
    # 返回两者中的最小值
    return min(moves_even, moves_odd)


Solution = create_solution(solution_function_name)