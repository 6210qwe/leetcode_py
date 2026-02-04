# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 802
标题: K-th Smallest Prime Fraction
难度: medium
链接: https://leetcode.cn/problems/k-th-smallest-prime-fraction/
题目类型: 数组、双指针、二分查找、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
786. 第 K 个最小的质数分数 - 给你一个按递增顺序排序的数组 arr 和一个整数 k 。数组 arr 由 1 和若干 质数 组成，且其中所有整数互不相同。 对于每对满足 0 <= i < j < arr.length 的 i 和 j ，可以得到分数 arr[i] / arr[j] 。 那么第 k 个最小的分数是多少呢? 以长度为 2 的整数数组返回你的答案, 这里 answer[0] == arr[i] 且 answer[1] == arr[j] 。 示例 1： 输入：arr = [1,2,3,5], k = 3 输出：[2,5] 解释：已构造好的分数,排序后如下所示: 1/5, 1/3, 2/5, 1/2, 3/5, 2/3 很明显第三个最小的分数是 2/5 示例 2： 输入：arr = [1,7], k = 1 输出：[1,7] 提示： * 2 <= arr.length <= 1000 * 1 <= arr[i] <= 3 * 104 * arr[0] == 1 * arr[i] 是一个 质数 ，i > 0 * arr 中的所有数字 互不相同 ，且按 严格递增 排序 * 1 <= k <= arr.length * (arr.length - 1) / 2 进阶：你可以设计并实现时间复杂度小于 O(n2) 的算法解决此问题吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找和双指针来找到第 k 个最小的质数分数。

算法步骤:
1. 定义一个辅助函数 `count_smaller_or_equal`，用于计算小于等于给定值的分数数量。
2. 使用二分查找来确定第 k 个最小分数的值。
3. 在每次二分查找中，使用双指针来计算小于等于当前中间值的分数数量。
4. 根据计算结果调整二分查找的范围，直到找到第 k 个最小分数。

关键点:
- 使用二分查找和双指针结合，可以在 O(n log(max(arr))) 时间内解决问题。
- 辅助函数 `count_smaller_or_equal` 通过双指针遍历数组，计算小于等于给定值的分数数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log(max(arr)))
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def kth_smallest_prime_fraction(arr: List[int], k: int) -> List[int]:
    def count_smaller_or_equal(x: float) -> int:
        count = 0
        max_fraction = (0, 1)
        j = 1
        for i in range(len(arr) - 1):
            while j < len(arr) and arr[i] / arr[j] > x:
                j += 1
            if j < len(arr):
                count += len(arr) - j
                if arr[i] * max_fraction[1] > arr[j] * max_fraction[0]:
                    max_fraction = (arr[i], arr[j])
        return count, max_fraction

    low, high = 0.0, 1.0
    while low < high:
        mid = (low + high) / 2
        count, max_fraction = count_smaller_or_equal(mid)
        if count < k:
            low = mid
        elif count > k:
            high = mid
        else:
            return list(max_fraction)

    return list(max_fraction)


Solution = create_solution(kth_smallest_prime_fraction)