# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3184
标题: Maximum Balanced Subsequence Sum
难度: hard
链接: https://leetcode.cn/problems/maximum-balanced-subsequence-sum/
题目类型: 树状数组、线段树、数组、二分查找、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2926. 平衡子序列的最大和 - 给你一个下标从 0 开始的整数数组 nums 。 nums 一个长度为 k 的 子序列 指的是选出 k 个 下标 i0 < i1 < ... < ik-1 ，如果这个子序列满足以下条件，我们说它是 平衡的 ： * 对于范围 [1, k - 1] 内的所有 j ，nums[ij] - nums[ij-1] >= ij - ij-1 都成立。 nums 长度为 1 的 子序列 是平衡的。 请你返回一个整数，表示 nums 平衡 子序列里面的 最大元素和 。 一个数组的 子序列 指的是从原数组中删除一些元素（也可能一个元素也不删除）后，剩余元素保持相对顺序得到的 非空 新数组。 示例 1： 输入：nums = [3,3,5,6] 输出：14 解释：这个例子中，选择子序列 [3,5,6] ，下标为 0 ，2 和 3 的元素被选中。 nums[2] - nums[0] >= 2 - 0 。 nums[3] - nums[2] >= 3 - 2 。 所以，这是一个平衡子序列，且它的和是所有平衡子序列里最大的。 包含下标 1 ，2 和 3 的子序列也是一个平衡的子序列。 最大平衡子序列和为 14 。 示例 2： 输入：nums = [5,-1,-3,8] 输出：13 解释：这个例子中，选择子序列 [5,8] ，下标为 0 和 3 的元素被选中。 nums[3] - nums[0] >= 3 - 0 。 所以，这是一个平衡子序列，且它的和是所有平衡子序列里最大的。 最大平衡子序列和为 13 。 示例 3： 输入：nums = [-2,-1] 输出：-1 解释：这个例子中，选择子序列 [-1] 。 这是一个平衡子序列，而且它的和是 nums 所有平衡子序列里最大的。 提示： * 1 <= nums.length <= 105 * -109 <= nums[i] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用树状数组（Fenwick Tree）来维护前缀最大值。

算法步骤:
1. 将每个元素 nums[i] 转换为一个新的值 nums[i] - i，并对其进行离散化处理。
2. 使用树状数组来维护前缀最大值。
3. 遍历数组，对于每个元素，查询其在树状数组中的前缀最大值，并更新当前元素的最大和。
4. 更新树状数组中的当前元素的最大和。

关键点:
- 离散化处理可以将数值映射到较小的范围内，便于使用树状数组。
- 树状数组用于高效地查询和更新前缀最大值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 nums 的长度。离散化处理的时间复杂度为 O(n log n)，树状数组的操作时间为 O(log n)。
空间复杂度: O(n)，用于存储离散化后的值和树状数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, idx, val):
        while idx <= self.n:
            self.tree[idx] = max(self.tree[idx], val)
            idx += idx & -idx

    def query(self, idx):
        res = 0
        while idx > 0:
            res = max(res, self.tree[idx])
            idx -= idx & -idx
        return res

def solution_function_name(nums: List[int]) -> int:
    n = len(nums)
    # 离散化处理
    values = sorted(set(nums[i] - i for i in range(n)))
    rank = {val: i + 1 for i, val in enumerate(values)}
    
    # 初始化树状数组
    tree = FenwickTree(len(values))
    
    # 计算最大平衡子序列和
    max_sum = float('-inf')
    for i in range(n):
        val = nums[i] - i
        idx = rank[val]
        prev_max = tree.query(idx - 1)
        current_max = max(prev_max + nums[i], nums[i])
        max_sum = max(max_sum, current_max)
        tree.update(idx, current_max)
    
    return max_sum

Solution = create_solution(solution_function_name)