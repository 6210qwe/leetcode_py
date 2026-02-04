# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3944
标题: Minimum Time to Activate String
难度: medium
链接: https://leetcode.cn/problems/minimum-time-to-activate-string/
题目类型: 数组、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3639. 变为活跃状态的最小时间 - 给你一个长度为 n 的字符串 s 和一个整数数组 order，其中 order 是范围 [0, n - 1] 内数字的一个 排列。 从时间 t = 0 开始，在每个时间点，将字符串 s 中下标为 order[t] 的字符替换为 '*'。 如果 子字符串 包含 至少 一个 '*' ，则认为该子字符串有效。 如果字符串中 有效子字符串 的总数大于或等于 k，则称该字符串为 活跃 字符串。 返回字符串 s 变为 活跃 状态的最小时间 t。如果无法变为活跃状态，返回 -1。 示例 1: 输入: s = "abc", order = [1,0,2], k = 2 输出: 0 解释: t order[t] 修改后的 s 有效子字符串 计数 激活状态 (计数 >= k) 0 1 "a*c" "*", "a*", "*c", "a*c" 4 是 字符串 s 在 t = 0 时变为激活状态。因此，答案是 0。 示例 2: 输入: s = "cat", order = [0,2,1], k = 6 输出: 2 解释: t order[t] 修改后的 s 有效子字符串 计数 激活状态 (计数 >= k) 0 0 "*at" "*", "*a", "*at" 3 否 1 2 "*a*" "*", "*a", "*a*", "a*", "*" 5 否 2 1 "***" 所有子字符串(包含 '*') 6 是 字符串 s 在 t = 2 时变为激活状态。因此，答案是 2。 示例 3: 输入: s = "xy", order = [0,1], k = 4 输出: -1 解释: 即使完成所有替换，也无法得到 k = 4 个有效子字符串。因此，答案是 -1。 提示: * 1 <= n == s.length <= 105 * order.length == n * 0 <= order[i] <= n - 1 * s 由小写英文字母组成。 * order 是从 0 到 n - 1 的整数排列。 * 1 <= k <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀和和二分查找来高效计算有效子字符串的数量。

算法步骤:
1. 初始化一个前缀和数组 `prefix_sum`，用于记录在每个位置之前的 '*' 的数量。
2. 遍历 `order` 数组，逐步将字符替换为 '*'，并更新 `prefix_sum`。
3. 使用二分查找来确定最小的时间 `t`，使得有效子字符串的数量大于或等于 `k`。
4. 如果找到这样的 `t`，返回 `t`；否则返回 -1。

关键点:
- 前缀和数组 `prefix_sum` 用于快速计算有效子字符串的数量。
- 二分查找用于高效地找到最小的时间 `t`。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimum_time_to_activate_string(s: str, order: List[int], k: int) -> int:
    n = len(s)
    prefix_sum = [0] * (n + 1)
    active_count = 0

    def count_valid_substrings(t: int) -> int:
        nonlocal active_count
        for i in range(t):
            index = order[i]
            if s[index] != '*':
                s_list = list(s)
                s_list[index] = '*'
                s = ''.join(s_list)
                prefix_sum[index + 1] = prefix_sum[index] + 1
                active_count += (index + 1) * 2 - prefix_sum[index + 1]
        return active_count

    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if count_valid_substrings(mid) >= k:
            right = mid
        else:
            left = mid + 1

    if count_valid_substrings(left) >= k:
        return left
    return -1


Solution = create_solution(minimum_time_to_activate_string)