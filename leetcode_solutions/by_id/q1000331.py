# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000331
标题: 数组中两个数的最大异或值
难度: medium
链接: https://leetcode.cn/problems/ms70jA/
题目类型: 位运算、字典树、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 067. 数组中两个数的最大异或值 - 给定一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。 示例 1： 输入：nums = [3,10,5,25,2,8] 输出：28 解释：最大运算结果是 5 XOR 25 = 28. 示例 2： 输入：nums = [0] 输出：0 示例 3： 输入：nums = [2,4] 输出：6 示例 4： 输入：nums = [8,10,2] 输出：10 示例 5： 输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70] 输出：127 提示： * 1 <= nums.length <= 2 * 105 * 0 <= nums[i] <= 231 - 1 进阶：你可以在 O(n) 的时间解决这个问题吗？ 注意：本题与主站 421 题相同： https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/ [https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储二进制表示的数字，并在查询时尽量选择与当前位不同的路径以最大化异或值。

算法步骤:
1. 构建一个字典树，将每个数字的二进制表示插入到字典树中。
2. 对于每个数字，从字典树中查找与其异或值最大的另一个数字。
3. 在查找过程中，尽量选择与当前位不同的路径以最大化异或值。

关键点:
- 使用字典树存储二进制表示的数字。
- 在查找过程中，优先选择与当前位不同的路径。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
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


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num: int):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def find_max_xor(self, num: int) -> int:
        node = self.root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggle_bit = 1 - bit
            if toggle_bit in node.children:
                max_xor |= (1 << i)
                node = node.children[toggle_bit]
            else:
                node = node.children[bit]
        return max_xor


def findMaximumXOR(nums: List[int]) -> int:
    """
    函数式接口 - 返回数组中两个数的最大异或值
    """
    trie = Trie()
    for num in nums:
        trie.insert(num)

    max_xor = 0
    for num in nums:
        max_xor = max(max_xor, trie.find_max_xor(num))
    return max_xor


Solution = create_solution(findMaximumXOR)