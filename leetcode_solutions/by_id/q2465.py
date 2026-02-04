# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2465
标题: Shifting Letters II
难度: medium
链接: https://leetcode.cn/problems/shifting-letters-ii/
题目类型: 数组、字符串、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2381. 字母移位 II - 给你一个小写英文字母组成的字符串 s 和一个二维整数数组 shifts ，其中 shifts[i] = [starti, endi, directioni] 。对于每个 i ，将 s 中从下标 starti 到下标 endi （两者都包含）所有字符都进行移位运算，如果 directioni = 1 将字符向后移位，如果 directioni = 0 将字符向前移位。 将一个字符 向后 移位的意思是将这个字符用字母表中 下一个 字母替换（字母表视为环绕的，所以 'z' 变成 'a'）。类似的，将一个字符 向前 移位的意思是将这个字符用字母表中 前一个 字母替换（字母表是环绕的，所以 'a' 变成 'z' ）。 请你返回对 s 进行所有移位操作以后得到的最终字符串。 示例 1： 输入：s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]] 输出："ace" 解释：首先，将下标从 0 到 1 的字母向前移位，得到 s = "zac" 。 然后，将下标从 1 到 2 的字母向后移位，得到 s = "zbd" 。 最后，将下标从 0 到 2 的字符向后移位，得到 s = "ace" 。 示例 2: 输入：s = "dztz", shifts = [[0,0,0],[1,1,1]] 输出："catz" 解释：首先，将下标从 0 到 0 的字母向前移位，得到 s = "cztz" 。 最后，将下标从 1 到 1 的字符向后移位，得到 s = "catz" 。 提示： * 1 <= s.length, shifts.length <= 5 * 104 * shifts[i].length == 3 * 0 <= starti <= endi < s.length * 0 <= directioni <= 1 * s 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用差分数组来高效地处理区间更新，并通过前缀和计算最终的移位值。

算法步骤:
1. 初始化一个长度为 n+1 的差分数组 diff，用于记录每个位置的移位变化。
2. 遍历 shifts 数组，根据方向更新差分数组。
3. 计算前缀和，得到每个位置的最终移位值。
4. 根据最终移位值更新字符串 s。

关键点:
- 使用差分数组可以高效地处理区间更新。
- 通过前缀和计算最终的移位值。
- 字符移位时需要考虑模 26 的操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是字符串 s 的长度，m 是 shifts 数组的长度。
空间复杂度: O(n)，用于存储差分数组和前缀和。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def shifting_letters(s: str, shifts: List[List[int]]) -> str:
    n = len(s)
    diff = [0] * (n + 1)
    
    for start, end, direction in shifts:
        shift = 1 if direction == 1 else -1
        diff[start] += shift
        diff[end + 1] -= shift
    
    prefix_sum = 0
    result = []
    for i in range(n):
        prefix_sum += diff[i]
        new_char = chr(((ord(s[i]) - ord('a') + prefix_sum) % 26) + ord('a'))
        result.append(new_char)
    
    return ''.join(result)


Solution = create_solution(shifting_letters)