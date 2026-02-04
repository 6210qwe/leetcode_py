# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2877
标题: Shortest String That Contains Three Strings
难度: medium
链接: https://leetcode.cn/problems/shortest-string-that-contains-three-strings/
题目类型: 贪心、字符串、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2800. 包含三个字符串的最短字符串 - 给你三个字符串 a ，b 和 c ， 你的任务是找到长度 最短 的字符串，且这三个字符串都是它的 子字符串 。 如果有多个这样的字符串，请你返回 字典序最小 的一个。 请你返回满足题目要求的字符串。 注意： * 两个长度相同的字符串 a 和 b ，如果在第一个不相同的字符处，a 的字母在字母表中比 b 的字母 靠前 ，那么字符串 a 比字符串 b 字典序小 。 * 子字符串 是一个字符串中一段连续的字符序列。 示例 1： 输入：a = "abc", b = "bca", c = "aaa" 输出："aaabca" 解释：字符串 "aaabca" 包含所有三个字符串：a = ans[2...4] ，b = ans[3..5] ，c = ans[0..2] 。结果字符串的长度至少为 6 ，且"aaabca" 是字典序最小的一个。 示例 2： 输入：a = "ab", b = "ba", c = "aba" 输出："aba" 解释：字符串 "aba" 包含所有三个字符串：a = ans[0..1] ，b = ans[1..2] ，c = ans[0..2] 。由于 c 的长度为 3 ，结果字符串的长度至少为 3 。"aba" 是字典序最小的一个。 提示： * 1 <= a.length, b.length, c.length <= 100 * a ，b ，c 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 枚举所有可能的字符串组合顺序，并找到最短且字典序最小的组合。

算法步骤:
1. 定义一个辅助函数 `merge` 用于合并两个字符串，确保第二个字符串尽可能多地重叠到第一个字符串的末尾。
2. 枚举所有可能的字符串组合顺序（共 6 种）。
3. 对每种组合顺序，使用 `merge` 函数逐步合并字符串，得到最终的组合字符串。
4. 记录所有组合字符串中最短且字典序最小的一个。

关键点:
- 使用 `merge` 函数来最大化重叠部分，从而减少最终字符串的长度。
- 通过枚举所有可能的组合顺序，确保找到最优解。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是字符串的最大长度。因为需要枚举 6 种组合顺序，并且每次合并操作的时间复杂度为 O(n)。
空间复杂度: O(1)，除了输入和输出外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def merge(s1: str, s2: str) -> str:
    """
    合并两个字符串，确保 s2 尽可能多地重叠到 s1 的末尾。
    """
    for i in range(len(s1)):
        if s1[i:] == s2[:len(s1) - i]:
            return s1 + s2[len(s1) - i:]
    return s1 + s2


def solution_function_name(a: str, b: str, c: str) -> str:
    """
    找到包含三个字符串的最短字符串，且字典序最小。
    """
    # 枚举所有可能的组合顺序
    orders = [(a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)]
    
    min_str = None
    
    for order in orders:
        merged_str = order[0]
        for i in range(1, len(order)):
            merged_str = merge(merged_str, order[i])
        
        if min_str is None or len(merged_str) < len(min_str) or (len(merged_str) == len(min_str) and merged_str < min_str):
            min_str = merged_str
    
    return min_str


Solution = create_solution(solution_function_name)