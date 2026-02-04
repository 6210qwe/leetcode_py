# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2623
标题: Maximum XOR of Two Non-Overlapping Subtrees
难度: hard
链接: https://leetcode.cn/problems/maximum-xor-of-two-non-overlapping-subtrees/
题目类型: 树、深度优先搜索、图、字典树
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2479. 两个不重叠子树的最大异或值 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Trie 树来存储子树的异或值，并在遍历过程中计算最大异或值。

算法步骤:
1. 定义一个 Trie 结构来存储子树的异或值。
2. 使用深度优先搜索 (DFS) 遍历树，计算每个节点为根的子树的异或值，并将其插入到 Trie 中。
3. 在 DFS 过程中，对于每个节点，查询其左子树和右子树的最大异或值，并更新全局最大值。
4. 最后返回全局最大异或值。

关键点:
- 使用 Trie 来高效地存储和查询子树的异或值。
- 通过两次 DFS 分别处理左子树和右子树，确保子树不重叠。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * 30)，其中 n 是树的节点数。每个节点最多需要 30 次操作（因为整数是 32 位）。
空间复杂度: O(n * 30)，Trie 的最坏情况下的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, value: int):
        node = self.root
        for i in range(30, -1, -1):
            bit = (value >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            node.value = max(node.value, value)

    def query_max_xor(self, value: int) -> int:
        node = self.root
        max_xor = 0
        for i in range(30, -1, -1):
            bit = (value >> i) & 1
            toggled_bit = 1 - bit
            if toggled_bit in node.children:
                max_xor |= (1 << i)
                node = node.children[toggled_bit]
            else:
                node = node.children.get(bit, node)
        return max_xor

class Solution:
    def max_xor(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], xor: int) -> int:
            if not node:
                return 0
            current_xor = xor ^ node.val
            left_xor = dfs(node.left, current_xor)
            right_xor = dfs(node.right, current_xor)
            trie.insert(current_xor)
            return max(left_xor, right_xor, current_xor)

        trie = Trie()
        dfs(root, 0)
        return trie.query_max_xor(0)

Solution = create_solution(Solution)