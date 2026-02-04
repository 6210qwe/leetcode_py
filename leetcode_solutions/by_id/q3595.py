# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3595
标题: Rearrange K Substrings to Form Target String
难度: medium
链接: https://leetcode.cn/problems/rearrange-k-substrings-to-form-target-string/
题目类型: 哈希表、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3365. 重排子字符串以形成目标字符串 - 给你两个字符串 s 和 t（它们互为字母异位词），以及一个整数 k。 你的任务是判断是否可以将字符串 s 分割成 k 个等长的子字符串，然后重新排列这些子字符串，并以任意顺序连接它们，使得最终得到的新字符串与给定的字符串 t 相匹配。 如果可以做到，返回 true；否则，返回 false。 字母异位词 是指由另一个单词或短语的所有字母重新排列形成的单词或短语，使用所有原始字母恰好一次。 子字符串 是字符串中的一个连续 非空 字符序列。 示例 1： 输入： s = "abcd", t = "cdab", k = 2 输出： true 解释： * 将 s 分割成 2 个长度为 2 的子字符串：["ab", "cd"]。 * 重新排列这些子字符串为 ["cd", "ab"]，然后连接它们得到 "cdab"，与 t 相匹配。 示例 2： 输入： s = "aabbcc", t = "bbaacc", k = 3 输出： true 解释： * 将 s 分割成 3 个长度为 2 的子字符串：["aa", "bb", "cc"]。 * 重新排列这些子字符串为 ["bb", "aa", "cc"]，然后连接它们得到 "bbaacc"，与 t 相匹配。 示例 3： 输入： s = "aabbcc", t = "bbaacc", k = 2 输出： false 解释： * 将 s 分割成 2 个长度为 3 的子字符串：["aab", "bcc"]。 * 这些子字符串无法重新排列形成 t = "bbaacc"，所以输出 false。 提示： * 1 <= s.length == t.length <= 2 * 105 * 1 <= k <= s.length * s.length 能被 k 整除。 * s 和 t 仅由小写英文字母组成。 * 输入保证 s 和 t 互为字母异位词。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用计数器来验证每个子字符串的字符频率是否匹配。

算法步骤:
1. 检查 s 和 t 是否具有相同的字符频率。
2. 计算每个子字符串的长度。
3. 将 s 和 t 分割成 k 个子字符串。
4. 对每个子字符串进行字符频率计数。
5. 比较 s 和 t 的子字符串字符频率是否相同。

关键点:
- 使用计数器来验证字符频率。
- 确保每个子字符串的长度相等。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + k * (n/k) * log(n/k)) = O(n + n * log(n/k)) = O(n * log(n/k))
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from collections import Counter


def can_rearrange_substrings(s: str, t: str, k: int) -> bool:
    """
    判断是否可以将字符串 s 分割成 k 个等长的子字符串，然后重新排列这些子字符串，并以任意顺序连接它们，使得最终得到的新字符串与给定的字符串 t 相匹配。
    """
    # 检查 s 和 t 是否具有相同的字符频率
    if Counter(s) != Counter(t):
        return False
    
    n = len(s)
    if n % k != 0:
        return False
    
    sub_len = n // k
    s_substrings = [s[i * sub_len : (i + 1) * sub_len] for i in range(k)]
    t_substrings = [t[i * sub_len : (i + 1) * sub_len] for i in range(k)]
    
    # 对每个子字符串进行字符频率计数
    s_counts = [Counter(sub) for sub in s_substrings]
    t_counts = [Counter(sub) for sub in t_substrings]
    
    # 比较 s 和 t 的子字符串字符频率是否相同
    s_counts.sort()
    t_counts.sort()
    
    return s_counts == t_counts


Solution = create_solution(can_rearrange_substrings)