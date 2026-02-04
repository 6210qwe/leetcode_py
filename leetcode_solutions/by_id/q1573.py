# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1573
标题: Find Two Non-overlapping Sub-arrays Each With Target Sum
难度: medium
链接: https://leetcode.cn/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
题目类型: 数组、哈希表、二分查找、动态规划、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1477. 找两个和为目标值且不重叠的子数组 - 给你一个整数数组 arr 和一个整数值 target 。 请你在 arr 中找 两个互不重叠的子数组 且它们的和都等于 target 。可能会有多种方案，请你返回满足要求的两个子数组长度和的 最小值 。 请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 -1 。 示例 1： 输入：arr = [3,2,2,4,3], target = 3 输出：2 解释：只有两个子数组和为 3 （[3] 和 [3]）。它们的长度和为 2 。 示例 2： 输入：arr = [7,3,4,7], target = 7 输出：2 解释：尽管我们有 3 个互不重叠的子数组和为 7 （[7], [3,4] 和 [7]），但我们会选择第一个和第三个子数组，因为它们的长度和 2 是最小值。 示例 3： 输入：arr = [4,3,2,6,2,3,4], target = 6 输出：-1 解释：我们只有一个和为 6 的子数组。 示例 4： 输入：arr = [5,5,4,4,5], target = 3 输出：-1 解释：我们无法找到和为 3 的子数组。 示例 5： 输入：arr = [3,1,1,1,5,1,2,1], target = 3 输出：3 解释：注意子数组 [1,2] 和 [2,1] 不能成为一个方案因为它们重叠了。 提示： * 1 <= arr.length <= 10^5 * 1 <= arr[i] <= 1000 * 1 <= target <= 10^8
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和与哈希表来记录和为 target 的子数组的起始位置，并通过动态规划来找到最短的非重叠子数组。

算法步骤:
1. 计算前缀和数组 prefix_sum。
2. 使用哈希表记录每个前缀和第一次出现的位置。
3. 从右向左遍历数组，使用动态规划记录从当前索引到末尾的最小子数组长度。
4. 再次从左向右遍历数组，尝试找到一个和为 target 的子数组，并更新最小长度和。

关键点:
- 使用前缀和和哈希表快速找到和为 target 的子数组。
- 动态规划记录最小子数组长度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_two_non_overlapping_sub_arrays(arr: List[int], target: int) -> int:
    n = len(arr)
    if n < 2:
        return -1

    # 计算前缀和数组
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    # 哈希表记录前缀和第一次出现的位置
    prefix_sum_map = {}
    min_length = float('inf')
    dp = [float('inf')] * n

    # 从右向左遍历数组，记录从当前索引到末尾的最小子数组长度
    for i in range(n - 1, -1, -1):
        if prefix_sum[i + 1] - target in prefix_sum_map:
            dp[i] = min(dp[i], prefix_sum_map[prefix_sum[i + 1] - target] - i)
        if i < n - 1:
            dp[i] = min(dp[i], dp[i + 1])

    # 从左向右遍历数组，尝试找到一个和为 target 的子数组，并更新最小长度和
    for i in range(n):
        if prefix_sum[i + 1] - target in prefix_sum_map:
            j = prefix_sum_map[prefix_sum[i + 1] - target]
            if i + 1 < j:
                min_length = min(min_length, (i + 1 - j) + dp[j])
        if prefix_sum[i + 1] not in prefix_sum_map:
            prefix_sum_map[prefix_sum[i + 1]] = i + 1

    return min_length if min_length != float('inf') else -1


Solution = create_solution(find_two_non_overlapping_sub_arrays)