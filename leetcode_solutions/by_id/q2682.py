# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2682
标题: Count Increasing Quadruplets
难度: hard
链接: https://leetcode.cn/problems/count-increasing-quadruplets/
题目类型: 树状数组、数组、动态规划、枚举、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2552. 统计上升四元组 - 给你一个长度为 n 下标从 0 开始的整数数组 nums ，它包含 1 到 n 的所有数字，请你返回上升四元组的数目。 如果一个四元组 (i, j, k, l) 满足以下条件，我们称它是上升的： * 0 <= i < j < k < l < n 且 * nums[i] < nums[k] < nums[j] < nums[l] 。 示例 1： 输入：nums = [1,3,2,4,5] 输出：2 解释： - 当 i = 0 ，j = 1 ，k = 2 且 l = 3 时，有 nums[i] < nums[k] < nums[j] < nums[l] 。 - 当 i = 0 ，j = 1 ，k = 2 且 l = 4 时，有 nums[i] < nums[k] < nums[j] < nums[l] 。 没有其他的四元组，所以我们返回 2 。 示例 2： 输入：nums = [1,2,3,4] 输出：0 解释：只存在一个四元组 i = 0 ，j = 1 ，k = 2 ，l = 3 ，但是 nums[j] < nums[k] ，所以我们返回 0 。 提示： * 4 <= nums.length <= 4000 * 1 <= nums[i] <= nums.length * nums 中所有数字 互不相同 ，nums 是一个排列。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用树状数组来维护前缀和，以高效地计算满足条件的四元组数量。

算法步骤:
1. 初始化两个树状数组，分别用于维护左侧和右侧的前缀和。
2. 遍历数组，对于每个元素，计算其左侧和右侧的前缀和。
3. 对于每个可能的中间元素对 (j, k)，计算满足条件的 i 和 l 的数量，并累加到结果中。

关键点:
- 使用树状数组可以高效地进行区间查询和更新操作。
- 通过两次遍历数组，分别计算左侧和右侧的前缀和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 log n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import bisect

class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, idx, val):
        while idx <= self.n:
            self.tree[idx] += val
            idx += idx & -idx

    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

def count_quadruplets(nums: List[int]) -> int:
    n = len(nums)
    left_bit = BIT(n)
    right_bit = BIT(n)
    count = 0

    for num in nums:
        right_bit.update(num, 1)

    for j in range(n):
        right_bit.update(nums[j], -1)
        for k in range(j + 1, n):
            if nums[j] > nums[k]:
                left_count = left_bit.query(nums[k] - 1)
                right_count = right_bit.query(n) - right_bit.query(nums[j])
                count += left_count * right_count
        left_bit.update(nums[j], 1)

    return count

Solution = create_solution(count_quadruplets)