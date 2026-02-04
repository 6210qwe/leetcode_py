# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 993
标题: Tallest Billboard
难度: hard
链接: https://leetcode.cn/problems/tallest-billboard/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
956. 最高的广告牌 - 你正在安装一个广告牌，并希望它高度最大。这块广告牌将有两个钢制支架，两边各一个。每个钢支架的高度必须相等。 你有一堆可以焊接在一起的钢筋 rods。举个例子，如果钢筋的长度为 1、2 和 3，则可以将它们焊接在一起形成长度为 6 的支架。 返回 广告牌的最大可能安装高度 。如果没法安装广告牌，请返回 0 。 示例 1： 输入：[1,2,3,6] 输出：6 解释：我们有两个不相交的子集 {1,2,3} 和 {6}，它们具有相同的和 sum = 6。 示例 2： 输入：[1,2,3,4,5,6] 输出：10 解释：我们有两个不相交的子集 {2,3,5} 和 {4,6}，它们具有相同的和 sum = 10。 示例 3： 输入：[1,2] 输出：0 解释：没法安装广告牌，所以返回 0。 提示： 1. 0 <= rods.length <= 20 2. 1 <= rods[i] <= 1000 3. sum(rods[i]) <= 5000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们使用一个字典 `dp` 来记录在某个高度差下的最大高度。初始时，`dp[0] = 0` 表示高度差为 0 时的最大高度为 0。

算法步骤:
1. 初始化 `dp` 字典，其中 `dp[0] = 0`。
2. 遍历每个钢筋，对于每个钢筋，创建一个新的字典 `new_dp` 来存储当前状态。
3. 对于每个高度差 `diff`，有三种选择：
   - 不使用当前钢筋。
   - 将当前钢筋加到较高的那一边。
   - 将当前钢筋加到较低的那一边。
4. 更新 `dp` 为 `new_dp`。
5. 最后，返回 `dp[0]`，即高度差为 0 时的最大高度。

关键点:
- 使用字典来存储高度差和对应的最大高度，避免了不必要的空间浪费。
- 通过动态规划的方法，逐步构建出最终的解。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是钢筋的数量，m 是钢筋长度的总和。
空间复杂度: O(m)，因为 `dp` 字典的大小最多为 m。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def tallestBillboard(rods: List[int]) -> int:
    """
    函数式接口 - 实现最高的广告牌
    """
    dp = {0: 0}
    
    for rod in rods:
        new_dp = dp.copy()
        for diff, taller in dp.items():
            shorter = taller - diff
            # 不使用当前钢筋
            if diff not in new_dp:
                new_dp[diff] = taller
            else:
                new_dp[diff] = max(new_dp[diff], taller)
            
            # 将当前钢筋加到较高的一边
            new_diff = diff + rod
            if new_diff not in new_dp:
                new_dp[new_diff] = taller + rod
            else:
                new_dp[new_diff] = max(new_dp[new_diff], taller + rod)
            
            # 将当前钢筋加到较低的一边
            new_diff = abs(diff - rod)
            new_taller = max(taller, shorter + rod)
            if new_diff not in new_dp:
                new_dp[new_diff] = new_taller
            else:
                new_dp[new_diff] = max(new_dp[new_diff], new_taller)
        
        dp = new_dp
    
    return dp[0]


Solution = create_solution(tallestBillboard)