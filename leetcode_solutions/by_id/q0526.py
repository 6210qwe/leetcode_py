# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 526
标题: Beautiful Arrangement
难度: medium
链接: https://leetcode.cn/problems/beautiful-arrangement/
题目类型: 位运算、数组、动态规划、回溯、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
526. 优美的排列 - 假设有从 1 到 n 的 n 个整数。用这些整数构造一个数组 perm（下标从 1 开始），只要满足下述条件 之一 ，该数组就是一个 优美的排列 ： * perm[i] 能够被 i 整除 * i 能够被 perm[i] 整除 给你一个整数 n ，返回可以构造的 优美排列 的 数量 。 示例 1： 输入：n = 2 输出：2 解释： 第 1 个优美的排列是 [1,2]： - perm[1] = 1 能被 i = 1 整除 - perm[2] = 2 能被 i = 2 整除 第 2 个优美的排列是 [2,1]: - perm[1] = 2 能被 i = 1 整除 - i = 2 能被 perm[2] = 1 整除 示例 2： 输入：n = 1 输出：1 提示： * 1 <= n <= 15
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法生成所有可能的排列，并检查每个排列是否满足优美排列的条件。

算法步骤:
1. 初始化一个计数器 `count` 用于记录优美排列的数量。
2. 使用回溯法生成从 1 到 n 的所有排列。
3. 在生成每个排列的过程中，检查当前排列是否满足优美排列的条件。
4. 如果满足条件，则增加计数器 `count`。
5. 返回计数器 `count` 的值。

关键点:
- 使用回溯法生成排列。
- 在生成排列的过程中进行条件检查，避免生成不必要的排列。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n!)
- 回溯法生成所有排列的时间复杂度为 O(n!)。

空间复杂度: O(n)
- 递归调用栈的空间复杂度为 O(n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def count_arrangement(n: int) -> int:
    def is_beautiful(arrangement: List[int]) -> bool:
        for i in range(1, n + 1):
            if (i % arrangement[i - 1] != 0) and (arrangement[i - 1] % i != 0):
                return False
        return True

    def backtrack(start: int):
        if start == n:
            if is_beautiful(perm):
                nonlocal count
                count += 1
            return
        for i in range(start, n):
            perm[start], perm[i] = perm[i], perm[start]
            backtrack(start + 1)
            perm[start], perm[i] = perm[i], perm[start]

    count = 0
    perm = list(range(1, n + 1))
    backtrack(0)
    return count

Solution = create_solution(count_arrangement)