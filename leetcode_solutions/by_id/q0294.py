# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 294
标题: Flip Game II
难度: medium
链接: https://leetcode.cn/problems/flip-game-ii/
题目类型: 记忆化搜索、数学、动态规划、回溯、博弈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
294. 翻转游戏 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 记忆化搜索，判断先手是否能获胜

算法步骤:
1. 枚举所有可能的操作
2. 如果存在一个操作使得对手必败，则先手必胜
3. 使用记忆化优化

关键点:
- 记忆化搜索
- 博弈论
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - n为字符串长度
空间复杂度: O(n) - 记忆化空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from functools import lru_cache
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_win(current_state: str) -> bool:
    """
    函数式接口 - 翻转游戏 II
    
    实现思路:
    记忆化搜索：判断先手是否能获胜。
    
    Args:
        current_state: 当前状态字符串
        
    Returns:
        先手是否能获胜
        
    Example:
        >>> can_win("++++")
        True
    """
    @lru_cache(maxsize=None)
    def dfs(state: str) -> bool:
        """记忆化搜索"""
        for i in range(len(state) - 1):
            if state[i:i+2] == "++":
                new_state = state[:i] + "--" + state[i+2:]
                # 如果对手不能获胜，则先手获胜
                if not dfs(new_state):
                    return True
        return False
    
    return dfs(current_state)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(can_win)
