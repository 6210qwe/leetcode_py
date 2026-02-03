# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000370
标题: 黑白翻转棋
难度: medium
链接: https://leetcode.cn/problems/fHi6rV/
题目类型: 广度优先搜索、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 41. 黑白翻转棋 - 在 `n*m` 大小的棋盘中，有黑白两种棋子，黑棋记作字母 `"X"`, 白棋记作字母 `"O"`，空余位置记作 `"."`。当落下的棋子与其他相同颜色的棋子在行、列或对角线完全包围（中间不存在空白位置）另一种颜色的棋子，则可以翻转这些棋子的颜色。 ![1.gif](https://pic.leetcode.cn/1630396029-eTgzpN-6da662e67368466a96d203f67bb6e793.gif){:height=170px}![2.gif](https://pic.leetcode.cn/1630396240-nMvdcc-8e4261afe9f60e05a4f740694b439b6b.gif){:height=170px}![3.gif](https://pic.leetcode.cn/1630396291-kEtzLL-6fcb682daeecb5c3f56eb88b23c81d33.gif){:height=170px} 「力扣挑战赛」黑白翻转棋项目中，将提供给选手一个未形成可翻转棋子的棋盘残局，其状态记作 `chessboard`。若下一步可放置一枚黑棋，请问选手最多能翻转多少枚白棋。 **注意：** - 若翻转白棋成黑棋后，棋盘上仍存在可以翻转的白棋，将可以 **继续** 翻转白棋 - 输入数据保证初始棋盘状态无可以翻转的棋子且存在空余位置 **示例 1：** > 输入：`chessboard = ["....X.","....X.","XOOO..","......","......"]` > > 输出：`3` > > 解释： > 可以选择下在 `[2,4]` 处，能够翻转白方三枚棋子。 **示例 2：** > 输入：`chessboard = [".X.",".O.","XO."]` > > 输出：`2` > > 解释： > 可以选择下在 `[2,2]` 处，能够翻转白方两枚棋子。 ![2126c1d21b1b9a9924c639d449cc6e65.gif](https://pic.leetcode.cn/1626683255-OBtBud-2126c1d21b1b9a9924c639d449cc6e65.gif) **示例 3：** > 输入：`chessboard = [".......",".......",".......","X......",".O.....","..O....","....OOX"]` > > 输出：`4` > > 解释： > 可以选择下在 `[6,3]` 处，能够翻转白方四枚棋子。 ![803f2f04098b6174397d6c696f54d709.gif](https://pic.leetcode.cn/1630393770-Puyked-803f2f04098b6174397d6c696f54d709.gif) **提示：** - `1 <= chessboard.length, chessboard[i].length <= 8` - `chessboard[i]` 仅包含 `"."、"O"` 和 `"X"`
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: BFS模拟翻转棋，尝试所有可能的落子位置

算法步骤:
1. 枚举所有空位置作为落子点
2. 对每个位置，使用BFS模拟翻转过程
3. 统计能翻转的白棋数量
4. 返回最大值

关键点:
- BFS模拟翻转过程
- 8个方向的检查
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n*m*8*max_depth) - n*m为棋盘大小
空间复杂度: O(n*m) - 棋盘空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import deque
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def flip_chess(chessboard: List[str]) -> int:
    """
    函数式接口 - 黑白翻转棋
    
    实现思路:
    BFS模拟翻转棋，尝试所有可能的落子位置。
    
    Args:
        chessboard: 棋盘状态
        
    Returns:
        最多能翻转的白棋数量
        
    Example:
        >>> flip_chess(["....X.","....X.","XOOO..","......","......"])
        3
    """
    m, n = len(chessboard), len(chessboard[0])
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    max_flip = 0
    
    def bfs_flip(start_r: int, start_c: int) -> int:
        """从(start_r, start_c)开始BFS翻转"""
        board = [list(row) for row in chessboard]
        board[start_r][start_c] = 'X'
        queue = deque([(start_r, start_c)])
        flip_count = 0
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                # 找到连续的O
                path = []
                nr, nc = r + dr, c + dc
                
                while 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                    path.append((nr, nc))
                    nr += dr
                    nc += dc
                
                # 如果路径末端是X，则可以翻转
                if path and 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'X':
                    for pr, pc in path:
                        board[pr][pc] = 'X'
                        flip_count += 1
                        queue.append((pr, pc))
        
        return flip_count
    
    # 尝试所有空位置
    for i in range(m):
        for j in range(n):
            if chessboard[i][j] == '.':
                max_flip = max(max_flip, bfs_flip(i, j))
    
    return max_flip


Solution = create_solution(flip_chess)
