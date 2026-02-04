# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4073
标题: Lexicographically Smallest String After Reverse
难度: medium
链接: https://leetcode.cn/problems/lexicographically-smallest-string-after-reverse/
题目类型: 双指针、二分查找、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3722. 反转后字典序最小的字符串 - 给你一个由小写英文字母组成的、长度为 n 的字符串 s。 你 必须执行 恰好 一次操作：选择一个整数 k，满足 1 <= k <= n，然后执行以下两个选项之一： * 反转 s 的 前 k 个字符，或 * 反转 s 的 后 k 个字符。 返回在 恰好 执行一次此类操作后可以获得的 字典序最小 的字符串。 如果字符串 a 和字符串 b 在第一个不同的位置上，a 中的字母在字母表中比 b 中对应的字母出现得更早，则称字符串 a 字典序小于 字符串 b。如果前 min(a.length, b.length) 个字符都相同，则较短的字符串字典序较小。 示例 1: 输入: s = "dcab" 输出: "acdb" 解释: * 选择 k = 3，反转前 3 个字符。 * 将 "dca" 反转为 "acd"，得到的字符串 s = "acdb"，这是可获得的字典序最小的字符串。 示例 2: 输入: s = "abba" 输出: "aabb" 解释: * 选择 k = 3，反转后 3 个字符。 * 将 "bba" 反转为 "abb"，得到的字符串是 "aabb"，这是可获得的字典序最小的字符串。 示例 3: 输入: s = "zxy" 输出: "xzy" 解释: * 选择 k = 2，反转前 2 个字符。 * 将 "zx" 反转为 "xz"，得到的字符串是 "xzy"，这是可获得的字典序最小的字符串。 提示: * 1 <= n == s.length <= 1000 * s 由小写英文字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过比较反转前 k 个字符和反转后 k 个字符的结果，找到字典序最小的字符串。

算法步骤:
1. 定义一个辅助函数 `reverse_substring` 来反转字符串的一部分。
2. 遍历所有可能的 k 值，分别计算反转前 k 个字符和反转后 k 个字符的结果。
3. 比较这些结果，返回字典序最小的字符串。

关键点:
- 使用双指针方法来高效地反转字符串的一部分。
- 通过遍历所有可能的 k 值来确保找到最优解。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是字符串的长度。需要遍历所有可能的 k 值，并且每次反转操作的时间复杂度是 O(k)。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def reverse_substring(s: str, start: int, end: int) -> str:
    """
    辅助函数：反转字符串 s 从 start 到 end 的部分。
    """
    return s[:start] + s[start:end+1][::-1] + s[end+1:]


def solution_function_name(s: str) -> str:
    """
    函数式接口 - 反转后字典序最小的字符串
    """
    n = len(s)
    min_string = s
    
    for k in range(1, n + 1):
        # 反转前 k 个字符
        reversed_prefix = reverse_substring(s, 0, k - 1)
        if reversed_prefix < min_string:
            min_string = reversed_prefix
        
        # 反转后 k 个字符
        reversed_suffix = reverse_substring(s, n - k, n - 1)
        if reversed_suffix < min_string:
            min_string = reversed_suffix
    
    return min_string


Solution = create_solution(solution_function_name)