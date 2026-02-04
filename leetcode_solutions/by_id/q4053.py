# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4053
标题: Majority Frequency Characters
难度: easy
链接: https://leetcode.cn/problems/majority-frequency-characters/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3692. 众数频率字符 - 给你一个由小写英文字母组成的字符串 s。 对于一个值 k，频率组 是在 s 中恰好出现 k 次的字符集合。 众数频率组 是包含 不同 字符数量最多的频率组。 返回一个字符串，包含众数频率组中的所有字符，字符的顺序 不限 。如果两个或多个频率组的大小并列最大，则选择其频率 k 较大 的那个组。 示例 1: 输入: s = "aaabbbccdddde" 输出: "ab" 解释: 频率 (k) 组中不同字符 组大小 是否众数? 4 {d} 1 否 3 {a, b} 2 是 2 {c} 1 否 1 {e} 1 否 字符 'a' 和 'b' 的频率相同，都为 3，它们在众数频率组中。 示例 2: 输入: s = "abcd" 输出: "abcd" 解释: 频率 (k) 组中不同字符 组大小 是否众数? 1 {a, b, c, d} 4 是 所有字符的频率都相同，都为 1，它们都在众数频率组中。 示例 3: 输入: s = "pfpfgi" 输出: "fp" 解释: 频率 (k) 组中不同字符 组大小 是否众数? 2 {p, f} 2 是 1 {g, i} 2 否 (组大小并列，选择频率更大的 k = 2) 字符 'p' 和 'f' 的频率相同，都为 2，它们在众数频率组中。频率为 1 的组大小并列，但我们选择频率更高的组 2。 提示: * 1 <= s.length <= 100 * s 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表统计每个字符的频率，然后遍历哈希表找到众数频率组。

算法步骤:
1. 使用哈希表统计每个字符的频率。
2. 初始化一个字典 `freq_groups`，键为频率，值为具有该频率的字符列表。
3. 遍历哈希表，将字符按频率分组到 `freq_groups` 中。
4. 找到 `freq_groups` 中字符数量最多的频率组，如果有多个频率组字符数量相同，则选择频率较大的那个组。
5. 返回该频率组中的所有字符。

关键点:
- 使用哈希表高效统计字符频率。
- 通过字典 `freq_groups` 分组字符，并找到字符数量最多的频率组。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 s 的长度。需要遍历字符串一次来统计频率，再遍历哈希表一次来分组和找到众数频率组。
空间复杂度: O(1)，因为字符集是固定的（26 个小写字母），所以哈希表和 `freq_groups` 的大小都是常数级别的。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(s: str) -> str:
    """
    函数式接口 - 返回众数频率组中的所有字符
    """
    # 统计每个字符的频率
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # 将字符按频率分组
    freq_groups = {}
    for char, count in char_count.items():
        if count not in freq_groups:
            freq_groups[count] = []
        freq_groups[count].append(char)
    
    # 找到字符数量最多的频率组
    max_group_size = 0
    max_freq = 0
    for freq, group in freq_groups.items():
        if len(group) > max_group_size or (len(group) == max_group_size and freq > max_freq):
            max_group_size = len(group)
            max_freq = freq
    
    # 返回该频率组中的所有字符
    return ''.join(freq_groups[max_freq])


Solution = create_solution(solution_function_name)