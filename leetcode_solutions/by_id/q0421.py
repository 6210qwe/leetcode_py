# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 421
标题: Maximum XOR of Two Numbers in an Array
难度: medium
链接: https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/
题目类型: 位运算、字典树、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
421. 数组中两个数的最大异或值 - 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。 示例 1： 输入：nums = [3,10,5,25,2,8] 输出：28 解释：最大运算结果是 5 XOR 25 = 28. 示例 2： 输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70] 输出：127 提示： * 1 <= nums.length <= 2 * 105 * 0 <= nums[i] <= 231 - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树（Trie）来存储每个数字的二进制表示，并在遍历过程中找到最大异或值。

算法步骤:
1. 构建一个字典树（Trie），用于存储每个数字的二进制表示。
2. 对于每个数字，将其插入到字典树中。
3. 对于每个数字，通过字典树查找与其异或值最大的另一个数字。
4. 返回找到的最大异或值。

关键点:
- 使用字典树可以高效地存储和查找二进制表示。
- 在查找过程中，尽量选择与当前位不同的路径，以最大化异或值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 其中 n 是数组的长度。每个数字的插入和查找操作都是 O(32) = O(1)。
空间复杂度: O(n) - 字典树的空间复杂度为 O(n * 32) = O(n)。
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
            toggled_bit = 1 - bit
            if toggled_bit in node.children:
                max_xor |= (1 << i)
                node = node.children[toggled_bit]
            else:
                node = node.children[bit]
        return max_xor

def maximum_xor_of_two_numbers_in_an_array(nums: List[int]) -> int:
    """
    函数式接口 - 返回数组中两个数的最大异或值
    
    实现思路:
    使用字典树（Trie）来存储每个数字的二进制表示，并在遍历过程中找到最大异或值。
    
    Args:
        nums: 整数数组
        
    Returns:
        最大异或值
        
    Example:
        >>> maximum_xor_of_two_numbers_in_an_array([3, 10, 5, 25, 2, 8])
        28
    """
    trie = Trie()
    max_xor = 0
    for num in nums:
        trie.insert(num)
        max_xor = max(max_xor, trie.find_max_xor(num))
    return max_xor

# 自动生成Solution类（无需手动编写）
Solution = create_solution(maximum_xor_of_two_numbers_in_an_array)