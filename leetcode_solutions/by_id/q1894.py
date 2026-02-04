# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1894
标题: Merge Strings Alternately
难度: easy
链接: https://leetcode.cn/problems/merge-strings-alternately/
题目类型: 双指针、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1768. 交替合并字符串 - 给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。 返回 合并后的字符串 。 示例 1： 输入：word1 = "abc", word2 = "pqr" 输出："apbqcr" 解释：字符串合并情况如下所示： word1： a b c word2： p q r 合并后： a p b q c r 示例 2： 输入：word1 = "ab", word2 = "pqrs" 输出："apbqrs" 解释：注意，word2 比 word1 长，"rs" 需要追加到合并后字符串的末尾。 word1： a b word2： p q r s 合并后： a p b q r s 示例 3： 输入：word1 = "abcd", word2 = "pq" 输出："apbqcd" 解释：注意，word1 比 word2 长，"cd" 需要追加到合并后字符串的末尾。 word1： a b c d word2： p q 合并后： a p b q c d 提示： * 1 <= word1.length, word2.length <= 100 * word1 和 word2 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针交替遍历两个字符串，并将字符依次添加到结果字符串中。

算法步骤:
1. 初始化两个指针 i 和 j 分别指向 word1 和 word2 的起始位置。
2. 创建一个空的结果字符串 result。
3. 交替从 word1 和 word2 中取字符，直到其中一个字符串遍历完毕。
4. 将剩余的字符直接追加到结果字符串中。

关键点:
- 使用双指针交替遍历字符串，确保字符交替添加。
- 处理字符串长度不一致的情况，将剩余字符追加到结果字符串中。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 和 m 分别是 word1 和 word2 的长度。
空间复杂度: O(n + m)，结果字符串的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def merge_alternately(word1: str, word2: str) -> str:
    """
    函数式接口 - 交替合并两个字符串
    """
    i, j = 0, 0
    result = []
    
    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1
    
    # 追加剩余的字符
    result.extend(word1[i:])
    result.extend(word2[j:])
    
    return ''.join(result)


Solution = create_solution(merge_alternately)