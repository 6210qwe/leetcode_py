# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2276
标题: Groups of Strings
难度: hard
链接: https://leetcode.cn/problems/groups-of-strings/
题目类型: 位运算、并查集、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2157. 字符串分组 - 给你一个下标从 0 开始的字符串数组 words 。每个字符串都只包含 小写英文字母 。words 中任意一个子串中，每个字母都至多只出现一次。 如果通过以下操作之一，我们可以从 s1 的字母集合得到 s2 的字母集合，那么我们称这两个字符串为 关联的 ： * 往 s1 的字母集合中添加一个字母。 * 从 s1 的字母集合中删去一个字母。 * 将 s1 中的一个字母替换成另外任意一个字母（也可以替换为这个字母本身）。 数组 words 可以分为一个或者多个无交集的 组 。如果一个字符串与另一个字符串关联，那么它们应当属于同一个组。 注意，你需要确保分好组后，一个组内的任一字符串与其他组的字符串都不关联。可以证明在这个条件下，分组方案是唯一的。 请你返回一个长度为 2 的数组 ans ： * ans[0] 是 words 分组后的 总组数 。 * ans[1] 是字符串数目最多的组所包含的字符串数目。 示例 1： 输入：words = ["a","b","ab","cde"] 输出：[2,3] 解释： - words[0] 可以得到 words[1] （将 'a' 替换为 'b'）和 words[2] （添加 'b'）。所以 words[0] 与 words[1] 和 words[2] 关联。 - words[1] 可以得到 words[0] （将 'b' 替换为 'a'）和 words[2] （添加 'a'）。所以 words[1] 与 words[0] 和 words[2] 关联。 - words[2] 可以得到 words[0] （删去 'b'）和 words[1] （删去 'a'）。所以 words[2] 与 words[0] 和 words[1] 关联。 - words[3] 与 words 中其他字符串都不关联。 所以，words 可以分成 2 个组 ["a","b","ab"] 和 ["cde"] 。最大的组大小为 3 。 示例 2： 输入：words = ["a","ab","abc"] 输出：[1,3] 解释： - words[0] 与 words[1] 关联。 - words[1] 与 words[0] 和 words[2] 关联。 - words[2] 与 words[1] 关联。 由于所有字符串与其他字符串都关联，所以它们全部在同一个组内。 所以最大的组大小为 3 。 提示： * 1 <= words.length <= 2 * 104 * 1 <= words[i].length <= 26 * words[i] 只包含小写英文字母。 * words[i] 中每个字母最多只出现一次。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 使用位运算表示每个字符串的字符集合。
- 使用并查集来管理字符串之间的关联关系。
- 对于每个字符串，生成其所有可能的变换（添加/删除/替换一个字符），并检查这些变换是否存在于输入字符串中。如果存在，则将它们合并到同一个组。

算法步骤:
1. 初始化并查集。
2. 将每个字符串转换为位掩码，并存储在字典中。
3. 遍历每个字符串，生成其所有可能的变换。
4. 如果变换存在于字典中，则将当前字符串和变换字符串合并到同一个组。
5. 统计每个组的大小，并找到最大组的大小。

关键点:
- 使用位掩码表示字符串，便于快速比较和变换。
- 使用并查集高效地管理字符串之间的关联关系。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * 26^2) 其中 n 是字符串的数量，每个字符串最多有 26 个字符，每个字符有 26 种变换。
空间复杂度: O(n) 用于存储并查集和位掩码字典。
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
        self.size = [1] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.count -= 1

    def get_count(self):
        return self.count

    def get_size(self, x):
        return self.size[self.find(x)]

def group_strings(words: List[str]) -> List[int]:
    n = len(words)
    uf = UnionFind(n)
    mask_to_index = {}

    for i, word in enumerate(words):
        mask = 0
        for char in word:
            mask |= 1 << (ord(char) - ord('a'))
        if mask in mask_to_index:
            uf.union(i, mask_to_index[mask])
        else:
            mask_to_index[mask] = i

        for j in range(26):
            # 添加一个字符
            new_mask = mask | (1 << j)
            if new_mask in mask_to_index:
                uf.union(i, mask_to_index[new_mask])

            # 删除一个字符
            if mask & (1 << j):
                new_mask = mask ^ (1 << j)
                if new_mask in mask_to_index:
                    uf.union(i, mask_to_index[new_mask])

            # 替换一个字符
            for k in range(26):
                if mask & (1 << j):
                    new_mask = mask ^ (1 << j) | (1 << k)
                    if new_mask in mask_to_index:
                        uf.union(i, mask_to_index[new_mask])

    max_group_size = 0
    for i in range(n):
        max_group_size = max(max_group_size, uf.get_size(i))

    return [uf.get_count(), max_group_size]

Solution = create_solution(group_strings)