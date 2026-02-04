# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2368
标题: Sum of Total Strength of Wizards
难度: hard
链接: https://leetcode.cn/problems/sum-of-total-strength-of-wizards/
题目类型: 栈、数组、前缀和、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2281. 巫师的总力量和 - 作为国王的统治者，你有一支巫师军队听你指挥。 给你一个下标从 0 开始的整数数组 strength ，其中 strength[i] 表示第 i 位巫师的力量值。对于连续的一组巫师（也就是这些巫师的力量值是 strength 的 子数组），总力量 定义为以下两个值的 乘积 ： * 巫师中 最弱 的能力值。 * 组中所有巫师的个人力量值 之和 。 请你返回 所有 巫师组的 总 力量之和。由于答案可能很大，请将答案对 109 + 7 取余 后返回。 子数组 是一个数组里 非空 连续子序列。 示例 1： 输入：strength = [1,3,1,2] 输出：44 解释：以下是所有连续巫师组： - [1,3,1,2] 中 [1] ，总力量值为 min([1]) * sum([1]) = 1 * 1 = 1 - [1,3,1,2] 中 [3] ，总力量值为 min([3]) * sum([3]) = 3 * 3 = 9 - [1,3,1,2] 中 [1] ，总力量值为 min([1]) * sum([1]) = 1 * 1 = 1 - [1,3,1,2] 中 [2] ，总力量值为 min([2]) * sum([2]) = 2 * 2 = 4 - [1,3,1,2] 中 [1,3] ，总力量值为 min([1,3]) * sum([1,3]) = 1 * 4 = 4 - [1,3,1,2] 中 [3,1] ，总力量值为 min([3,1]) * sum([3,1]) = 1 * 4 = 4 - [1,3,1,2] 中 [1,2] ，总力量值为 min([1,2]) * sum([1,2]) = 1 * 3 = 3 - [1,3,1,2] 中 [1,3,1] ，总力量值为 min([1,3,1]) * sum([1,3,1]) = 1 * 5 = 5 - [1,3,1,2] 中 [3,1,2] ，总力量值为 min([3,1,2]) * sum([3,1,2]) = 1 * 6 = 6 - [1,3,1,2] 中 [1,3,1,2] ，总力量值为 min([1,3,1,2]) * sum([1,3,1,2]) = 1 * 7 = 7 所有力量值之和为 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44 。 示例 2： 输入：strength = [5,4,6] 输出：213 解释：以下是所有连续巫师组： - [5,4,6] 中 [5] ，总力量值为 min([5]) * sum([5]) = 5 * 5 = 25 - [5,4,6] 中 [4] ，总力量值为 min([4]) * sum([4]) = 4 * 4 = 16 - [5,4,6] 中 [6] ，总力量值为 min([6]) * sum([6]) = 6 * 6 = 36 - [5,4,6] 中 [5,4] ，总力量值为 min([5,4]) * sum([5,4]) = 4 * 9 = 36 - [5,4,6] 中 [4,6] ，总力量值为 min([4,6]) * sum([4,6]) = 4 * 10 = 40 - [5,4,6] 中 [5,4,6] ，总力量值为 min([5,4,6]) * sum([5,4,6]) = 4 * 15 = 60 所有力量值之和为 25 + 16 + 36 + 36 + 40 + 60 = 213 。 提示： * 1 <= strength.length <= 105 * 1 <= strength[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用单调栈来找到每个元素作为最小值时的贡献。

算法步骤:
1. 计算前缀和数组 `prefix_sum` 和前缀和的前缀和数组 `prefix_prefix_sum`。
2. 使用单调栈找到每个元素作为最小值时的左右边界。
3. 计算每个元素作为最小值时的贡献，并累加到结果中。

关键点:
- 使用单调栈来高效地找到每个元素作为最小值时的左右边界。
- 使用前缀和数组和前缀和的前缀和数组来快速计算区间和。
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


def total_strength(strength: List[int]) -> int:
    MOD = 10**9 + 7
    n = len(strength)
    
    # 计算前缀和数组
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = (prefix_sum[i - 1] + strength[i - 1]) % MOD
    
    # 计算前缀和的前缀和数组
    prefix_prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_prefix_sum[i] = (prefix_prefix_sum[i - 1] + prefix_sum[i]) % MOD
    
    # 单调栈
    stack = []
    left_bound = [0] * n
    right_bound = [0] * n
    
    # 找到每个元素作为最小值时的左边界
    for i in range(n):
        while stack and strength[stack[-1]] >= strength[i]:
            stack.pop()
        left_bound[i] = stack[-1] if stack else -1
        stack.append(i)
    
    stack = []
    # 找到每个元素作为最小值时的右边界
    for i in range(n - 1, -1, -1):
        while stack and strength[stack[-1]] > strength[i]:
            stack.pop()
        right_bound[i] = stack[-1] if stack else n
        stack.append(i)
    
    result = 0
    for i in range(n):
        left = left_bound[i]
        right = right_bound[i]
        
        # 计算左侧区间和
        left_sum = (prefix_prefix_sum[i] - prefix_prefix_sum[max(0, left + 1)] + MOD) % MOD
        left_count = i - max(0, left)
        
        # 计算右侧区间和
        right_sum = (prefix_prefix_sum[right] - prefix_prefix_sum[i + 1] + MOD) % MOD
        right_count = right - (i + 1)
        
        # 计算贡献
        result += (right_sum * left_count - left_sum * right_count) * strength[i]
        result %= MOD
    
    return result


Solution = create_solution(total_strength)