# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3714
标题: Maximum and Minimum Sums of at Most Size K Subsequences
难度: medium
链接: https://leetcode.cn/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/
题目类型: 数组、数学、动态规划、组合数学、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3428. 最多 K 个元素的子序列的最值之和 - 给你一个整数数组 nums 和一个正整数 k，返回所有长度最多为 k 的 子序列 中 最大值 与 最小值 之和的总和。 非空子序列 是指从另一个数组中删除一些或不删除任何元素（且不改变剩余元素的顺序）得到的数组。 由于答案可能非常大，请返回对 109 + 7 取余数的结果。 示例 1： 输入： nums = [1,2,3], k = 2 输出： 24 解释： 数组 nums 中所有长度最多为 2 的子序列如下： 子序列 最小值 最大值 和 [1] 1 1 2 [2] 2 2 4 [3] 3 3 6 [1, 2] 1 2 3 [1, 3] 1 3 4 [2, 3] 2 3 5 总和 24 因此，输出为 24。 示例 2： 输入： nums = [5,0,6], k = 1 输出： 22 解释： 对于长度恰好为 1 的子序列，最小值和最大值均为元素本身。因此，总和为 5 + 5 + 0 + 0 + 6 + 6 = 22。 示例 3： 输入： nums = [1,1,1], k = 2 输出： 12 解释： 子序列 [1, 1] 和 [1] 各出现 3 次。对于所有这些子序列，最小值和最大值均为 1。因此，总和为 12。 提示： * 1 <= nums.length <= 105 * 0 <= nums[i] <= 109 * 1 <= k <= min(100, nums.length)
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过前缀和计算每个元素作为最小值和最大值的贡献。

算法步骤:
1. 计算每个元素作为最小值的贡献。
2. 计算每个元素作为最大值的贡献。
3. 将两个贡献相加并取模。

关键点:
- 使用前缀和快速计算贡献。
- 注意处理边界情况和取模操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 nums 的长度。排序操作的时间复杂度为 O(n log n)，后续遍历的时间复杂度为 O(n)。
空间复杂度: O(n)，用于存储前缀和数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

MOD = 10**9 + 7

def solution_function_name(nums: List[int], k: int) -> int:
    """
    函数式接口 - 返回所有长度最多为 k 的子序列中最大值与最小值之和的总和。
    """
    n = len(nums)
    if n == 1:
        return 2 * nums[0] % MOD
    
    # 计算前缀和
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = (prefix_sum[i] + nums[i]) % MOD
    
    # 排序并计算贡献
    sorted_nums = sorted((num, i) for i, num in enumerate(nums))
    
    def calculate_contribution(is_min: bool) -> int:
        contribution = 0
        count = 0
        for i in range(n):
            if is_min:
                contribution += nums[sorted_nums[i][1]] * (prefix_sum[min(i + k, n)] - prefix_sum[i])
            else:
                contribution += nums[sorted_nums[i][1]] * (prefix_sum[i + 1] - prefix_sum[max(i - k + 1, 0)])
            contribution %= MOD
        return contribution
    
    min_contribution = calculate_contribution(True)
    max_contribution = calculate_contribution(False)
    
    return (min_contribution + max_contribution) % MOD

Solution = create_solution(solution_function_name)