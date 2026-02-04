# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3443
标题: Maximum Total Reward Using Operations II
难度: hard
链接: https://leetcode.cn/problems/maximum-total-reward-using-operations-ii/
题目类型: 位运算、数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3181. 执行操作可获得的最大总奖励 II - 给你一个整数数组 rewardValues，长度为 n，代表奖励的值。 最初，你的总奖励 x 为 0，所有下标都是 未标记 的。你可以执行以下操作 任意次 ： * 从区间 [0, n - 1] 中选择一个 未标记 的下标 i。 * 如果 rewardValues[i] 大于 你当前的总奖励 x，则将 rewardValues[i] 加到 x 上（即 x = x + rewardValues[i]），并 标记 下标 i。 以整数形式返回执行最优操作能够获得的 最大 总奖励。 示例 1： 输入：rewardValues = [1,1,3,3] 输出：4 解释： 依次标记下标 0 和 2，总奖励为 4，这是可获得的最大值。 示例 2： 输入：rewardValues = [1,6,4,3,2] 输出：11 解释： 依次标记下标 0、2 和 1。总奖励为 11，这是可获得的最大值。 提示： * 1 <= rewardValues.length <= 5 * 104 * 1 <= rewardValues[i] <= 5 * 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和排序来实现。

算法步骤:
1. 对 rewardValues 进行排序。
2. 初始化总奖励 x 为 0。
3. 遍历排序后的 rewardValues，如果当前奖励大于 x，则将其加到 x 上，并标记该下标。
4. 返回最终的总奖励 x。

关键点:
- 通过排序确保每次选择的奖励值都是当前可行的最大值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 rewardValues 的长度，主要由排序操作决定。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(rewardValues: List[int]) -> int:
    """
    函数式接口 - 计算最大总奖励
    """
    # 对 rewardValues 进行排序
    rewardValues.sort()
    
    # 初始化总奖励 x 为 0
    x = 0
    
    # 遍历排序后的 rewardValues
    for reward in rewardValues:
        if reward > x:
            x += reward
    
    return x


Solution = create_solution(solution_function_name)