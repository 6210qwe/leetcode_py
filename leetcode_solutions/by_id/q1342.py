# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1342
标题: Queens That Can Attack the King
难度: medium
链接: https://leetcode.cn/problems/queens-that-can-attack-the-king/
题目类型: 数组、矩阵、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1222. 可以攻击国王的皇后 - 在一个 下标从 0 开始 的 8 x 8 棋盘上，可能有多个黑皇后和一个白国王。 给你一个二维整数数组 queens，其中 queens[i] = [xQueeni, yQueeni] 表示第 i 个黑皇后在棋盘上的位置。还给你一个长度为 2 的整数数组 king，其中 king = [xKing, yKing] 表示白国王的位置。 返回 能够直接攻击国王的黑皇后的坐标。你可以以 任何顺序 返回答案。 示例 1： [https://pic.leetcode.cn/1703052515-HqjAJq-chess1.jpg] 输入：queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0] 输出：[[0,1],[1,0],[3,3]] 解释：上面的图示显示了三个可以直接攻击国王的皇后和三个不能攻击国王的皇后（用红色虚线标记）。 示例 2： [https://pic.leetcode.cn/1703052660-bPPflt-chess2.jpg] 输入：queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3] 输出：[[2,2],[3,4],[4,4]] 解释：上面的图示显示了三个能够直接攻击国王的黑皇后和三个不能攻击国王的黑皇后（用红色虚线标记）。 提示： * 1 <= queens.length < 64 * queens[i].length == king.length == 2 * 0 <= xQueeni, yQueeni, xKing, yKing < 8 * 所有给定的位置都是 唯一 的。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个方向上最近的皇后，然后检查这些皇后是否能攻击到国王。

算法步骤:
1. 初始化一个哈希表 `directions`，记录每个方向上最近的皇后。
2. 遍历所有皇后，更新哈希表中每个方向上最近的皇后。
3. 遍历哈希表，检查每个方向上最近的皇后是否能攻击到国王，如果可以则加入结果列表。

关键点:
- 使用哈希表记录每个方向上最近的皇后，避免重复计算。
- 检查每个方向上最近的皇后是否能攻击到国王。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是皇后数量。我们只需要遍历一次皇后数组。
空间复杂度: O(1)，哈希表的大小是固定的，最多有 8 个方向。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(queens: List[List[int]], king: List[int]) -> List[List[int]]:
    """
    函数式接口 - 返回能够直接攻击国王的黑皇后的坐标
    """
    # 定义八个方向
    directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    
    # 初始化哈希表，记录每个方向上最近的皇后
    closest_queens = {d: None for d in directions}
    
    # 遍历所有皇后，更新哈希表中每个方向上最近的皇后
    for queen in queens:
        for d in directions:
            if (queen[0] - king[0], queen[1] - king[1]) == d:
                if closest_queens[d] is None or abs(queen[0] - king[0]) + abs(queen[1] - king[1]) < abs(closest_queens[d][0] - king[0]) + abs(closest_queens[d][1] - king[1]):
                    closest_queens[d] = queen
    
    # 检查每个方向上最近的皇后是否能攻击到国王
    result = [queen for queen in closest_queens.values() if queen is not None]
    
    return result


Solution = create_solution(solution_function_name)