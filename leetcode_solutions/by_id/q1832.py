# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1832
标题: Minimum Operations to Make a Subsequence
难度: hard
链接: https://leetcode.cn/problems/minimum-operations-to-make-a-subsequence/
题目类型: 贪心、数组、哈希表、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1713. 得到子序列的最少操作次数 - 给你一个数组 target ，包含若干 互不相同 的整数，以及另一个整数数组 arr ，arr 可能 包含重复元素。 每一次操作中，你可以在 arr 的任意位置插入任一整数。比方说，如果 arr = [1,4,1,2] ，那么你可以在中间添加 3 得到 [1,4,3,1,2] 。你可以在数组最开始或最后面添加整数。 请你返回 最少 操作次数，使得 target 成为 arr 的一个子序列。 一个数组的 子序列 指的是删除原数组的某些元素（可能一个元素都不删除），同时不改变其余元素的相对顺序得到的数组。比方说，[2,7,4] 是 [4,2,3,7,2,1,4] 的子序列（加粗元素），但 [2,4,2] 不是子序列。 示例 1： 输入：target = [5,1,3], arr = [9,4,2,3,4] 输出：2 解释：你可以添加 5 和 1 ，使得 arr 变为 [5,9,4,1,2,3,4] ，target 为 arr 的子序列。 示例 2： 输入：target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1] 输出：3 提示： * 1 <= target.length, arr.length <= 105 * 1 <= target[i], arr[i] <= 109 * target 不包含任何重复元素。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用最长递增子序列 (LIS) 的思想来解决这个问题。首先，我们需要找到 `arr` 中与 `target` 相同的元素，并记录它们在 `target` 中的位置。然后，我们使用这些位置来构建一个最长递增子序列。最后，结果就是 `target` 的长度减去这个最长递增子序列的长度。

算法步骤:
1. 创建一个字典 `index_map`，将 `target` 中的每个元素映射到它的索引。
2. 遍历 `arr`，如果 `arr` 中的元素在 `target` 中存在，则将其索引加入一个新的列表 `indices`。
3. 在 `indices` 上应用 LIS 算法，找到最长递增子序列的长度。
4. 返回 `target` 的长度减去 LIS 的长度，即为最少操作次数。

关键点:
- 使用二分查找来优化 LIS 算法的时间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 `arr` 的长度。遍历 `arr` 的时间复杂度是 O(n)，而 LIS 算法的时间复杂度是 O(n log n)。
空间复杂度: O(n)，用于存储 `index_map` 和 `indices`。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_operations_to_subsequence(target: List[int], arr: List[int]) -> int:
    """
    函数式接口 - 计算将 target 变成 arr 的子序列所需的最少操作次数
    """
    # 创建一个字典，将 target 中的每个元素映射到它的索引
    index_map = {num: i for i, num in enumerate(target)}
    
    # 遍历 arr，如果 arr 中的元素在 target 中存在，则将其索引加入一个新的列表 indices
    indices = []
    for num in arr:
        if num in index_map:
            indices.append(index_map[num])
    
    # 在 indices 上应用 LIS 算法，找到最长递增子序列的长度
    def length_of_lis(nums: List[int]) -> int:
        dp = []
        for num in nums:
            idx = bisect.bisect_left(dp, num)
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num
        return len(dp)
    
    lis_length = length_of_lis(indices)
    
    # 返回 target 的长度减去 LIS 的长度，即为最少操作次数
    return len(target) - lis_length


Solution = create_solution(min_operations_to_subsequence)