# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 723
标题: Candy Crush
难度: medium
链接: https://leetcode.cn/problems/candy-crush/
题目类型: 数组、双指针、矩阵、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
723. 粉碎糖果 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归方法不断粉碎糖果，直到没有更多的糖果可以被粉碎。

算法步骤:
1. 检查每一行和每一列，标记需要粉碎的糖果。
2. 如果有糖果被标记，则粉碎这些糖果，并将上方的糖果下移填补空位。
3. 重复上述步骤，直到没有更多的糖果可以被粉碎。

关键点:
- 使用一个辅助函数来检查并标记需要粉碎的糖果。
- 使用另一个辅助函数来粉碎糖果并将上方的糖果下移。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O((R * C) * (R + C))，其中 R 是行数，C 是列数。最坏情况下，每次粉碎操作都需要遍历整个矩阵。
空间复杂度: O(1)，除了输入矩阵外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def candyCrush(board: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 实现最优解法
    """
    R, C = len(board), len(board[0])
    todo = False

    # 标记需要粉碎的糖果
    for r in range(R):
        for c in range(C - 2):
            if abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c + 2]) != 0:
                board[r][c] = board[r][c + 1] = board[r][c + 2] = -abs(board[r][c])
                todo = True

    for r in range(R - 2):
        for c in range(C):
            if abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) != 0:
                board[r][c] = board[r + 1][c] = board[r + 2][c] = -abs(board[r][c])
                todo = True

    # 粉碎糖果并将上方的糖果下移
    if todo:
        for c in range(C):
            wr = R - 1
            for r in range(R - 1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0

    return board if not todo else candyCrush(board)


Solution = create_solution(candyCrush)