# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3929
标题: Subarrays with XOR at Least K
难度: hard
链接: https://leetcode.cn/problems/subarrays-with-xor-at-least-k/
题目类型: 位运算、字典树、数组、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3632. 异或至少为 K 的子数组数目 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀异或和与字典树（Trie）来高效查找满足条件的子数组。

算法步骤:
1. 计算前缀异或和。
2. 使用 Trie 树存储前缀异或和。
3. 对于每个前缀异或和，使用 Trie 树查找满足条件的子数组。

关键点:
- 使用 Trie 树可以高效地查找满足条件的前缀异或和。
- 通过前缀异或和的性质，可以快速计算子数组的异或值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * log(max_num))，其中 n 是数组长度，max_num 是数组中的最大值。
空间复杂度: O(n * log(max_num))，用于存储 Trie 树。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num: int) -> None:
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            node.count += 1

    def get_count(self, num: int, k: int) -> int:
        node = self.root
        count = 0
        for i in range(31, -1, -1):
            if not node:
                break
            bit = (num >> i) & 1
            target_bit = (k >> i) & 1
            if target_bit == 1:
                if bit in node.children:
                    count += node.children[bit].count
                node = node.children[1 - bit]
            else:
                node = node.children[bit]
        return count

def subarrays_with_xor_at_least_k(nums: List[int], k: int) -> int:
    """
    函数式接口 - 返回异或至少为 K 的子数组数目
    """
    prefix_xor = 0
    trie = Trie()
    trie.insert(0)
    count = 0
    for num in nums:
        prefix_xor ^= num
        count += trie.get_count(prefix_xor, k)
        trie.insert(prefix_xor)
    return count

Solution = create_solution(subarrays_with_xor_at_least_k)