# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1772
标题: Create Sorted Array through Instructions
难度: hard
链接: https://leetcode.cn/problems/create-sorted-array-through-instructions/
题目类型: 树状数组、线段树、数组、二分查找、分治、有序集合、归并排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1649. 通过指令创建有序数组 - 给你一个整数数组 instructions ，你需要根据 instructions 中的元素创建一个有序数组。一开始你有一个空的数组 nums ，你需要 从左到右 遍历 instructions 中的元素，将它们依次插入 nums 数组中。每一次插入操作的 代价 是以下两者的 较小值 ： * nums 中 严格小于 instructions[i] 的数字数目。 * nums 中 严格大于 instructions[i] 的数字数目。 比方说，如果要将 3 插入到 nums = [1,2,3,5] ，那么插入操作的 代价 为 min(2, 1) (元素 1 和 2 小于 3 ，元素 5 大于 3 ），插入后 nums 变成 [1,2,3,3,5] 。 请你返回将 instructions 中所有元素依次插入 nums 后的 总最小代价 。由于答案会很大，请将它对 109 + 7 取余 后返回。 示例 1： 输入：instructions = [1,5,6,2] 输出：1 解释：一开始 nums = [] 。 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。 插入 5 ，代价为 min(1, 0) = 0 ，现在 nums = [1,5] 。 插入 6 ，代价为 min(2, 0) = 0 ，现在 nums = [1,5,6] 。 插入 2 ，代价为 min(1, 2) = 1 ，现在 nums = [1,2,5,6] 。 总代价为 0 + 0 + 0 + 1 = 1 。 示例 2: 输入：instructions = [1,2,3,6,5,4] 输出：3 解释：一开始 nums = [] 。 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。 插入 2 ，代价为 min(1, 0) = 0 ，现在 nums = [1,2] 。 插入 3 ，代价为 min(2, 0) = 0 ，现在 nums = [1,2,3] 。 插入 6 ，代价为 min(3, 0) = 0 ，现在 nums = [1,2,3,6] 。 插入 5 ，代价为 min(3, 1) = 1 ，现在 nums = [1,2,3,5,6] 。 插入 4 ，代价为 min(3, 2) = 2 ，现在 nums = [1,2,3,4,5,6] 。 总代价为 0 + 0 + 0 + 0 + 1 + 2 = 3 。 示例 3： 输入：instructions = [1,3,3,3,2,4,2,1,2] 输出：4 解释：一开始 nums = [] 。 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3] 。 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3] 。 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3,3] 。 插入 2 ，代价为 min(1, 3) = 1 ，现在 nums = [1,2,3,3,3] 。 插入 4 ，代价为 min(5, 0) = 0 ，现在 nums = [1,2,3,3,3,4] 。 ​​​​​插入 2 ，代价为 min(1, 4) = 1 ，现在 nums = [1,2,2,3,3,3,4] 。 插入 1 ，代价为 min(0, 6) = 0 ，现在 nums = [1,1,2,2,3,3,3,4] 。 插入 2 ，代价为 min(2, 4) = 2 ，现在 nums = [1,1,2,2,2,3,3,3,4] 。 总代价为 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4 。 提示： * 1 <= instructions.length <= 105 * 1 <= instructions[i] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用树状数组（Fenwick Tree）来高效地计算小于和大于当前元素的数量。

算法步骤:
1. 初始化一个大小为 max(instructions) + 1 的树状数组。
2. 遍历 instructions 数组，对于每个元素：
   - 计算小于该元素的数量。
   - 计算大于该元素的数量。
   - 计算插入代价，并更新总代价。
   - 更新树状数组以包含当前元素。
3. 返回总代价对 10^9 + 7 取余的结果。

关键点:
- 树状数组可以在 O(log n) 时间内进行单点更新和区间查询。
- 通过树状数组可以高效地计算小于和大于当前元素的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log M)，其中 n 是 instructions 的长度，M 是 instructions 中的最大值。
空间复杂度: O(M)，用于存储树状数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

MOD = 10**9 + 7

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

def create_sorted_array(instructions: List[int]) -> int:
    max_val = max(instructions)
    tree = FenwickTree(max_val)
    total_cost = 0

    for num in instructions:
        less_than = tree.query(num - 1)
        greater_than = tree.query(max_val) - tree.query(num)
        cost = min(less_than, greater_than)
        total_cost = (total_cost + cost) % MOD
        tree.update(num, 1)

    return total_cost

Solution = create_solution(create_sorted_array)