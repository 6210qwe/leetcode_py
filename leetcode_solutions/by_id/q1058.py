# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1058
标题: Lexicographically Smallest Equivalent String
难度: medium
链接: https://leetcode.cn/problems/lexicographically-smallest-equivalent-string/
题目类型: 并查集、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1061. 按字典序排列最小的等效字符串 - 给出长度相同的两个字符串s1 和 s2 ，还有一个字符串 baseStr 。 其中 s1[i] 和 s2[i] 是一组等价字符。 * 举个例子，如果 s1 = "abc" 且 s2 = "cde"，那么就有 'a' == 'c', 'b' == 'd', 'c' == 'e'。 等价字符遵循任何等价关系的一般规则： * 自反性 ：'a' == 'a' * 对称性 ：'a' == 'b' 则必定有 'b' == 'a' * 传递性 ：'a' == 'b' 且 'b' == 'c' 就表明 'a' == 'c' 例如， s1 = "abc" 和 s2 = "cde" 的等价信息和之前的例子一样，那么 baseStr = "eed" , "acd" 或 "aab"，这三个字符串都是等价的，而 "aab" 是 baseStr 的按字典序最小的等价字符串 利用 s1 和 s2 的等价信息，找出并返回 baseStr 的按字典序排列最小的等价字符串。 示例 1： 输入：s1 = "parker", s2 = "morris", baseStr = "parser" 输出："makkek" 解释：根据 A 和 B 中的等价信息，我们可以将这些字符分为 [m,p], [a,o], [k,r,s], [e,i] 共 4 组。每组中的字符都是等价的，并按字典序排列。所以答案是 "makkek"。 示例 2： 输入：s1 = "hello", s2 = "world", baseStr = "hold" 输出："hdld" 解释：根据 A 和 B 中的等价信息，我们可以将这些字符分为 [h,w], [d,e,o], [l,r] 共 3 组。所以只有 S 中的第二个字符 'o' 变成 'd'，最后答案为 "hdld"。 示例 3： 输入：s1 = "leetcode", s2 = "programs", baseStr = "sourcecode" 输出："aauaaaaada" 解释：我们可以把 A 和 B 中的等价字符分为 [a,o,e,r,s,c], [l,p], [g,t] 和 [d,m] 共 4 组，因此 S 中除了 'u' 和 'd' 之外的所有字母都转化成了 'a'，最后答案为 "aauaaaaada"。 提示： * 1 <= s1.length, s2.length, baseStr <= 1000 * s1.length == s2.length * 字符串s1, s2, and baseStr 仅由从 'a' 到 'z' 的小写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来处理等价字符的合并和查找。

算法步骤:
1. 初始化并查集，每个字符初始时都是自己的根。
2. 遍历 s1 和 s2，将每对等价字符进行合并。
3. 对于 baseStr 中的每个字符，找到其在并查集中的根，并用根字符替换。
4. 返回处理后的 baseStr。

关键点:
- 使用并查集来高效处理等价字符的合并和查找。
- 在合并时，总是将较小的字符作为根，以保证字典序最小。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 s1 和 s2 的长度，m 是 baseStr 的长度。初始化并查集的时间复杂度是 O(1)，合并操作的时间复杂度接近 O(1)（使用路径压缩和按秩合并），查找操作的时间复杂度也是接近 O(1)。
空间复杂度: O(1)，并查集的空间复杂度是常数级别的，因为字符集是固定的 26 个小写字母。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class UnionFind:
    def __init__(self):
        self.parent = list(range(26))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if root_x < root_y:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y


def smallest_equivalent_string(s1: str, s2: str, base_str: str) -> str:
    uf = UnionFind()
    
    for char1, char2 in zip(s1, s2):
        uf.union(ord(char1) - ord('a'), ord(char2) - ord('a'))
    
    result = []
    for char in base_str:
        root = uf.find(ord(char) - ord('a'))
        result.append(chr(root + ord('a')))
    
    return ''.join(result)


Solution = create_solution(smallest_equivalent_string)