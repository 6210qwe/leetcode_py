# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1826
标题: Maximum XOR With an Element From Array
难度: hard
链接: https://leetcode.cn/problems/maximum-xor-with-an-element-from-array/
题目类型: 位运算、字典树、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1707. 与数组中元素的最大异或值 - 给你一个由非负整数组成的数组 nums 。另有一个查询数组 queries ，其中 queries[i] = [xi, mi] 。 第 i 个查询的答案是 xi 和任何 nums 数组中不超过 mi 的元素按位异或（XOR）得到的最大值。换句话说，答案是 max(nums[j] XOR xi) ，其中所有 j 均满足 nums[j] <= mi 。如果 nums 中的所有元素都大于 mi，最终答案就是 -1 。 返回一个整数数组 answer 作为查询的答案，其中 answer.length == queries.length 且 answer[i] 是第 i 个查询的答案。 示例 1： 输入：nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]] 输出：[3,3,7] 解释： 1) 0 和 1 是仅有的两个不超过 1 的整数。0 XOR 3 = 3 而 1 XOR 3 = 2 。二者中的更大值是 3 。 2) 1 XOR 2 = 3. 3) 5 XOR 2 = 7. 示例 2： 输入：nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]] 输出：[15,-1,5] 提示： * 1 <= nums.length, queries.length <= 105 * queries[i].length == 2 * 0 <= nums[j], xi, mi <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典树 (Trie) 来存储 nums 数组中的元素，并在查询时通过 Trie 找到最大异或值。

算法步骤:
1. 构建一个 Trie 树来存储 nums 数组中的所有元素。
2. 对每个查询，使用 Trie 树找到不超过 mi 的最大异或值。
3. 如果没有找到符合条件的元素，返回 -1。

关键点:
- 使用 Trie 树可以高效地进行按位操作，从而快速找到最大异或值。
- 在构建 Trie 时，需要将 nums 数组中的元素按位插入 Trie。
- 在查询时，从最高位开始逐位比较，尽量选择与当前位不同的路径以最大化异或值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + q * log(max_num))，其中 n 是 nums 的长度，q 是 queries 的长度，max_num 是 nums 中的最大值。
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
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        node.value = num
    
    def find_max_xor(self, num, max_val):
        node = self.root
        xor_val = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggled_bit = 1 - bit
            if toggled_bit in node.children and node.children[toggled_bit].value is not None and node.children[toggled_bit].value <= max_val:
                xor_val |= (1 << i)
                node = node.children[toggled_bit]
            else:
                node = node.children.get(bit, node)
        return xor_val if node.value is not None and node.value <= max_val else -1

def solution_function_name(nums: List[int], queries: List[List[int]]) -> List[int]:
    """
    函数式接口 - 实现
    """
    trie = Trie()
    for num in nums:
        trie.insert(num)
    
    result = []
    for xi, mi in queries:
        result.append(trie.find_max_xor(xi, mi))
    
    return result

Solution = create_solution(solution_function_name)