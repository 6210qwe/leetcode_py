# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1146
标题: Greatest Common Divisor of Strings
难度: easy
链接: https://leetcode.cn/problems/greatest-common-divisor-of-strings/
题目类型: 数学、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1071. 字符串的最大公因子 - 对于字符串 s 和 t，只有在 s = t + t + t + ... + t + t（t 自身连接 1 次或多次）时，我们才认定 “t 能除尽 s”。 给定两个字符串 str1 和 str2 。返回 最长字符串 x，要求满足 x 能除尽 str1 且 x 能除尽 str2 。 示例 1： 输入：str1 = "ABCABC", str2 = "ABC" 输出："ABC" 示例 2： 输入：str1 = "ABABAB", str2 = "ABAB" 输出："AB" 示例 3： 输入：str1 = "LEET", str2 = "CODE" 输出："" 示例 4： 输入：str1 = "AAAAAB", str2 = "AAA" 输出："" 提示： * 1 <= str1.length, str2.length <= 1000 * str1 和 str2 由大写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用最大公约数 (GCD) 来找到最长的公共前缀。

算法步骤:
1. 计算两个字符串长度的最大公约数。
2. 提取该长度的子串作为候选解。
3. 验证该子串是否能同时整除两个字符串。

关键点:
- 使用 `math.gcd` 函数来计算两个字符串长度的最大公约数。
- 通过验证子串是否能整除两个字符串来确保结果的正确性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 和 m 分别是 str1 和 str2 的长度。计算 GCD 的时间复杂度为 O(log(min(n, m)))，验证子串的时间复杂度为 O(n + m)。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
import math


def gcd_of_strings(str1: str, str2: str) -> str:
    """
    返回两个字符串的最大公因子。
    """
    # 计算两个字符串长度的最大公约数
    gcd_length = math.gcd(len(str1), len(str2))
    
    # 提取该长度的子串作为候选解
    candidate = str1[:gcd_length]
    
    # 验证该子串是否能同时整除两个字符串
    if str1 == candidate * (len(str1) // gcd_length) and str2 == candidate * (len(str2) // gcd_length):
        return candidate
    else:
        return ""


Solution = create_solution(gcd_of_strings)