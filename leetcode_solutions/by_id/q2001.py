# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2001
标题: Jump Game VII
难度: medium
链接: https://leetcode.cn/problems/jump-game-vii/
题目类型: 字符串、动态规划、前缀和、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1871. 跳跃游戏 VII - 给你一个下标从 0 开始的二进制字符串 s 和两个整数 minJump 和 maxJump 。一开始，你在下标 0 处，且该位置的值一定为 '0' 。当同时满足如下条件时，你可以从下标 i 移动到下标 j 处： * i + minJump <= j <= min(i + maxJump, s.length - 1) 且 * s[j] == '0'. 如果你可以到达 s 的下标 s.length - 1 处，请你返回 true ，否则返回 false 。 示例 1： 输入：s = "011010", minJump = 2, maxJump = 3 输出：true 解释： 第一步，从下标 0 移动到下标 3 。 第二步，从下标 3 移动到下标 5 。 示例 2： 输入：s = "01101110", minJump = 2, maxJump = 3 输出：false 提示： * 2 <= s.length <= 105 * s[i] 要么是 '0' ，要么是 '1' * s[0] == '0' * 1 <= minJump <= maxJump < s.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和滑动窗口来解决这个问题。我们维护一个布尔数组 dp，其中 dp[i] 表示是否可以从起点到达下标 i。通过滑动窗口来更新 dp 数组。

算法步骤:
1. 初始化布尔数组 dp，长度与 s 相同，dp[0] = True。
2. 使用一个变量 left 来记录当前窗口的左边界。
3. 遍历字符串 s，对于每个下标 i：
   - 如果 dp[i] 为 True，则更新窗口的右边界 right。
   - 对于在 [left, right] 范围内的所有下标 j，如果 s[j] == '0'，则 dp[j] = True。
   - 更新 left 边界。
4. 返回 dp[-1]。

关键点:
- 使用滑动窗口来优化时间复杂度，避免重复计算。
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


def can_reach_end(s: str, minJump: int, maxJump: int) -> bool:
    n = len(s)
    if s[n - 1] != '0':
        return False

    dp = [False] * n
    dp[0] = True
    left = 0

    for i in range(1, n):
        if i >= minJump:
            left = max(left, i - maxJump)
            if dp[left]:
                dp[i] = True
            while left < i and not dp[left]:
                left += 1
        if dp[i] and s[i] == '0':
            dp[i] = True
        else:
            dp[i] = False

    return dp[-1]


Solution = create_solution(can_reach_end)