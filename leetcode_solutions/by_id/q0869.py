# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 869
标题: Similar String Groups
难度: hard
链接: https://leetcode.cn/problems/similar-string-groups/
题目类型: 深度优先搜索、广度优先搜索、并查集、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
839. 相似字符串组 - 如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。 例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与 "tars"，"rats"，或 "arts" 相似。 总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts" 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。 给你一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。请问 strs 中有多少个相似字符串组？ 示例 1： 输入：strs = ["tars","rats","arts","star"] 输出：2 示例 2： 输入：strs = ["omv","ovm"] 输出：1 提示： * 1 <= strs.length <= 300 * 1 <= strs[i].length <= 300 * strs[i] 只包含小写字母。 * strs 中的所有单词都具有相同的长度，且是彼此的字母异位词。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来管理字符串的相似关系。

算法步骤:
1. 定义一个并查集类 `UnionFind`，用于管理字符串的连通性。
2. 遍历字符串列表，检查每对字符串是否相似。如果相似，则在并查集中将它们合并。
3. 最后，返回并查集中连通分量的数量，即为相似字符串组的数量。

关键点:
- 通过比较字符串的差异来判断相似性。
- 使用并查集高效地管理连通性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * m)，其中 n 是字符串的数量，m 是字符串的长度。需要两两比较字符串。
空间复杂度: O(n)，并查集的空间复杂度为 O(n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1

def is_similar(s1: str, s2: str) -> bool:
    diff = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            diff += 1
        if diff > 2:
            return False
    return True

def solution_function_name(strs: List[str]) -> int:
    """
    函数式接口 - 返回相似字符串组的数量
    """
    n = len(strs)
    uf = UnionFind(n)

    for i in range(n):
        for j in range(i + 1, n):
            if is_similar(strs[i], strs[j]):
                uf.union(i, j)

    return uf.count

Solution = create_solution(solution_function_name)