# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000317
标题: 相似字符串组
难度: hard
链接: https://leetcode.cn/problems/H6lPxb/
题目类型: 深度优先搜索、广度优先搜索、并查集、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 117. 相似字符串组 - 如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。 例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与 "tars"，"rats"，或 "arts" 相似。 总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts" 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。 给定一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个 字母异位词 。请问 strs 中有多少个相似字符串组？ 字母异位词（anagram），一种把某个字符串的字母的位置（顺序）加以改换所形成的新词。 示例 1： 输入：strs = ["tars","rats","arts","star"] 输出：2 示例 2： 输入：strs = ["omv","ovm"] 输出：1 提示： * 1 <= strs.length <= 300 * 1 <= strs[i].length <= 300 * strs[i] 只包含小写字母。 * strs 中的所有单词都具有相同的长度，且是彼此的字母异位词。 注意：本题与主站 839 题相同：https://leetcode.cn/problems/similar-string-groups/ [https://leetcode.cn/problems/similar-string-groups/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来合并相似的字符串组。

算法步骤:
1. 初始化并查集。
2. 定义一个函数来检查两个字符串是否相似。
3. 遍历所有字符串对，如果两个字符串相似，则在并查集中合并它们。
4. 最后，返回并查集中的连通分量数。

关键点:
- 使用并查集高效地管理字符串组的合并。
- 通过检查字符差异来判断字符串是否相似。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * m)，其中 n 是字符串的数量，m 是字符串的长度。需要遍历所有字符串对，并检查每对字符串是否相似。
空间复杂度: O(n)，并查集的空间开销。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def are_similar(s1, s2):
    diff = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            diff += 1
        if diff > 2:
            return False
    return diff == 2 or diff == 0

def solution_function_name(strs: List[str]) -> int:
    n = len(strs)
    parent = list(range(n))
    rank = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if are_similar(strs[i], strs[j]):
                union(parent, rank, i, j)

    groups = set()
    for i in range(n):
        groups.add(find(parent, i))

    return len(groups)

Solution = create_solution(solution_function_name)