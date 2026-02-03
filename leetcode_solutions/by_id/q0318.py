# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 318
标题: Maximum Product of Word Lengths
难度: medium
链接: https://leetcode.cn/problems/maximum-product-of-word-lengths/
题目类型: 位运算、数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
318. 最大单词长度乘积 - 给你一个字符串数组 words ，找出并返回 length(words[i]) * length(words[j]) 的最大值，并且这两个单词不含有公共字母。如果不存在这样的两个单词，返回 0 。 示例 1： 输入：words = ["abcw","baz","foo","bar","xtfn","abcdef"] 输出：16 解释：这两个单词为 "abcw", "xtfn"。 示例 2： 输入：words = ["a","ab","abc","d","cd","bcd","abcd"] 输出：4 解释：这两个单词为 "ab", "cd"。 示例 3： 输入：words = ["a","aa","aaa","aaaa"] 输出：0 解释：不存在这样的两个单词。 提示： * 2 <= words.length <= 1000 * 1 <= words[i].length <= 1000 * words[i] 仅包含小写字母
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用位掩码表示每个单词包含的字母，然后检查两个单词是否有公共字母

算法步骤:
1. 为每个单词计算位掩码，如果包含字母c，则设置第(c-'a')位
2. 枚举所有单词对，如果两个单词的位掩码按位与为0，说明没有公共字母
3. 计算长度乘积的最大值

关键点:
- 使用位运算快速判断是否有公共字母
- 时间复杂度O(n^2)，空间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - n为单词数量
空间复杂度: O(n) - 位掩码数组空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def maximum_product_of_word_lengths(words: List[str]) -> int:
    """
    函数式接口 - 最大单词长度乘积
    
    实现思路:
    使用位掩码表示每个单词包含的字母，然后检查两个单词是否有公共字母。
    
    Args:
        words: 字符串数组
        
    Returns:
        两个不含有公共字母的单词的长度乘积最大值
        
    Example:
        >>> maximum_product_of_word_lengths(["abcw","baz","foo","bar","xtfn","abcdef"])
        16
    """
    n = len(words)
    masks = []
    
    # 计算每个单词的位掩码
    for word in words:
        mask = 0
        for char in word:
            mask |= 1 << (ord(char) - ord('a'))
        masks.append(mask)
    
    max_product = 0
    for i in range(n):
        for j in range(i + 1, n):
            # 如果两个单词没有公共字母
            if masks[i] & masks[j] == 0:
                max_product = max(max_product, len(words[i]) * len(words[j]))
    
    return max_product


# 自动生成Solution类（无需手动编写）
Solution = create_solution(maximum_product_of_word_lengths)
