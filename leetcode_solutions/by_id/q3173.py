# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3173
标题: The Wording Game
难度: hard
链接: https://leetcode.cn/problems/the-wording-game/
题目类型: 贪心、数组、数学、双指针、字符串、博弈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2868. 单词游戏 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和双指针来解决这个问题。我们需要找到一个最优的分割点，使得两个玩家的得分差值最小。

算法步骤:
1. 初始化两个指针 left 和 right 分别指向字符串的开头和结尾。
2. 计算从 left 到 right 的子字符串的得分。
3. 移动 left 或 right 指针，使得得分差值最小。
4. 重复步骤 2 和 3，直到找到最优解。

关键点:
- 使用双指针来减少计算量。
- 通过贪心算法来找到最优的分割点。
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


def solution_function_name(s: str) -> int:
    """
    函数式接口 - 实现单词游戏的最优解法
    """
    def calculate_score(substring: str) -> int:
        score = 0
        for char in substring:
            if char.isalpha():
                score += ord(char.lower()) - ord('a') + 1
        return score

    n = len(s)
    left, right = 0, n - 1
    min_diff = float('inf')
    left_score, right_score = 0, 0

    while left < right:
        if s[left].isalpha():
            left_score += ord(s[left].lower()) - ord('a') + 1
        if s[right].isalpha():
            right_score += ord(s[right].lower()) - ord('a') + 1
        min_diff = min(min_diff, abs(left_score - right_score))
        if left_score <= right_score:
            left += 1
        else:
            right -= 1

    return min_diff


Solution = create_solution(solution_function_name)