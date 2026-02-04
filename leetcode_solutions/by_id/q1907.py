# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1907
标题: Count Pairs With XOR in a Range
难度: hard
链接: https://leetcode.cn/problems/count-pairs-with-xor-in-a-range/
题目类型: 位运算、字典树、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1803. 统计异或值在范围内的数对有多少 - 给你一个整数数组 nums （下标 从 0 开始 计数）以及两个整数：low 和 high ，请返回 漂亮数对 的数目。 漂亮数对 是一个形如 (i, j) 的数对，其中 0 <= i < j < nums.length 且 low <= (nums[i] XOR nums[j]) <= high 。 示例 1： 输入：nums = [1,4,2,7], low = 2, high = 6 输出：6 解释：所有漂亮数对 (i, j) 列出如下： - (0, 1): nums[0] XOR nums[1] = 5 - (0, 2): nums[0] XOR nums[2] = 3 - (0, 3): nums[0] XOR nums[3] = 6 - (1, 2): nums[1] XOR nums[2] = 6 - (1, 3): nums[1] XOR nums[3] = 3 - (2, 3): nums[2] XOR nums[3] = 5 示例 2： 输入：nums = [9,8,4,2,1], low = 5, high = 14 输出：8 解释：所有漂亮数对 (i, j) 列出如下： ​​​​​ - (0, 2): nums[0] XOR nums[2] = 13 - (0, 3): nums[0] XOR nums[3] = 11 - (0, 4): nums[0] XOR nums[4] = 8 - (1, 2): nums[1] XOR nums[2] = 12 - (1, 3): nums[1] XOR nums[3] = 10 - (1, 4): nums[1] XOR nums[4] = 9 - (2, 3): nums[2] XOR nums[3] = 6 - (2, 4): nums[2] XOR nums[4] = 5 提示： * 1 <= nums.length <= 2 * 104 * 1 <= nums[i] <= 2 * 104 * 1 <= low <= high <= 2 * 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来高效地统计满足条件的数对。

算法步骤:
1. 构建一个字典树（Trie），用于存储二进制表示的数字。
2. 对于每个数字，将其插入字典树中，并计算当前数字与其他已插入数字的异或结果。
3. 使用字典树的查询功能，统计满足条件的数对数量。

关键点:
- 使用字典树可以高效地进行前缀匹配和异或操作。
- 通过逐位比较，可以在 O(1) 时间内判断是否满足条件。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * log(max(nums)))，其中 n 是 nums 的长度，log(max(nums)) 是数字的二进制位数。
空间复杂度: O(n * log(max(nums)))，字典树的空间复杂度。
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
    def __init__(self, max_bit=15):
        self.root = TrieNode()
        self.max_bit = max_bit

    def insert(self, num):
        node = self.root
        for i in range(self.max_bit, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            node.count += 1

    def query(self, num, limit):
        node = self.root
        result = 0
        for i in range(self.max_bit, -1, -1):
            if not node:
                break
            bit = (num >> i) & 1
            target_bit = (limit >> i) & 1
            if target_bit == 1:
                if bit in node.children:
                    result += node.children[bit].count
                node = node.children[1 - bit]
            else:
                node = node.children[bit]
        return result


def count_pairs_with_xor_in_range(nums: List[int], low: int, high: int) -> int:
    trie = Trie()
    result = 0
    for num in nums:
        result += trie.query(num, high + 1) - trie.query(num, low)
        trie.insert(num)
    return result


Solution = create_solution(count_pairs_with_xor_in_range)