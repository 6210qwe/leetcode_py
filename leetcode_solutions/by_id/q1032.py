# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1032
标题: Satisfiability of Equality Equations
难度: medium
链接: https://leetcode.cn/problems/satisfiability-of-equality-equations/
题目类型: 并查集、图、数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
990. 等式方程的可满足性 - 给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。 只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 示例 1： 输入：["a==b","b!=a"] 输出：false 解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。 示例 2： 输入：["b==a","a==b"] 输出：true 解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。 示例 3： 输入：["a==b","b==c","a==c"] 输出：true 示例 4： 输入：["a==b","b!=c","c==a"] 输出：false 示例 5： 输入：["c==c","b==d","x!=z"] 输出：true 提示： 1. 1 <= equations.length <= 500 2. equations[i].length == 4 3. equations[i][0] 和 equations[i][3] 是小写字母 4. equations[i][1] 要么是 '='，要么是 '!' 5. equations[i][2] 是 '='
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集来处理等式和不等式的关系。

算法步骤:
1. 初始化并查集，用于存储变量之间的连通性。
2. 遍历所有等式，将相等的变量进行合并。
3. 遍历所有不等式，检查不等式的两个变量是否在同一个集合中，如果是则返回 False。
4. 如果所有不等式都满足，则返回 True。

关键点:
- 使用并查集来高效地处理变量之间的连通性。
- 先处理等式，再处理不等式，确保在处理不等式时，等式已经完全处理完毕。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(nα(n))，其中 n 是 equations 的长度，α 是反阿克曼函数。
空间复杂度: O(1)，并查集的空间复杂度是常数级别的。
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

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y


def solution_function_name(equations: List[str]) -> bool:
    """
    函数式接口 - 判断给定的等式方程是否可满足
    """
    uf = UnionFind()
    
    # 处理等式
    for eq in equations:
        if eq[1] == "=":
            x, y = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a')
            uf.union(x, y)
    
    # 处理不等式
    for eq in equations:
        if eq[1] == "!":
            x, y = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a')
            if uf.find(x) == uf.find(y):
                return False
    
    return True


Solution = create_solution(solution_function_name)