# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 336
标题: Palindrome Pairs
难度: hard
链接: https://leetcode.cn/problems/palindrome-pairs/
题目类型: 字典树、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
336. 回文对 - 给定一个由唯一字符串构成的 0 索引 数组 words 。 回文对 是一对整数 (i, j) ，满足以下条件： * 0 <= i, j < words.length， * i != j ，并且 * words[i] + words[j]（两个字符串的连接）是一个回文串。 返回一个数组，它包含 words 中所有满足 回文对 条件的字符串。 你必须设计一个时间复杂度为 O(sum of words[i].length) 的算法。 示例 1： 输入：words = ["abcd","dcba","lls","s","sssll"] 输出：[[0,1],[1,0],[3,2],[2,4]] 解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"] 示例 2： 输入：words = ["bat","tab","cat"] 输出：[[0,1],[1,0]] 解释：可拼接成的回文串为 ["battab","tabbat"] 示例 3： 输入：words = ["a",""] 输出：[[0,1],[1,0]] 提示： * 1 <= words.length <= 5000 * 0 <= words[i].length <= 300 * words[i] 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 哈希表存储字符串，检查拼接后的回文

算法步骤:
1. 使用哈希表存储每个字符串的索引
2. 对于每个字符串，检查其前缀和后缀
3. 如果前缀是回文，检查剩余部分的反转是否在哈希表中
4. 如果后缀是回文，检查剩余部分的反转是否在哈希表中

关键点:
- 哈希表
- 回文检查
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n*k^2) - n为字符串数，k为平均长度
空间复杂度: O(n) - 哈希表空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def palindrome_pairs(words: List[str]) -> List[List[int]]:
    """
    函数式接口 - 回文对
    
    实现思路:
    哈希表存储字符串，检查拼接后的回文。
    
    Args:
        words: 字符串数组
        
    Returns:
        回文对列表
        
    Example:
        >>> palindrome_pairs(["abcd","dcba","lls","s","sssll"])
        [[0, 1], [1, 0], [3, 2], [2, 4]]
    """
    word_map = {word: i for i, word in enumerate(words)}
    result = []
    
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    
    for i, word in enumerate(words):
        # 检查前缀
        for j in range(len(word) + 1):
            prefix = word[:j]
            suffix = word[j:]
            
            if is_palindrome(prefix):
                reverse_suffix = suffix[::-1]
                if reverse_suffix in word_map and word_map[reverse_suffix] != i:
                    result.append([word_map[reverse_suffix], i])
            
            # 检查后缀（避免重复）
            if j < len(word) and is_palindrome(suffix):
                reverse_prefix = prefix[::-1]
                if reverse_prefix in word_map and word_map[reverse_prefix] != i:
                    result.append([i, word_map[reverse_prefix]])
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(palindrome_pairs)
