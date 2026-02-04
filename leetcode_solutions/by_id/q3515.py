# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3515
标题: Find if Digit Game Can Be Won
难度: easy
链接: https://leetcode.cn/problems/find-if-digit-game-can-be-won/
题目类型: 数组、数学
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3232. 判断是否可以赢得数字游戏 - 给你一个 正整数 数组 nums。 Alice 和 Bob 正在玩游戏。在游戏中，Alice 可以从 nums 中选择所有个位数 或 所有两位数，剩余的数字归 Bob 所有。如果 Alice 所选数字之和 严格大于 Bob 的数字之和，则 Alice 获胜。 如果 Alice 能赢得这场游戏，返回 true；否则，返回 false。 示例 1： 输入：nums = [1,2,3,4,10] 输出：false 解释： Alice 不管选个位数还是两位数都无法赢得比赛。 示例 2： 输入：nums = [1,2,3,4,5,14] 输出：true 解释： Alice 选择个位数可以赢得比赛，所选数字之和为 15。 示例 3： 输入：nums = [5,5,5,25] 输出：true 解释： Alice 选择两位数可以赢得比赛，所选数字之和为 25。 提示： * 1 <= nums.length <= 100 * 1 <= nums[i] <= 99
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 计算个位数和两位数的总和，分别与剩余数字的总和进行比较，判断 Alice 是否能赢。

算法步骤:
1. 初始化两个变量 `one_digit_sum` 和 `two_digit_sum` 分别存储个位数和两位数的总和。
2. 遍历数组 `nums`，将个位数和两位数分别累加到 `one_digit_sum` 和 `two_digit_sum`。
3. 计算剩余数字的总和 `total_sum` 减去 `one_digit_sum` 和 `two_digit_sum`。
4. 比较 `one_digit_sum` 和 `two_digit_sum` 与 `total_sum` 的差值，判断 Alice 是否能赢。

关键点:
- 通过一次遍历计算个位数和两位数的总和，避免多次遍历。
- 通过比较两种情况下的差值来判断 Alice 是否能赢。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历数组一次。
空间复杂度: O(1) - 只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_win_digit_game(nums: List[int]) -> bool:
    """
    判断 Alice 是否能赢得数字游戏。
    """
    one_digit_sum = 0
    two_digit_sum = 0
    total_sum = sum(nums)
    
    for num in nums:
        if num < 10:
            one_digit_sum += num
        else:
            two_digit_sum += num
    
    # 计算剩余数字的总和
    remaining_sum_one_digit = total_sum - one_digit_sum
    remaining_sum_two_digit = total_sum - two_digit_sum
    
    # 判断 Alice 是否能赢
    return one_digit_sum > remaining_sum_one_digit or two_digit_sum > remaining_sum_two_digit


Solution = create_solution(can_win_digit_game)