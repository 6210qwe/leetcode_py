# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2708
标题: Find the String with LCP
难度: hard
链接: https://leetcode.cn/problems/find-the-string-with-lcp/
题目类型: 贪心、并查集、数组、字符串、动态规划、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2573. 找出对应 LCP 矩阵的字符串 - 对任一由 n 个小写英文字母组成的字符串 word ，我们可以定义一个 n x n 的矩阵，并满足： * lcp[i][j] 等于子字符串 word[i,...,n-1] 和 word[j,...,n-1] 之间的最长公共前缀的长度。 给你一个 n x n 的矩阵 lcp 。返回与 lcp 对应的、按字典序最小的字符串 word 。如果不存在这样的字符串，则返回空字符串。 对于长度相同的两个字符串 a 和 b ，如果在 a 和 b 不同的第一个位置，字符串 a 的字母在字母表中出现的顺序先于 b 中的对应字母，则认为字符串 a 按字典序比字符串 b 小。例如，"aabd" 在字典上小于 "aaca" ，因为二者不同的第一位置是第三个字母，而 'b' 先于 'c' 出现。 示例 1： 输入：lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]] 输出："abab" 解释：lcp 对应由两个交替字母组成的任意 4 字母字符串，字典序最小的是 "abab" 。 示例 2： 输入：lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]] 输出："aaaa" 解释：lcp 对应只有一个不同字母的任意 4 字母字符串，字典序最小的是 "aaaa" 。 示例 3： 输入：lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]] 输出："" 解释：lcp[3][3] 无法等于 3 ，因为 word[3,...,3] 仅由单个字母组成；因此，不存在答案。 提示： * 1 <= n == lcp.length == lcp[i].length <= 1000 * 0 <= lcp[i][j] <= n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和并查集来构造字典序最小的字符串。

算法步骤:
1. 初始化一个并查集来管理字符的分组。
2. 遍历 LCP 矩阵，根据 LCP 值将字符分组。
3. 检查 LCP 矩阵的有效性，确保每个分组内的字符一致。
4. 构造字典序最小的字符串，使用尽可能小的字符。

关键点:
- 使用并查集来管理字符的分组。
- 确保 LCP 矩阵的有效性。
- 构造字典序最小的字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def findTheString(lcp: List[List[int]]) -> str:
    n = len(lcp)
    
    # 并查集
    parent = list(range(n))
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootX] = rootY
    
    # 根据 LCP 矩阵进行分组
    for i in range(n):
        for j in range(n):
            if lcp[i][j] > 0:
                union(i, j)
    
    # 检查 LCP 矩阵的有效性
    for i in range(n):
        for j in range(n):
            if lcp[i][j] > 0:
                if find(i) != find(j):
                    return ""
                if lcp[i][j] > min(n - i, n - j):
                    return ""
            else:
                if find(i) == find(j):
                    return ""
    
    # 构造字典序最小的字符串
    char_map = {}
    next_char = 'a'
    result = []
    for i in range(n):
        root = find(i)
        if root not in char_map:
            if next_char > 'z':
                return ""
            char_map[root] = next_char
            next_char = chr(ord(next_char) + 1)
        result.append(char_map[root])
    
    return "".join(result)

Solution = create_solution(findTheString)