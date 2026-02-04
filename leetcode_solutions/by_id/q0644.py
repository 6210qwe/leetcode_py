# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 644
标题: Maximum Average Subarray II
难度: hard
链接: https://leetcode.cn/problems/maximum-average-subarray-ii/
题目类型: 数组、二分查找、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
644. 子数组最大平均数 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来找到子数组的最大平均值。通过二分查找确定一个可能的平均值，然后检查是否存在一个长度至少为 k 的子数组，其平均值大于等于这个可能的平均值。

算法步骤:
1. 初始化二分查找的左右边界 left 和 right，分别为数组的最小值和最大值。
2. 进行二分查找：
   - 计算中间值 mid。
   - 检查是否存在一个长度至少为 k 的子数组，其平均值大于等于 mid。
   - 如果存在，则更新左边界 left；否则，更新右边界 right。
3. 当二分查找结束时，left 即为所求的最大平均值。

关键点:
- 使用前缀和数组来快速计算子数组的和。
- 通过二分查找来逼近最大平均值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log(max-min))，其中 n 是数组的长度，max 和 min 分别是数组中的最大值和最小值。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_max_average(nums: List[int], k: int) -> float:
    """
    函数式接口 - 找到长度至少为 k 的子数组的最大平均值
    """
    def check(mid: float) -> bool:
        # 检查是否存在一个长度至少为 k 的子数组，其平均值大于等于 mid
        cur_sum = sum(nums[:k]) - mid * k
        if cur_sum >= 0:
            return True
        prev_min = 0
        for i in range(k, len(nums)):
            cur_sum += nums[i] - mid
            prev_min = min(prev_min, cur_sum)
            if cur_sum - prev_min >= 0:
                return True
        return False

    left, right = min(nums), max(nums)
    while right - left > 1e-5:
        mid = (left + right) / 2
        if check(mid):
            left = mid
        else:
            right = mid
    return left


Solution = create_solution(find_max_average)