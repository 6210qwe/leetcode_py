# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3329
标题: Find the Length of the Longest Common Prefix
难度: medium
链接: https://leetcode.cn/problems/find-the-length-of-the-longest-common-prefix/
题目类型: 字典树、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3043. 最长公共前缀的长度 - 给你两个 正整数 数组 arr1 和 arr2 。 正整数的 前缀 是其 最左边 的一位或多位数字组成的整数。例如，123 是整数 12345 的前缀，而 234 不是 。 设若整数 c 是整数 a 和 b 的 公共前缀 ，那么 c 需要同时是 a 和 b 的前缀。例如，5655359 和 56554 有公共前缀 565 和 5655，而 1223 和 43456 没有 公共前缀。 你需要找出属于 arr1 的整数 x 和属于 arr2 的整数 y 组成的所有数对 (x, y) 之中最长的公共前缀的长度。 返回所有数对之中最长公共前缀的长度。如果它们之间不存在公共前缀，则返回 0 。 示例 1： 输入：arr1 = [1,10,100], arr2 = [1000] 输出：3 解释：存在 3 个数对 (arr1[i], arr2[j]) ： - (1, 1000) 的最长公共前缀是 1 。 - (10, 1000) 的最长公共前缀是 10 。 - (100, 1000) 的最长公共前缀是 100 。 最长的公共前缀是 100 ，长度为 3 。 示例 2： 输入：arr1 = [1,2,3], arr2 = [4,4,4] 输出：0 解释：任何数对 (arr1[i], arr2[j]) 之中都不存在公共前缀，因此返回 0 。 请注意，同一个数组内元素之间的公共前缀不在考虑范围内。 提示： * 1 <= arr1.length, arr2.length <= 5 * 104 * 1 <= arr1[i], arr2[i] <= 108
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储 arr1 中每个数字的前缀，并在遍历 arr2 时查找最长公共前缀。

算法步骤:
1. 构建一个 Trie 树，将 arr1 中每个数字的每一位插入到 Trie 中。
2. 遍历 arr2 中的每个数字，使用 Trie 查找与 arr1 中数字的最长公共前缀。
3. 记录并更新最长公共前缀的长度。

关键点:
- 使用 Trie 来高效地存储和查找前缀。
- 在 Trie 中记录每个节点的深度，以便计算前缀长度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 arr1 的长度，m 是 arr2 的长度。每个数字的平均长度为常数。
空间复杂度: O(n * L)，其中 n 是 arr1 的长度，L 是数字的平均长度。Trie 树的空间复杂度取决于 arr1 中数字的总长度。
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
        self.is_end = False
        self.depth = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num: int):
        node = self.root
        for digit in str(num):
            if digit not in node.children:
                node.children[digit] = TrieNode()
            node = node.children[digit]
            node.depth += 1
        node.is_end = True

    def longest_common_prefix(self, num: int) -> int:
        node = self.root
        prefix_length = 0
        for digit in str(num):
            if digit in node.children:
                node = node.children[digit]
                prefix_length += 1
            else:
                break
        return prefix_length


def find_longest_common_prefix(arr1: List[int], arr2: List[int]) -> int:
    trie = Trie()
    for num in arr1:
        trie.insert(num)

    max_prefix_length = 0
    for num in arr2:
        prefix_length = trie.longest_common_prefix(num)
        max_prefix_length = max(max_prefix_length, prefix_length)

    return max_prefix_length


Solution = create_solution(find_longest_common_prefix)