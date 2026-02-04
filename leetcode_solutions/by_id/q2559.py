# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2559
标题: Maximum Number of Non-overlapping Palindrome Substrings
难度: hard
链接: https://leetcode.cn/problems/maximum-number-of-non-overlapping-palindrome-substrings/
题目类型: 贪心、双指针、字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2472. 不重叠回文子字符串的最大数目 - 给你一个字符串 s 和一个 正 整数 k 。 从字符串 s 中选出一组满足下述条件且 不重叠 的子字符串：
* 每个子字符串的长度 至少 为 k 。
* 每个子字符串是一个 回文串 。
返回最优方案中能选择的子字符串的 最大 数目。 子字符串 是字符串中一个连续的字符序列。
示例 1 ：
输入：s = "abaccdbbd", k = 3
输出：2
解释：可以选择 s = "abaccdbbd" 中斜体加粗的子字符串。"aba" 和 "dbbd" 都是回文，且长度至少为 k = 3 。
可以证明，无法选出两个以上的有效子字符串。
示例 2 ：
输入：s = "adbcda", k = 2
输出：0
解释：字符串中不存在长度至少为 2 的回文子字符串。
提示：
* 1 <= k <= s.length <= 2000
* s 仅由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Manacher 算法预处理所有回文子串，然后使用贪心算法选择不重叠的最长回文子串。

算法步骤:
1. 使用 Manacher 算法预处理字符串 s，得到每个位置的最长回文半径。
2. 遍历字符串，记录每个位置的最长回文子串的长度。
3. 使用贪心算法选择不重叠的最长回文子串，确保每个子串的长度至少为 k。

关键点:
- 使用 Manacher 算法可以在 O(n) 时间内预处理所有回文子串。
- 通过贪心算法选择不重叠的最长回文子串，确保时间复杂度最优。
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


def manacher(s: str) -> List[int]:
    # Manacher 算法预处理
    t = '#'.join('^{}$'.format(s))
    n = len(t)
    p = [0] * n
    center = right = 0
    for i in range(1, n - 1):
        if right > i:
            p[i] = min(right - i, p[2 * center - i])
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1
        if i + p[i] > right:
            center, right = i, i + p[i]
    return p


def max_palindromes(s: str, k: int) -> int:
    n = len(s)
    p = manacher(s)
    palindromes = [0] * (n + 1)
    
    for i in range(1, n + 1):
        r = p[2 * i - 1]
        if r // 2 >= k:
            palindromes[i - r // 2] = r // 2
    
    count = 0
    last_end = 0
    for i in range(n + 1):
        if palindromes[i] >= k and i + palindromes[i] > last_end:
            count += 1
            last_end = i + palindromes[i]
    
    return count


Solution = create_solution(max_palindromes)