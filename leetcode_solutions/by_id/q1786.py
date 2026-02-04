# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1786
标题: Count the Number of Consistent Strings
难度: easy
链接: https://leetcode.cn/problems/count-the-number-of-consistent-strings/
题目类型: 位运算、数组、哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1684. 统计一致字符串的数目 - 给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是 一致字符串 。 请你返回 words 数组中 一致字符串 的数目。 示例 1： 输入：allowed = "ab", words = ["ad","bd","aaab","baa","badab"] 输出：2 解释：字符串 "aaab" 和 "baa" 都是一致字符串，因为它们只包含字符 'a' 和 'b' 。 示例 2： 输入：allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"] 输出：7 解释：所有字符串都是一致的。 示例 3： 输入：allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"] 输出：4 解释：字符串 "cc"，"acd"，"ac" 和 "d" 是一致字符串。 提示： * 1 <= words.length <= 104 * 1 <= allowed.length <= 26 * 1 <= words[i].length <= 10 * allowed 中的字符 互不相同 。 * words[i] 和 allowed 只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用集合来存储 allowed 字符串中的字符，并检查每个 word 是否只包含这些字符。

算法步骤:
1. 将 allowed 字符串转换为集合，以便 O(1) 时间复杂度内进行成员检查。
2. 遍历 words 数组，对于每个 word，检查其所有字符是否都在 allowed 集合中。
3. 如果某个 word 的所有字符都在 allowed 集合中，则计数器加一。
4. 返回计数器的值。

关键点:
- 使用集合来提高字符检查的效率。
- 通过遍历每个 word 并检查其字符是否在 allowed 集合中来统计一致字符串的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 words 的长度，m 是每个 word 的平均长度。
空间复杂度: O(k)，其中 k 是 allowed 字符串的长度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_consistent_strings(allowed: str, words: List[str]) -> int:
    """
    函数式接口 - 统计一致字符串的数目
    """
    # 将 allowed 字符串转换为集合
    allowed_set = set(allowed)
    
    # 计数器初始化
    count = 0
    
    # 遍历 words 数组
    for word in words:
        # 检查 word 中的所有字符是否都在 allowed_set 中
        if all(char in allowed_set for char in word):
            count += 1
    
    return count


Solution = create_solution(count_consistent_strings)