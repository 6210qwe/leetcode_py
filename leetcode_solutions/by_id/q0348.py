# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 348
标题: Design Tic-Tac-Toe
难度: medium
链接: https://leetcode.cn/problems/design-tic-tac-toe/
题目类型: 设计、数组、哈希表、矩阵、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
348. 设计井字棋 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 维护行、列、对角线的计数

算法步骤:
1. 维护每行、每列、两条对角线的计数
2. 玩家1加1，玩家2减1
3. 如果某行/列/对角线的绝对值等于n，该玩家获胜

关键点:
- 维护计数
- 时间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - move操作O(1)
空间复杂度: O(n) - 计数数组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def tic_tac_toe_class(n: int):
    """
    函数式接口 - 设计井字棋
    
    实现思路:
    维护行、列、对角线的计数。
    
    Args:
        n: 棋盘大小
        
    Returns:
        TicTacToe类
        
    Example:
        >>> game = tic_tac_toe_class(3)
        >>> game.move(0, 0, 1)
        0
    """
    class TicTacToe:
        def __init__(self, n: int):
            self.n = n
            self.rows = [0] * n
            self.cols = [0] * n
            self.diag = 0  # 主对角线
            self.anti_diag = 0  # 副对角线
        
        def move(self, row: int, col: int, player: int) -> int:
            """移动"""
            # 玩家1加1，玩家2减1
            value = 1 if player == 1 else -1
            
            self.rows[row] += value
            self.cols[col] += value
            
            if row == col:
                self.diag += value
            if row + col == self.n - 1:
                self.anti_diag += value
            
            # 检查是否获胜
            if abs(self.rows[row]) == self.n or \
               abs(self.cols[col]) == self.n or \
               abs(self.diag) == self.n or \
               abs(self.anti_diag) == self.n:
                return player
            
            return 0
    
    return TicTacToe(n)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(tic_tac_toe_class)
