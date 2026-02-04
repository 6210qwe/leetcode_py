# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2902
标题: Max Pair Sum in an Array
难度: easy
链接: https://leetcode.cn/problems/max-pair-sum-in-an-array/
题目类型: 数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2815. 数组中的最大数对和 - 给你一个下标从 0 开始的整数数组 nums 。请你从 nums 中找出和 最大 的一对数，且这两个数数位上最大的数字相等。 返回最大和，如果不存在满足题意的数字对，返回 -1 。 示例 1： 输入：nums = [51,71,17,24,42] 输出：88 解释： i = 1 和 j = 2 ，nums[i] 和 nums[j] 数位上最大的数字相等，且这一对的总和 71 + 17 = 88 。 i = 3 和 j = 4 ，nums[i] 和 nums[j] 数位上最大的数字相等，且这一对的总和 24 + 42 = 66 。 可以证明不存在其他数对满足数位上最大的数字相等，所以答案是 88 。 示例 2： 输入：nums = [1,2,3,4] 输出：-1 解释：不存在数对满足数位上最大的数字相等。 提示： * 2 <= nums.length <= 100 * 1 <= nums[i] <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个数位上最大数字相同的数的最大值，然后遍历哈希表找到最大和。

算法步骤:
1. 定义一个函数 `max_digit` 来获取一个数的最大数位。
2. 使用一个哈希表 `max_pairs` 来记录每个数位上最大数字相同的数的最大值。
3. 遍历数组 `nums`，对于每个数，获取其最大数位，并更新哈希表。
4. 遍历哈希表，找到最大和。

关键点:
- 使用哈希表来记录每个数位上最大数字相同的数的最大值，可以快速找到满足条件的数对。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)（因为数位范围固定在 0 到 9）
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_pair_sum(nums: List[int]) -> int:
    """
    函数式接口 - 找出数组中和最大的一对数，且这两个数数位上最大的数字相等。
    """
    def max_digit(num: int) -> int:
        """获取一个数的最大数位。"""
        return max(int(digit) for digit in str(num))

    max_pairs = {}
    for num in nums:
        digit = max_digit(num)
        if digit not in max_pairs:
            max_pairs[digit] = [num]
        else:
            max_pairs[digit].append(num)
            max_pairs[digit].sort(reverse=True)
            if len(max_pairs[digit]) > 2:
                max_pairs[digit].pop()

    max_sum = -1
    for digit, pair in max_pairs.items():
        if len(pair) == 2:
            max_sum = max(max_sum, sum(pair))
    
    return max_sum


Solution = create_solution(max_pair_sum)