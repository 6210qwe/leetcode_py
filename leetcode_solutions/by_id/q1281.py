# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1281
标题: Can Make Palindrome from Substring
难度: medium
链接: https://leetcode.cn/problems/can-make-palindrome-from-substring/
题目类型: 位运算、数组、哈希表、字符串、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1177. 构建回文串检测 - 给你一个字符串 s，请你对 s 的子串进行检测。 每次检测，待检子串都可以表示为 queries[i] = [left, right, k]。我们可以 重新排列 子串 s[left], ..., s[right]，并从中选择 最多 k 项替换成任何小写英文字母。 如果在上述检测过程中，子串可以变成回文形式的字符串，那么检测结果为 true，否则结果为 false。 返回答案数组 answer[]，其中 answer[i] 是第 i 个待检子串 queries[i] 的检测结果。 注意：在替换时，子串中的每个字母都必须作为 独立的 项进行计数，也就是说，如果 s[left..right] = "aaa" 且 k = 2，我们只能替换其中的两个字母。（另外，任何检测都不会修改原始字符串 s，可以认为每次检测都是独立的） 示例： 输入：s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]] 输出：[true,false,false,true,true] 解释： queries[0] : 子串 = "d"，回文。 queries[1] : 子串 = "bc"，不是回文。 queries[2] : 子串 = "abcd"，只替换 1 个字符是变不成回文串的。 queries[3] : 子串 = "abcd"，可以变成回文的 "abba"。 也可以变成 "baab"，先重新排序变成 "bacd"，然后把 "cd" 替换为 "ab"。 queries[4] : 子串 = "abcda"，可以变成回文的 "abcba"。 提示： * 1 <= s.length, queries.length <= 10^5 * 0 <= queries[i][0] <= queries[i][1] < s.length * 0 <= queries[i][2] <= s.length * s 中只有小写英文字母
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀异或来快速计算子串中每个字符的奇偶性，并判断是否可以通过最多 k 次替换变成回文。

算法步骤:
1. 计算前缀异或数组，用于快速查询子串中每个字符的奇偶性。
2. 对于每个查询，使用前缀异或数组计算子串中每个字符的奇偶性。
3. 统计子串中奇数次出现的字符数量，如果该数量的一半小于等于 k，则可以变成回文。

关键点:
- 前缀异或数组可以在 O(1) 时间内计算任意子串中每个字符的奇偶性。
- 只需要统计奇数次出现的字符数量，因为每个字符最多需要替换一次才能变成回文。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + q)，其中 n 是字符串 s 的长度，q 是查询的数量。
空间复杂度: O(n)，用于存储前缀异或数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_make_pali_queries(s: str, queries: List[List[int]]) -> List[bool]:
    """
    函数式接口 - 判断子串是否可以通过最多 k 次替换变成回文。
    """
    # 计算前缀异或数组
    prefix_xor = [0]
    for char in s:
        prefix_xor.append(prefix_xor[-1] ^ (1 << (ord(char) - ord('a'))))
    
    def count_odd_chars(left: int, right: int) -> int:
        # 计算子串中每个字符的奇偶性
        xor_result = prefix_xor[right + 1] ^ prefix_xor[left]
        return bin(xor_result).count('1')
    
    result = []
    for left, right, k in queries:
        odd_count = count_odd_chars(left, right)
        # 判断是否可以通过最多 k 次替换变成回文
        result.append(odd_count // 2 <= k)
    
    return result


Solution = create_solution(can_make_pali_queries)