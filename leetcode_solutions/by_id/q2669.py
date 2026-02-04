# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2669
标题: Find the Substring With Maximum Cost
难度: medium
链接: https://leetcode.cn/problems/find-the-substring-with-maximum-cost/
题目类型: 数组、哈希表、字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2606. 找到最大开销的子字符串 - 给你一个字符串 s ，一个字符 互不相同 的字符串 chars 和一个长度与 chars 相同的整数数组 vals 。 子字符串的开销 是一个子字符串中所有字符对应价值之和。空字符串的开销是 0 。 字符的价值 定义如下： * 如果字符不在字符串 chars 中，那么它的价值是它在字母表中的位置（下标从 1 开始）。 * 比方说，'a' 的价值为 1 ，'b' 的价值为 2 ，以此类推，'z' 的价值为 26 。 * 否则，如果这个字符在 chars 中的位置为 i ，那么它的价值就是 vals[i] 。 请你返回字符串 s 的所有子字符串中的最大开销。 示例 1： 输入：s = "adaa", chars = "d", vals = [-1000] 输出：2 解释：字符 "a" 和 "d" 的价值分别为 1 和 -1000 。 最大开销子字符串是 "aa" ，它的开销为 1 + 1 = 2 。 2 是最大开销。 示例 2： 输入：s = "abc", chars = "abc", vals = [-1,-1,-1] 输出：0 解释：字符 "a" ，"b" 和 "c" 的价值分别为 -1 ，-1 和 -1 。 最大开销子字符串是 "" ，它的开销为 0 。 0 是最大开销。 提示： * 1 <= s.length <= 105 * s 只包含小写英文字母。 * 1 <= chars.length <= 26 * chars 只包含小写英文字母，且 互不相同 。 * vals.length == chars.length * -1000 <= vals[i] <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们维护一个当前子字符串的最大开销，并在遍历过程中更新最大值。

算法步骤:
1. 构建一个字典来存储每个字符的价值。
2. 初始化两个变量：`current_cost` 用于记录当前子字符串的开销，`max_cost` 用于记录最大开销。
3. 遍历字符串 `s`，对于每个字符：
   - 更新 `current_cost`。
   - 如果 `current_cost` 小于 0，则重置 `current_cost` 为 0。
   - 更新 `max_cost`。
4. 返回 `max_cost`。

关键点:
- 使用动态规划的思想，通过维护当前子字符串的开销来找到最大开销。
- 通过重置 `current_cost` 来处理负开销的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 s 的长度。
空间复杂度: O(1)，只需要常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_max_cost_substring(s: str, chars: str, vals: List[int]) -> int:
    """
    函数式接口 - 找到最大开销的子字符串
    """
    # 构建字符价值字典
    value_dict = {char: val for char, val in zip(chars, vals)}
    
    # 初始化变量
    current_cost = 0
    max_cost = 0
    
    # 遍历字符串 s
    for char in s:
        # 计算当前字符的价值
        if char in value_dict:
            char_value = value_dict[char]
        else:
            char_value = ord(char) - ord('a') + 1
        
        # 更新当前子字符串的开销
        current_cost += char_value
        
        # 如果当前子字符串的开销小于 0，则重置为 0
        if current_cost < 0:
            current_cost = 0
        
        # 更新最大开销
        max_cost = max(max_cost, current_cost)
    
    return max_cost


Solution = create_solution(find_max_cost_substring)