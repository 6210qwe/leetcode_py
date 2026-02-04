# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3593
标题: Find the Maximum Factor Score of Array
难度: medium
链接: https://leetcode.cn/problems/find-the-maximum-factor-score-of-array/
题目类型: 数组、数学、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3334. 数组的最大因子得分 - 给你一个整数数组 nums。 因子得分 定义为数组所有元素的最小公倍数（LCM）与最大公约数（GCD）的 乘积。 在 最多 移除一个元素的情况下，返回 nums 的 最大因子得分。 注意，单个数字的 LCM 和 GCD 都是其本身，而 空数组 的因子得分为 0。 示例 1： 输入： nums = [2,4,8,16] 输出： 64 解释： 移除数字 2 后，剩余元素的 GCD 为 4，LCM 为 16，因此最大因子得分为 4 * 16 = 64。 示例 2： 输入： nums = [1,2,3,4,5] 输出： 60 解释： 无需移除任何元素即可获得最大因子得分 60。 示例 3： 输入： nums = [3] 输出： 9 提示： * 1 <= nums.length <= 100 * 1 <= nums[i] <= 30
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 计算数组的所有元素的 LCM 和 GCD，并在最多移除一个元素的情况下，找到最大因子得分。

算法步骤:
1. 计算整个数组的 LCM 和 GCD。
2. 遍历数组，每次移除一个元素，计算剩余元素的 LCM 和 GCD。
3. 更新最大因子得分。

关键点:
- 使用 math 库中的 gcd 函数来计算 GCD。
- 使用 reduce 函数和 lcm 函数来计算 LCM。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * log(max(nums)))，其中 n 是数组长度，log(max(nums)) 是计算 LCM 和 GCD 的时间复杂度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def max_factor_score(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0] ** 2
    
    def array_lcm(arr):
        return reduce(lcm, arr)
    
    def array_gcd(arr):
        return reduce(gcd, arr)
    
    full_lcm = array_lcm(nums)
    full_gcd = array_gcd(nums)
    max_score = full_lcm * full_gcd
    
    for i in range(len(nums)):
        new_nums = nums[:i] + nums[i+1:]
        new_lcm = array_lcm(new_nums)
        new_gcd = array_gcd(new_nums)
        max_score = max(max_score, new_lcm * new_gcd)
    
    return max_score

Solution = create_solution(max_factor_score)