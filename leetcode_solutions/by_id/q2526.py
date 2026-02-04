# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2526
标题: Longest Increasing Subsequence II
难度: hard
链接: https://leetcode.cn/problems/longest-increasing-subsequence-ii/
题目类型: 树状数组、线段树、队列、数组、分治、动态规划、单调队列
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2407. 最长递增子序列 II - 给你一个整数数组 nums 和一个整数 k 。 找到 nums 中满足以下要求的最长子序列： * 子序列 严格递增 * 子序列中相邻元素的差值 不超过 k 。 请你返回满足上述要求的 最长子序列 的长度。 子序列 是从一个数组中删除部分元素后，剩余元素不改变顺序得到的数组。 示例 1： 输入：nums = [4,2,1,4,3,4,5,8,15], k = 3 输出：5 解释： 满足要求的最长子序列是 [1,3,4,5,8] 。 子序列长度为 5 ，所以我们返回 5 。 注意子序列 [1,3,4,5,8,15] 不满足要求，因为 15 - 8 = 7 大于 3 。 示例 2： 输入：nums = [7,4,5,1,8,12,4,7], k = 5 输出：4 解释： 满足要求的最长子序列是 [4,5,8,12] 。 子序列长度为 4 ，所以我们返回 4 。 示例 3： 输入：nums = [1,5], k = 1 输出：1 解释： 满足要求的最长子序列是 [1] 。 子序列长度为 1 ，所以我们返回 1 。 提示： * 1 <= nums.length <= 105 * 1 <= nums[i], k <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用树状数组（Fenwick Tree）来高效地查询和更新区间最大值。

算法步骤:
1. 初始化树状数组，大小为 max(nums) + 1。
2. 遍历 nums 数组，对于每个元素 num，查询 [num - k, num - 1] 区间的最大值，并更新当前元素的最大长度。
3. 更新树状数组中 num 位置的值为当前元素的最大长度。

关键点:
- 使用树状数组来高效地进行区间查询和单点更新。
- 通过离散化处理，将 nums 中的值映射到 [1, max(nums)] 范围内，以减少树状数组的大小。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 nums 的长度。每次查询和更新操作的时间复杂度为 O(log n)。
空间复杂度: O(n)，树状数组的空间复杂度为 O(n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, value: int) -> None:
        while index <= self.size:
            self.tree[index] = max(self.tree[index], value)
            index += index & -index

    def query(self, index: int) -> int:
        result = 0
        while index > 0:
            result = max(result, self.tree[index])
            index -= index & -index
        return result

def longest_increasing_subsequence_ii(nums: List[int], k: int) -> int:
    """
    函数式接口 - 返回满足要求的最长子序列的长度
    """
    if not nums:
        return 0

    # 离散化处理
    unique_nums = sorted(set(nums))
    rank = {num: i + 1 for i, num in enumerate(unique_nums)}

    # 初始化树状数组
    tree = FenwickTree(len(unique_nums))

    # 动态规划
    dp = [0] * len(nums)
    max_length = 0

    for i, num in enumerate(nums):
        num_rank = rank[num]
        left = bisect.bisect_left(unique_nums, num - k)
        right = bisect.bisect_left(unique_nums, num)
        if left < right:
            dp[i] = tree.query(right) + 1
        else:
            dp[i] = 1
        max_length = max(max_length, dp[i])
        tree.update(num_rank, dp[i])

    return max_length

Solution = create_solution(longest_increasing_subsequence_ii)