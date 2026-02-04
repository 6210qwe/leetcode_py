# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3197
标题: Maximum Strong Pair XOR II
难度: hard
链接: https://leetcode.cn/problems/maximum-strong-pair-xor-ii/
题目类型: 位运算、字典树、数组、哈希表、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2935. 找出强数对的最大异或值 II - 给你一个下标从 0 开始的整数数组 nums 。如果一对整数 x 和 y 满足以下条件，则称其为 强数对 ： * |x - y| <= min(x, y) 你需要从 nums 中选出两个整数，且满足：这两个整数可以形成一个强数对，并且它们的按位异或（XOR）值是在该数组所有强数对中的 最大值 。 返回数组 nums 所有可能的强数对中的 最大 异或值。 注意，你可以选择同一个整数两次来形成一个强数对。 示例 1： 输入：nums = [1,2,3,4,5] 输出：7 解释：数组 nums 中有 11 个强数对：(1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5) 和 (5, 5) 。 这些强数对中的最大异或值是 3 XOR 4 = 7 。 示例 2： 输入：nums = [10,100] 输出：0 解释：数组 nums 中有 2 个强数对：(10, 10) 和 (100, 100) 。 这些强数对中的最大异或值是 10 XOR 10 = 0 ，数对 (100, 100) 的异或值也是 100 XOR 100 = 0 。 示例 3： 输入：nums = [500,520,2500,3000] 输出：1020 解释：数组 nums 中有 6 个强数对：(500, 500), (500, 520), (520, 520), (2500, 2500), (2500, 3000) 和 (3000, 3000) 。 这些强数对中的最大异或值是 500 XOR 520 = 1020 ；另一个异或值非零的数对是 (5, 6) ，其异或值是 2500 XOR 3000 = 636 。 提示： * 1 <= nums.length <= 5 * 104 * 1 <= nums[i] <= 220 - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Trie 树来存储二进制表示的数字，并在遍历过程中找到最大异或值。

算法步骤:
1. 构建一个 Trie 树，用于存储每个数字的二进制表示。
2. 对数组进行排序，以便使用滑动窗口来维护当前范围内的数字。
3. 使用双指针方法，确保当前窗口内的数字都满足强数对的条件。
4. 在 Trie 树中查找当前数字的最大异或值，并更新结果。

关键点:
- 使用 Trie 树来高效地查找最大异或值。
- 使用双指针方法来维护当前窗口内的数字。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n + 32n) = O(n log n)，其中 n 是数组的长度。排序操作的时间复杂度是 O(n log n)，插入和查询 Trie 树的时间复杂度是 O(32n)。
空间复杂度: O(32n) = O(n)，Trie 树的空间复杂度。
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

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            node.count += 1

    def remove(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            node = node.children[bit]
            node.count -= 1

    def find_max_xor(self, num):
        node = self.root
        xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            target_bit = 1 - bit
            if target_bit in node.children and node.children[target_bit].count > 0:
                xor |= (1 << i)
                node = node.children[target_bit]
            else:
                node = node.children.get(bit, TrieNode())
        return xor

def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 找出强数对的最大异或值 II
    """
    nums.sort()
    trie = Trie()
    max_xor = 0
    left = 0
    for right, num in enumerate(nums):
        trie.insert(num)
        while num - nums[left] > nums[left]:
            trie.remove(nums[left])
            left += 1
        max_xor = max(max_xor, trie.find_max_xor(num))
    return max_xor

Solution = create_solution(solution_function_name)