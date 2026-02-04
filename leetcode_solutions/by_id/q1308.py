# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1308
标题: Smallest String With Swaps
难度: medium
链接: https://leetcode.cn/problems/smallest-string-with-swaps/
题目类型: 深度优先搜索、广度优先搜索、并查集、数组、哈希表、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1202. 交换字符串中的元素 - 给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。 你可以 任意多次交换 在 pairs 中任意一对索引处的字符。 返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。 示例 1: 输入：s = "dcab", pairs = [[0,3],[1,2]] 输出："bacd" 解释： 交换 s[0] 和 s[3], s = "bcad" 交换 s[1] 和 s[2], s = "bacd" 示例 2： 输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]] 输出："abcd" 解释： 交换 s[0] 和 s[3], s = "bcad" 交换 s[0] 和 s[2], s = "acbd" 交换 s[1] 和 s[2], s = "abcd" 示例 3： 输入：s = "cba", pairs = [[0,1],[1,2]] 输出："abc" 解释： 交换 s[0] 和 s[1], s = "bca" 交换 s[1] 和 s[2], s = "bac" 交换 s[0] 和 s[1], s = "abc" 提示： * 1 <= s.length <= 10^5 * 0 <= pairs.length <= 10^5 * 0 <= pairs[i][0], pairs[i][1] < s.length * s 中只含有小写英文字母
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集将可以互相交换的索引归为一组，然后对每组内的字符进行排序，最后将排序后的字符放回原位置。

算法步骤:
1. 初始化并查集。
2. 遍历 pairs 数组，将每对索引进行合并。
3. 将每个索引与其所在的连通分量进行映射。
4. 对每个连通分量内的字符进行排序。
5. 构建最终结果字符串。

关键点:
- 使用并查集来管理连通分量。
- 对每个连通分量内的字符进行排序，确保字典序最小。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n + m α(n))，其中 n 是字符串长度，m 是 pairs 的长度，α 是反阿克曼函数。
空间复杂度: O(n)，用于存储并查集和连通分量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def smallestStringWithSwaps(s: str, pairs: List[List[int]]) -> str:
    """
    函数式接口 - 实现最优解法
    """
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x, y):
            rootX = self.find(x)
            rootY = self.find(y)
            if rootX != rootY:
                self.parent[rootX] = rootY
    
    n = len(s)
    uf = UnionFind(n)
    
    for a, b in pairs:
        uf.union(a, b)
    
    # 将每个索引与其所在的连通分量进行映射
    groups = {}
    for i in range(n):
        root = uf.find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)
    
    # 对每个连通分量内的字符进行排序
    result = list(s)
    for indices in groups.values():
        chars = [s[i] for i in indices]
        chars.sort()
        for i, char in zip(indices, chars):
            result[i] = char
    
    return ''.join(result)


Solution = create_solution(smallestStringWithSwaps)