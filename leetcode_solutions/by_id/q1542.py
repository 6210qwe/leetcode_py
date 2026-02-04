# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1542
标题: Consecutive Characters
难度: easy
链接: https://leetcode.cn/problems/consecutive-characters/
题目类型: 字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1446. 连续字符 - 给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。 请你返回字符串 s 的 能量。 示例 1： 输入：s = "leetcode" 输出：2 解释：子字符串 "ee" 长度为 2 ，只包含字符 'e' 。 示例 2： 输入：s = "abbcccddddeeeeedcba" 输出：5 解释：子字符串 "eeeee" 长度为 5 ，只包含字符 'e' 。 提示： * 1 <= s.length <= 500 * s 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一次遍历来找到最长的连续相同字符子串。

算法步骤:
1. 初始化两个变量：`max_length` 用于记录最大连续字符长度，`current_length` 用于记录当前连续字符长度。
2. 遍历字符串 `s`：
   - 如果当前字符与前一个字符相同，则增加 `current_length`。
   - 如果当前字符与前一个字符不同，则更新 `max_length` 并重置 `current_length` 为 1。
3. 最后返回 `max_length` 和 `current_length` 中的最大值。

关键点:
- 通过一次遍历即可找到最长的连续相同字符子串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 s 的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(s: str) -> int:
    """
    函数式接口 - 返回字符串 s 的能量
    """
    if not s:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    return max(max_length, current_length)


Solution = create_solution(solution_function_name)