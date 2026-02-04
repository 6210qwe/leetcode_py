# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2977
标题: Check if a String Is an Acronym of Words
难度: easy
链接: https://leetcode.cn/problems/check-if-a-string-is-an-acronym-of-words/
题目类型: 数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2828. 判别首字母缩略词 - 给你一个字符串数组 words 和一个字符串 s ，请你判断 s 是不是 words 的 首字母缩略词 。 如果可以按顺序串联 words 中每个字符串的第一个字符形成字符串 s ，则认为 s 是 words 的首字母缩略词。例如，"ab" 可以由 ["apple", "banana"] 形成，但是无法从 ["bear", "aardvark"] 形成。 如果 s 是 words 的首字母缩略词，返回 true ；否则，返回 false 。 示例 1： 输入：words = ["alice","bob","charlie"], s = "abc" 输出：true 解释：words 中 "alice"、"bob" 和 "charlie" 的第一个字符分别是 'a'、'b' 和 'c'。因此，s = "abc" 是首字母缩略词。 示例 2： 输入：words = ["an","apple"], s = "a" 输出：false 解释：words 中 "an" 和 "apple" 的第一个字符分别是 'a' 和 'a'。 串联这些字符形成的首字母缩略词是 "aa" 。 因此，s = "a" 不是首字母缩略词。 示例 3： 输入：words = ["never","gonna","give","up","on","you"], s = "ngguoy" 输出：true 解释：串联数组 words 中每个字符串的第一个字符，得到字符串 "ngguoy" 。 因此，s = "ngguoy" 是首字母缩略词。 提示： * 1 <= words.length <= 100 * 1 <= words[i].length <= 10 * 1 <= s.length <= 100 * words[i] 和 s 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 检查字符串 s 是否等于 words 中每个字符串的第一个字符的串联。

算法步骤:
1. 初始化一个空字符串 result。
2. 遍历 words 数组，将每个字符串的第一个字符添加到 result 中。
3. 比较 result 和 s 是否相等，如果相等则返回 True，否则返回 False。

关键点:
- 通过遍历 words 数组并提取每个字符串的第一个字符来构建结果字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 words 数组的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_acronym(words: List[str], s: str) -> bool:
    """
    函数式接口 - 判断字符串 s 是否是 words 的首字母缩略词
    """
    # 构建结果字符串
    result = ''.join(word[0] for word in words)
    
    # 比较结果字符串和 s
    return result == s


Solution = create_solution(is_acronym)