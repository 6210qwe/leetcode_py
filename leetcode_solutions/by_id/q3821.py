# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3821
标题: Count Cells in Overlapping Horizontal and Vertical Substrings
难度: medium
链接: https://leetcode.cn/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/
题目类型: 数组、字符串、矩阵、字符串匹配、哈希函数、滚动哈希
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3529. 统计水平子串和垂直子串重叠格子的数目 - 给你一个由字符组成的 m x n 矩阵 grid 和一个字符串 pattern。 水平子串 是从左到右的一段连续字符序列。如果子串到达了某行的末尾，它将换行并从下一行的第一个字符继续。不会 从最后一行回到第一行。 垂直子串 是从上到下的一段连续字符序列。如果子串到达了某列的底部，它将换列并从下一列的第一个字符继续。不会 从最后一列回到第一列。 请统计矩阵中满足以下条件的单元格数量： * 该单元格必须属于 至少 一个等于 pattern 的水平子串，且属于 至少 一个等于 pattern 的垂直子串。 返回满足条件的单元格数量。 示例 1： [https://pic.leetcode.cn/1745660164-PjoTAy-gridtwosubstringsdrawio.png] 输入： grid = [["a","a","c","c"],["b","b","b","c"],["a","a","b","a"],["c","a","a","c"],["a","a","b","a"]], pattern = "abaca" 输出： 1 解释： "abaca" 作为一个水平子串（蓝色）和一个垂直子串（红色）各出现一次，并在一个单元格（紫色）处相交。 示例 2： [https://pic.leetcode.cn/1745660201-bMoajW-gridexample2fixeddrawio.png] 输入： grid = [["c","a","a","a"],["a","a","b","a"],["b","b","a","a"],["a","a","b","a"]], pattern = "aba" 输出： 4 解释： 上述被标记的单元格都同时属于至少一个 "aba" 的水平和垂直子串。 示例 3： 输入： grid = [["a"]], pattern = "a" 输出： 1 提示： * m == grid.length * n == grid[i].length * 1 <= m, n <= 1000 * 1 <= m * n <= 105 * 1 <= pattern.length <= m * n * grid 和 pattern 仅由小写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滚动哈希来快速查找水平和垂直子串。

算法步骤:
1. 计算模式字符串的滚动哈希值。
2. 对每一行进行滚动哈希，记录所有匹配的起始位置。
3. 对每一列进行滚动哈希，记录所有匹配的起始位置。
4. 找出同时在水平和垂直匹配中的单元格。

关键点:
- 使用滚动哈希可以高效地查找子串。
- 通过预计算模式字符串的哈希值，可以快速比较子串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)
空间复杂度: O(m + n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def compute_rolling_hash(s: str, base: int, mod: int) -> List[int]:
    hash_values = [0] * (len(s) + 1)
    power = 1
    for i in range(len(s)):
        hash_values[i + 1] = (hash_values[i] + (ord(s[i]) - ord('a') + 1) * power) % mod
        power = (power * base) % mod
    return hash_values

def find_substring_starts(text: str, pattern: str, base: int, mod: int) -> List[int]:
    text_hash = compute_rolling_hash(text, base, mod)
    pattern_hash = compute_rolling_hash(pattern, base, mod)[-1]
    
    starts = []
    pattern_len = len(pattern)
    for i in range(len(text) - pattern_len + 1):
        if (text_hash[i + pattern_len] - text_hash[i] + mod) % mod == pattern_hash:
            starts.append(i)
    return starts

def count_overlap_cells(grid: List[List[str]], pattern: str) -> int:
    m, n = len(grid), len(grid[0])
    base, mod = 257, 10**9 + 7
    
    # 将每行和每列转换为字符串
    rows = [''.join(row) for row in grid]
    cols = [''.join(grid[i][j] for i in range(m)) for j in range(n)]
    
    # 查找水平和垂直匹配的起始位置
    row_matches = [find_substring_starts(row, pattern, base, mod) for row in rows]
    col_matches = [find_substring_starts(col, pattern, base, mod) for col in cols]
    
    # 记录每个单元格是否在水平和垂直匹配中
    horizontal_matches = set()
    vertical_matches = set()
    
    for i, matches in enumerate(row_matches):
        for start in matches:
            for j in range(start, start + len(pattern)):
                horizontal_matches.add((i, j))
    
    for j, matches in enumerate(col_matches):
        for start in matches:
            for i in range(start, start + len(pattern)):
                vertical_matches.add((i, j))
    
    # 计算重叠单元格的数量
    overlap_count = len(horizontal_matches & vertical_matches)
    return overlap_count

Solution = create_solution(count_overlap_cells)