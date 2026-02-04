# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2322
标题: Number of Ways to Build Sturdy Brick Wall
难度: medium
链接: https://leetcode.cn/problems/number-of-ways-to-build-sturdy-brick-wall/
题目类型: 位运算、数组、动态规划、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2184. 建造坚实的砖墙的方法数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和状态压缩来解决这个问题。我们用一个整数表示当前行的状态，每一位表示该位置是否有砖块。通过预处理所有可能的状态及其对应的下一个状态，然后使用动态规划计算每个状态的方案数。

算法步骤:
1. 预处理所有可能的状态及其对应的下一个状态。
2. 初始化动态规划数组，dp[i] 表示状态 i 的方案数。
3. 遍历每一层，更新动态规划数组。
4. 返回最终结果。

关键点:
- 使用位运算来表示和处理状态。
- 通过预处理减少重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n * n + m * 2^n)，其中 n 是墙的宽度，m 是墙的高度。
空间复杂度: O(2^n)，用于存储动态规划数组和预处理的状态。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def count_sturdy_walls(height: int, width: int) -> int:
    MOD = 10**9 + 7
    
    # 生成所有可能的状态
    def generate_states(w):
        states = []
        for i in range(1 << w):
            if i & (i << 1) == 0 and i & (i >> 1) == 0:
                states.append(i)
        return states
    
    # 生成状态转移表
    def generate_transitions(states, w):
        transitions = {}
        for state in states:
            next_states = []
            for next_state in states:
                if state & next_state == 0:
                    next_states.append(next_state)
            transitions[state] = next_states
        return transitions
    
    states = generate_states(width)
    transitions = generate_transitions(states, width)
    
    # 动态规划
    dp = [0] * (1 << width)
    dp[0] = 1
    
    for _ in range(height):
        new_dp = [0] * (1 << width)
        for state in states:
            for next_state in transitions[state]:
                new_dp[next_state] += dp[state]
                new_dp[next_state] %= MOD
        dp = new_dp
    
    return sum(dp) % MOD

Solution = create_solution(count_sturdy_walls)