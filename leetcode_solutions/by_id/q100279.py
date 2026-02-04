# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100279
标题: 字母迷宫
难度: medium
链接: https://leetcode.cn/problems/ju-zhen-zhong-de-lu-jing-lcof/
题目类型: 数组、字符串、回溯、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 129. 字母迷宫 - 字母迷宫游戏初始界面记作 m x n 二维字符串数组 grid，请判断玩家是否能在 grid 中找到目标单词 target。 注意：寻找单词时 必须 按照字母顺序，通过水平或垂直方向相邻的单元格内的字母构成，同时，同一个单元格内的字母 不允许被重复使用 。 [https://assets.leetcode.com/uploads/2020/11/04/word2.jpg] 示例 1： 输入：grid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], target = "ABCCED" 输出：true 示例 2： 输入：grid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], target = "SEE" 输出：true 示例 3： 输入：grid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], target = "ABCB" 输出：false 提示： * m == grid.length * n = grid[i].length * 1 <= m, n <= 6 * 1 <= target.length <= 15 * grid 和 target 仅由大小写英文字母组成 注意：本题与主站 79 题相同：https://leetcode.cn/problems/word-search/ [https://leetcode.cn/problems/word-search/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用深度优先搜索 (DFS) 来遍历矩阵中的每个字符，并检查是否可以形成目标单词。

算法步骤:
1. 遍历矩阵中的每个字符，如果当前字符与目标单词的第一个字符匹配，则从该位置开始进行 DFS。
2. 在 DFS 过程中，检查当前字符是否与目标单词的下一个字符匹配，如果匹配则继续递归搜索相邻的字符。
3. 如果在某个位置找到了目标单词的所有字符，则返回 True。
4. 如果遍历完所有可能的路径仍未找到目标单词，则返回 False。

关键点:
- 使用一个辅助函数来进行 DFS，并传递当前的位置和目标单词的当前索引。
- 使用一个集合来记录已经访问过的单元格，以避免重复使用同一个单元格。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * 4^k)，其中 m 和 n 是矩阵的行数和列数，k 是目标单词的长度。最坏情况下，每个字符都可能有四个方向的递归调用。
空间复杂度: O(k)，递归调用栈的深度最多为 k。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def exist(board: List[List[str]], word: str) -> bool:
    if not board or not board[0]:
        return False
    
    rows, cols = len(board), len(board[0])
    visited = set()
    
    def dfs(r, c, index):
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or board[r][c] != word[index]:
            return False
        visited.add((r, c))
        if (dfs(r + 1, c, index + 1) or
            dfs(r - 1, c, index + 1) or
            dfs(r, c + 1, index + 1) or
            dfs(r, c - 1, index + 1)):
            return True
        visited.remove((r, c))
        return False
    
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False

Solution = create_solution(exist)