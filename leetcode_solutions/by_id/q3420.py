# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3420
标题: Find Occurrences of an Element in an Array
难度: medium
链接: https://leetcode.cn/problems/find-occurrences-of-an-element-in-an-array/
题目类型: 数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3159. 查询数组中元素的出现位置 - 给你一个整数数组 nums ，一个整数数组 queries 和一个整数 x 。 对于每个查询 queries[i] ，你需要找到 nums 中第 queries[i] 个 x 的位置，并返回它的下标。如果数组中 x 的出现次数少于 queries[i] ，该查询的答案为 -1 。 请你返回一个整数数组 answer ，包含所有查询的答案。 示例 1： 输入：nums = [1,3,1,7], queries = [1,3,2,4], x = 1 输出：[0,-1,2,-1] 解释： * 第 1 个查询，第一个 1 出现在下标 0 处。 * 第 2 个查询，nums 中只有两个 1 ，所以答案为 -1 。 * 第 3 个查询，第二个 1 出现在下标 2 处。 * 第 4 个查询，nums 中只有两个 1 ，所以答案为 -1 。 示例 2： 输入：nums = [1,2,3], queries = [10], x = 5 输出：[-1] 解释： * 第 1 个查询，nums 中没有 5 ，所以答案为 -1 。 提示： * 1 <= nums.length, queries.length <= 105 * 1 <= queries[i] <= 105 * 1 <= nums[i], x <= 104
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个元素的位置，然后通过二分查找来快速定位第 k 个元素的位置。

算法步骤:
1. 遍历 `nums` 数组，使用哈希表记录每个元素 `x` 出现的所有位置。
2. 对于每个查询 `queries[i]`，使用二分查找在哈希表中找到第 `queries[i]` 个 `x` 的位置。
3. 如果 `x` 的出现次数少于 `queries[i]`，则返回 -1。

关键点:
- 使用哈希表记录每个元素的位置，方便快速查找。
- 使用二分查找来快速定位第 k 个元素的位置。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m log k)，其中 n 是 `nums` 的长度，m 是 `queries` 的长度，k 是 `x` 在 `nums` 中的最大出现次数。
空间复杂度: O(n)，用于存储哈希表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_occurrences(nums: List[int], queries: List[int], x: int) -> List[int]:
    """
    函数式接口 - 查找数组中元素的出现位置
    """
    # 记录每个元素 x 出现的所有位置
    positions = {}
    for i, num in enumerate(nums):
        if num == x:
            if num not in positions:
                positions[num] = []
            positions[num].append(i)

    def binary_search(arr, target):
        """二分查找第 target 个元素的位置"""
        if target > len(arr):
            return -1
        return arr[target - 1]

    # 处理每个查询
    result = []
    for query in queries:
        if x in positions:
            result.append(binary_search(positions[x], query))
        else:
            result.append(-1)

    return result


Solution = create_solution(find_occurrences)