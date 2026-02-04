# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2694
标题: Find the Maximum Divisibility Score
难度: easy
链接: https://leetcode.cn/problems/find-the-maximum-divisibility-score/
题目类型: 数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2644. 找出可整除性得分最大的整数 - 给你两个整数数组 nums 和 divisors 。 divisors[i] 的 可整除性得分 等于满足 nums[j] 能被 divisors[i] 整除的下标 j 的数量。 返回 可整除性得分 最大的整数 divisors[i] 。如果有多个整数具有最大得分，则返回数值最小的一个。 示例 1： 输入：nums = [2,9,15,50], divisors = [5,3,7,2] 输出：2 解释： divisors[0] 的可整除性分数为 2 因为 nums[2] 和 nums[3] 能被 5 整除。 divisors[1] 的可整除性分数为 2 因为 nums[1] 和 nums[2] 能被 3 整除。 divisors[2] 的可整除性分数为 0 因为 nums 中没有数字能被 7 整除。 divisors[3] 的可整除性分数为 2 因为 nums[0] 和 nums[3] 能够被 2 整除。 因为 divisors[0] 、divisor[1] 和 divisors[3] 有相同的可整除性分数，我们返回更小的那个 divisors[3]。 示例 2： 输入：nums = [4,7,9,3,9], divisors = [5,2,3] 输出：3 解释： divisors[0] 的可整除性分数为 0 因为 nums 中没有数字能被 5 整除。 divisors[1] 的可整除性分数为 1 因为只有 nums[0] 能被 2 整除。 divisors[2] 的可整除性分数为 3 因为 nums[2] ，nums[3] 和 nums[4] 能被 3 整除。 示例 3： 输入：nums = [20,14,21,10], divisors = [10,16,20] 输出：10 解释： divisors[0] 的可整除性分数为 2 因为 nums[0] 和 nums[3] 能被 10 整除。 divisors[1] 的可整除性分数为 0 因为 nums 中没有数字能被 16 整除。 divisors[2] 的可整除性分数为 1 因为 nums[0] 能被 20 整除。 因为 divisors[0] 的可整除性分数最大，我们返回 divisors[0]。 提示： * 1 <= nums.length, divisors.length <= 1000 * 1 <= nums[i], divisors[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 对每个 divisors 中的元素，计算其在 nums 中的可整除性得分，并记录最大得分及其对应的最小 divisors 值。

算法步骤:
1. 初始化最大得分 max_score 为 0，以及结果 res 为无穷大。
2. 遍历每个 divisors 中的元素 d：
   - 计算 d 在 nums 中的可整除性得分 score。
   - 如果 score 大于 max_score，更新 max_score 和 res。
   - 如果 score 等于 max_score 且 d 小于 res，更新 res。
3. 返回 res。

关键点:
- 使用一个变量来记录当前的最大得分和对应的最小 divisors 值。
- 通过遍历 divisors 和 nums 来计算每个 divisors 的得分。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 nums 的长度，m 是 divisors 的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_max_divisibility_score(nums: List[int], divisors: List[int]) -> int:
    """
    函数式接口 - 找出可整除性得分最大的整数
    """
    max_score = 0
    res = float('inf')
    
    for d in divisors:
        score = sum(num % d == 0 for num in nums)
        if score > max_score or (score == max_score and d < res):
            max_score = score
            res = d
    
    return res


Solution = create_solution(find_max_divisibility_score)