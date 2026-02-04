# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1024
标题: Triples with Bitwise AND Equal To Zero
难度: hard
链接: https://leetcode.cn/problems/triples-with-bitwise-and-equal-to-zero/
题目类型: 位运算、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
982. 按位与为零的三元组 - 给你一个整数数组 nums ，返回其中 按位与三元组 的数目。 按位与三元组 是由下标 (i, j, k) 组成的三元组，并满足下述全部条件： * 0 <= i < nums.length * 0 <= j < nums.length * 0 <= k < nums.length * nums[i] & nums[j] & nums[k] == 0 ，其中 & 表示按位与运算符。 示例 1： 输入：nums = [2,1,3] 输出：12 解释：可以选出如下 i, j, k 三元组： (i=0, j=0, k=1) : 2 & 2 & 1 (i=0, j=1, k=0) : 2 & 1 & 2 (i=0, j=1, k=1) : 2 & 1 & 1 (i=0, j=1, k=2) : 2 & 1 & 3 (i=0, j=2, k=1) : 2 & 3 & 1 (i=1, j=0, k=0) : 1 & 2 & 2 (i=1, j=0, k=1) : 1 & 2 & 1 (i=1, j=0, k=2) : 1 & 2 & 3 (i=1, j=1, k=0) : 1 & 1 & 2 (i=1, j=2, k=0) : 1 & 3 & 2 (i=2, j=0, k=1) : 3 & 2 & 1 (i=2, j=1, k=0) : 3 & 1 & 2 示例 2： 输入：nums = [0,0,0] 输出：27 提示： * 1 <= nums.length <= 1000 * 0 <= nums[i] < 216
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录所有可能的按位与结果，然后通过查找哈希表来计算满足条件的三元组数量。

算法步骤:
1. 使用一个哈希表 `pair_count` 来记录所有可能的 `nums[i] & nums[j]` 结果及其出现次数。
2. 遍历 `nums` 数组，对于每个 `nums[k]`，检查 `pair_count` 中有多少个键值对的键与 `nums[k]` 按位与结果为 0。
3. 累加这些键值对的值，即为满足条件的三元组数量。

关键点:
- 使用哈希表记录所有可能的按位与结果，减少重复计算。
- 通过查找哈希表来快速计算满足条件的三元组数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是 nums 的长度。我们需要遍历所有可能的 (i, j) 对来构建哈希表，然后再遍历一次 nums 数组来查找满足条件的三元组。
空间复杂度: O(n^2)，哈希表 `pair_count` 最多存储 n^2 个不同的按位与结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_triplets(nums: List[int]) -> int:
    """
    计算按位与为零的三元组数量
    """
    pair_count = {}
    n = len(nums)
    
    # 构建哈希表，记录所有可能的 nums[i] & nums[j] 结果及其出现次数
    for i in range(n):
        for j in range(n):
            pair = nums[i] & nums[j]
            if pair in pair_count:
                pair_count[pair] += 1
            else:
                pair_count[pair] = 1
    
    # 遍历 nums 数组，计算满足条件的三元组数量
    triplets_count = 0
    for k in range(n):
        for pair, count in pair_count.items():
            if pair & nums[k] == 0:
                triplets_count += count
    
    return triplets_count


Solution = create_solution(count_triplets)