# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1516
标题: The k-th Lexicographical String of All Happy Strings of Length n
难度: medium
链接: https://leetcode.cn/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
题目类型: 字符串、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1415. 长度为 n 的开心字符串中字典序第 k 小的字符串 - 一个 「开心字符串」定义为： * 仅包含小写字母 ['a', 'b', 'c']. * 对所有在 1 到 s.length - 1 之间的 i ，满足 s[i] != s[i + 1] （字符串的下标从 1 开始）。 比方说，字符串 "abc"，"ac"，"b" 和 "abcbabcbcb" 都是开心字符串，但是 "aa"，"baa" 和 "ababbc" 都不是开心字符串。 给你两个整数 n 和 k ，你需要将长度为 n 的所有开心字符串按字典序排序。 请你返回排序后的第 k 个开心字符串，如果长度为 n 的开心字符串少于 k 个，那么请你返回 空字符串 。 示例 1： 输入：n = 1, k = 3 输出："c" 解释：列表 ["a", "b", "c"] 包含了所有长度为 1 的开心字符串。按照字典序排序后第三个字符串为 "c" 。 示例 2： 输入：n = 1, k = 4 输出："" 解释：长度为 1 的开心字符串只有 3 个。 示例 3： 输入：n = 3, k = 9 输出："cab" 解释：长度为 3 的开心字符串总共有 12 个 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"] 。第 9 个字符串为 "cab" 示例 4： 输入：n = 2, k = 7 输出："" 示例 5： 输入：n = 10, k = 100 输出："abacbabacb" 提示： * 1 <= n <= 10 * 1 <= k <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用递归生成所有可能的开心字符串，并按字典序排序。

算法步骤:
1. 定义一个递归函数 `generate_happy_strings`，用于生成所有可能的开心字符串。
2. 在递归函数中，如果当前字符串长度达到 n，则将其加入结果列表。
3. 否则，遍历字符集 ['a', 'b', 'c']，选择与前一个字符不同的字符继续递归。
4. 最后，检查结果列表的长度是否大于等于 k，如果是则返回第 k-1 个字符串，否则返回空字符串。

关键点:
- 递归生成所有可能的开心字符串。
- 保证每个字符与前一个字符不同。
- 按字典序排序并返回第 k 个字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(3^n) - 生成所有可能的开心字符串需要 3^n 的时间。
空间复杂度: O(3^n) - 存储所有可能的开心字符串需要 3^n 的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def generate_happy_strings(current: str, n: int, result: List[str]):
    if len(current) == n:
        result.append(current)
        return
    for char in ['a', 'b', 'c']:
        if not current or current[-1] != char:
            generate_happy_strings(current + char, n, result)

def get_happy_string(n: int, k: int) -> str:
    result = []
    generate_happy_strings("", n, result)
    if k > len(result):
        return ""
    return result[k - 1]

Solution = create_solution(get_happy_string)