# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1294
标题: Range Frequency Queries
难度: medium
链接: https://leetcode.cn/problems/range-frequency-queries/
题目类型: 设计、线段树、数组、哈希表、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2080. 区间内查询数字的频率 - 请你设计一个数据结构，它能求出给定子数组内一个给定值的 频率 。 子数组中一个值的 频率 指的是这个子数组中这个值的出现次数。 请你实现 RangeFreqQuery 类： * RangeFreqQuery(int[] arr) 用下标从 0 开始的整数数组 arr 构造一个类的实例。 * int query(int left, int right, int value) 返回子数组 arr[left...right] 中 value 的 频率 。 一个 子数组 指的是数组中一段连续的元素。arr[left...right] 指的是 nums 中包含下标 left 和 right 在内 的中间一段连续元素。 示例 1： 输入： ["RangeFreqQuery", "query", "query"] [[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]] 输出： [null, 1, 2] 解释： RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]); rangeFreqQuery.query(1, 2, 4); // 返回 1 。4 在子数组 [33, 4] 中出现 1 次。 rangeFreqQuery.query(0, 11, 33); // 返回 2 。33 在整个子数组中出现 2 次。 提示： * 1 <= arr.length <= 105 * 1 <= arr[i], value <= 104 * 0 <= left <= right < arr.length * 调用 query 不超过 105 次。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储每个值在数组中的所有索引，然后使用二分查找来快速计算区间内的频率。

算法步骤:
1. 初始化时，遍历数组，将每个值的索引存入哈希表。
2. 查询时，使用二分查找找到左边界和右边界，计算区间内的频率。

关键点:
- 使用哈希表存储每个值的索引列表。
- 使用二分查找快速定位区间内的频率。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + q log n)，其中 n 是数组长度，q 是查询次数。初始化的时间复杂度是 O(n)，每次查询的时间复杂度是 O(log n)。
空间复杂度: O(n)，哈希表存储每个值的索引列表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.index_map = {}
        for i, num in enumerate(arr):
            if num not in self.index_map:
                self.index_map[num] = []
            self.index_map[num].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.index_map:
            return 0
        indices = self.index_map[value]
        left_idx = self._binary_search_left(indices, left)
        right_idx = self._binary_search_right(indices, right)
        return right_idx - left_idx

    def _binary_search_left(self, indices: List[int], target: int) -> int:
        low, high = 0, len(indices)
        while low < high:
            mid = (low + high) // 2
            if indices[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

    def _binary_search_right(self, indices: List[int], target: int) -> int:
        low, high = 0, len(indices)
        while low < high:
            mid = (low + high) // 2
            if indices[mid] <= target:
                low = mid + 1
            else:
                high = mid
        return low


Solution = create_solution(RangeFreqQuery)