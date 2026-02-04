# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1995
标题: Finding Pairs With a Certain Sum
难度: medium
链接: https://leetcode.cn/problems/finding-pairs-with-a-certain-sum/
题目类型: 设计、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1865. 找出和为指定值的下标对 - 给你两个整数数组 nums1 和 nums2 ，请你实现一个支持下述两类查询的数据结构： 1. 累加 ，将一个正整数加到 nums2 中指定下标对应元素上。 2. 计数 ，统计满足 nums1[i] + nums2[j] 等于指定值的下标对 (i, j) 数目（0 <= i < nums1.length 且 0 <= j < nums2.length）。 实现 FindSumPairs 类： * FindSumPairs(int[] nums1, int[] nums2) 使用整数数组 nums1 和 nums2 初始化 FindSumPairs 对象。 * void add(int index, int val) 将 val 加到 nums2[index] 上，即，执行 nums2[index] += val 。 * int count(int tot) 返回满足 nums1[i] + nums2[j] == tot 的下标对 (i, j) 数目。 示例： 输入： ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"] [[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]] 输出： [null, 8, null, 2, 1, null, null, 11] 解释： FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]); findSumPairs.count(7); // 返回 8 ; 下标对 (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) 满足 2 + 5 = 7 ，下标对 (5,1), (5,5) 满足 3 + 4 = 7 findSumPairs.add(3, 2); // 此时 nums2 = [1,4,5,4,5,4] findSumPairs.count(8); // 返回 2 ；下标对 (5,2), (5,4) 满足 3 + 5 = 8 findSumPairs.count(4); // 返回 1 ；下标对 (5,0) 满足 3 + 1 = 4 findSumPairs.add(0, 1); // 此时 nums2 = [2,4,5,4,5,4] findSumPairs.add(1, 1); // 此时 nums2 = [2,5,5,4,5,4] findSumPairs.count(7); // 返回 11 ；下标对 (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) 满足 2 + 5 = 7 ，下标对 (5,3), (5,5) 满足 3 + 4 = 7 提示： * 1 <= nums1.length <= 1000 * 1 <= nums2.length <= 105 * 1 <= nums1[i] <= 109 * 1 <= nums2[i] <= 105 * 0 <= index < nums2.length * 1 <= val <= 105 * 1 <= tot <= 109 * 最多调用 add 和 count 函数各 1000 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录 `nums2` 中每个元素的出现次数，以便在 `count` 操作中快速查找。

算法步骤:
1. 初始化时，使用一个哈希表 `num2_count` 记录 `nums2` 中每个元素的出现次数。
2. 在 `add` 操作中，更新 `nums2` 中指定下标的元素，并相应地更新 `num2_count`。
3. 在 `count` 操作中，遍历 `nums1` 中的每个元素，计算其与 `tot` 的差值，并在 `num2_count` 中查找该差值的出现次数，累加结果。

关键点:
- 使用哈希表来存储 `nums2` 中每个元素的出现次数，以实现高效的 `count` 操作。
- 在 `add` 操作中，需要同时更新 `nums2` 和 `num2_count`。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 `nums1` 的长度，m 是 `nums2` 的长度。初始化和 `add` 操作的时间复杂度为 O(1)，`count` 操作的时间复杂度为 O(n)。
空间复杂度: O(m)，其中 m 是 `nums2` 的长度。需要额外的空间来存储 `nums2` 中每个元素的出现次数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.num2_count = {}
        for num in nums2:
            self.num2_count[num] = self.num2_count.get(num, 0) + 1

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val
        self.nums2[index] = new_val
        self.num2_count[old_val] -= 1
        if self.num2_count[old_val] == 0:
            del self.num2_count[old_val]
        self.num2_count[new_val] = self.num2_count.get(new_val, 0) + 1

    def count(self, tot: int) -> int:
        result = 0
        for num in self.nums1:
            complement = tot - num
            if complement in self.num2_count:
                result += self.num2_count[complement]
        return result


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(FindSumPairs)