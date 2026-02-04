# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3436
标题: Find Subarray With Bitwise OR Closest to K
难度: hard
链接: https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/
题目类型: 位运算、线段树、数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3171. 找到按位或最接近 K 的子数组 - 给你一个数组 nums 和一个整数 k 。你需要找到 nums 的一个 子数组 ，满足子数组中所有元素按位或运算 OR 的值与 k 的 绝对差 尽可能 小 。换言之，你需要选择一个子数组 nums[l..r] 满足 |k - (nums[l] OR nums[l + 1] ... OR nums[r])| 最小。 请你返回 最小 的绝对差值。 子数组 是数组中连续的 非空 元素序列。 示例 1： 输入：nums = [1,2,4,5], k = 3 输出：0 解释： 子数组 nums[0..1] 的按位 OR 运算值为 3 ，得到最小差值 |3 - 3| = 0 。 示例 2： 输入：nums = [1,3,1,3], k = 2 输出：1 解释： 子数组 nums[1..1] 的按位 OR 运算值为 3 ，得到最小差值 |3 - 2| = 1 。 示例 3： 输入：nums = [1], k = 10 输出：9 解释： 只有一个子数组，按位 OR 运算值为 1 ，得到最小差值 |10 - 1| = 9 。 提示： * 1 <= nums.length <= 105 * 1 <= nums[i] <= 109 * 1 <= k <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口和位运算来找到最接近 k 的子数组。

算法步骤:
1. 初始化两个指针 left 和 right，分别表示当前窗口的左右边界。
2. 使用一个变量 current_or 来存储当前窗口内的按位或结果。
3. 遍历数组，逐步扩展右边界，并更新 current_or。
4. 如果 current_or 大于等于 k，尝试收缩左边界以找到更优解。
5. 记录每次计算的最小绝对差值。

关键点:
- 使用滑动窗口可以有效地减少不必要的重复计算。
- 通过位运算快速更新当前窗口的按位或结果。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_subarray_with_bitwise_or_closest_to_k(nums: List[int], k: int) -> int:
    """
    函数式接口 - 找到按位或最接近 K 的子数组
    """
    n = len(nums)
    min_diff = float('inf')
    current_or = 0
    left = 0

    for right in range(n):
        current_or |= nums[right]
        while current_or >= k and left <= right:
            min_diff = min(min_diff, abs(k - current_or))
            current_or ^= nums[left]
            left += 1
        min_diff = min(min_diff, abs(k - current_or))

    return min_diff


Solution = create_solution(find_subarray_with_bitwise_or_closest_to_k)