# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 79
标题: Word Search
难度: medium
链接: https://leetcode.cn/problems/word-search/
题目类型: 深度优先搜索、数组、字符串、回溯、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
79. 单词搜索 - 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 示例 1： [https://assets.leetcode.com/uploads/2020/11/04/word2.jpg] 输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCCED" 输出：true 示例 2： [https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg] 输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "SEE" 输出：true 示例 3： [https://assets.leetcode.com/uploads/2020/10/15/word3.jpg] 输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCB" 输出：false 提示： * m == board.length * n = board[i].length * 1 <= m, n <= 6 * 1 <= word.length <= 15 * board 和 word 仅由大小写英文字母组成 进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯算法，从每个位置开始搜索单词

算法步骤:
1. 遍历矩阵，从每个位置开始搜索
2. 回溯函数backtrack(i, j, index)：
   - 如果index == len(word)，返回True
   - 如果越界或字符不匹配，返回False
   - 标记当前位置为已访问
   - 向四个方向递归搜索
   - 回溯，恢复当前位置
3. 如果找到，返回True；否则返回False

关键点:
- 使用回溯算法搜索所有可能的路径
- 需要标记已访问的位置，避免重复使用
- 时间复杂度O(m*n*4^L)，空间复杂度O(L)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m*n*4^L) - m×n个起始位置，每个位置最多4^L条路径
空间复杂度: O(L) - 递归栈深度为L（单词长度）
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def exist(board: List[List[str]], word: str) -> bool:
    """
    函数式接口 - 回溯算法
    
    实现思路:
    使用回溯算法从矩阵的每个位置开始搜索单词。
    
    Args:
        board: m×n的二维字符网格
        word: 要搜索的单词
        
    Returns:
        如果word存在于网格中返回True，否则返回False
        
    Example:
        >>> exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCCED")
        True
    """
    m, n = len(board), len(board[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def backtrack(i: int, j: int, index: int) -> bool:
        """回溯函数"""
        if index == len(word):
            return True
        
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
            return False
        
        # 标记为已访问
        temp = board[i][j]
        board[i][j] = '#'
        
        # 向四个方向搜索
        for di, dj in directions:
            if backtrack(i + di, j + dj, index + 1):
                return True
        
        # 回溯，恢复当前位置
        board[i][j] = temp
        return False
    
    # 从每个位置开始搜索
    for i in range(m):
        for j in range(n):
            if backtrack(i, j, 0):
                return True
    
    return False


# 自动生成Solution类（无需手动编写）
Solution = create_solution(exist)
