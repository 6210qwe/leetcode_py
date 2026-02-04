# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1138
标题: Grumpy Bookstore Owner
难度: medium
链接: https://leetcode.cn/problems/grumpy-bookstore-owner/
题目类型: 数组、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1052. 爱生气的书店老板 - 有一个书店老板，他的书店开了 n 分钟。每分钟都有一些顾客进入这家商店。给定一个长度为 n 的整数数组 customers ，其中 customers[i] 是在第 i 分钟开始时进入商店的顾客数量，所有这些顾客在第 i 分钟结束后离开。 在某些分钟内，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，若老板不生气则顾客是满意的。 书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 minutes 分钟不生气，但却只能使用一次。 请你返回 这一天营业下来，最多有多少客户能够感到满意 。 示例 1： 输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3 输出：16 解释：书店老板在最后 3 分钟保持冷静。 感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16. 示例 2： 输入：customers = [1], grumpy = [0], minutes = 1 输出：1 提示： * n == customers.length == grumpy.length * 1 <= minutes <= n <= 2 * 104 * 0 <= customers[i] <= 1000 * grumpy[i] == 0 or 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来找到使用秘密技巧的最佳时间段。

算法步骤:
1. 计算不使用秘密技巧时的满意顾客总数。
2. 使用滑动窗口计算在每个可能的时间段内使用秘密技巧可以增加的满意顾客数。
3. 选择使总满意顾客数最大的时间段。

关键点:
- 通过滑动窗口技术，可以在 O(n) 时间内找到最佳时间段。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def maxSatisfied(customers: List[int], grumpy: List[int], X: int) -> int:
    """
    函数式接口 - 返回最多有多少客户能够感到满意
    """
    n = len(customers)
    total_satisfied = 0
    max_additional_satisfied = 0
    current_additional_satisfied = 0
    
    # 计算不使用秘密技巧时的满意顾客总数
    for i in range(n):
        if grumpy[i] == 0:
            total_satisfied += customers[i]
    
    # 使用滑动窗口计算在每个可能的时间段内使用秘密技巧可以增加的满意顾客数
    for i in range(n):
        if i < X:
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]
        else:
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]
            if grumpy[i - X] == 1:
                current_additional_satisfied -= customers[i - X]
        
        max_additional_satisfied = max(max_additional_satisfied, current_additional_satisfied)
    
    return total_satisfied + max_additional_satisfied


Solution = create_solution(maxSatisfied)