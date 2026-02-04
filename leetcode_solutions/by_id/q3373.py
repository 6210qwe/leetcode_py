# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3373
标题: Maximum Prime Difference
难度: medium
链接: https://leetcode.cn/problems/maximum-prime-difference/
题目类型: 数组、数学、数论
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3115. 质数的最大距离 - 给你一个整数数组 nums。 返回两个（不一定不同的）质数在 nums 中 下标 的 最大距离。 示例 1： 输入： nums = [4,2,9,5,3] 输出： 3 解释： nums[1]、nums[3] 和 nums[4] 是质数。因此答案是 |4 - 1| = 3。 示例 2： 输入： nums = [4,8,2,8] 输出： 0 解释： nums[2] 是质数。因为只有一个质数，所以答案是 |2 - 2| = 0。 提示： * 1 <= nums.length <= 3 * 105 * 1 <= nums[i] <= 100 * 输入保证 nums 中至少有一个质数。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用埃拉托斯特尼筛法预处理所有可能的质数，并在遍历数组时记录质数的位置，最后计算最大距离。

算法步骤:
1. 使用埃拉托斯特尼筛法生成 1 到 100 之间的所有质数。
2. 遍历数组，记录每个质数的下标。
3. 计算质数下标之间的最大距离。

关键点:
- 使用埃拉托斯特尼筛法高效生成质数。
- 在遍历数组时记录质数下标，并计算最大距离。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + log(log(max_num)))，其中 n 是数组长度，max_num 是数组中的最大值（这里是 100）。
空间复杂度: O(max_num)，用于存储质数。
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
    函数式接口 - 返回两个（不一定不同的）质数在 nums 中下标的最大距离。
    """
    # 生成 1 到 100 之间的所有质数
    max_num = 100
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    # 记录质数的下标
    prime_indices = []
    for i, num in enumerate(nums):
        if is_prime[num]:
            prime_indices.append(i)

    # 计算质数下标之间的最大距离
    if len(prime_indices) == 1:
        return 0
    else:
        return max(prime_indices[-1] - prime_indices[0], 0)


Solution = create_solution(solution_function_name)