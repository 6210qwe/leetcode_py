# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 952
标题: Word Subsets
难度: medium
链接: https://leetcode.cn/problems/word-subsets/
题目类型: 数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
916. 单词子集 - 给你两个字符串数组 words1 和 words2。 现在，如果 b 中的每个字母都出现在 a 中，包括重复出现的字母，那么称字符串 b 是字符串 a 的 子集 。 * 例如，"wrr" 是 "warrior" 的子集，但不是 "world" 的子集。 如果对 words2 中的每一个单词 b，b 都是 a 的子集，那么我们称 words1 中的单词 a 是 通用单词 。 以数组形式返回 words1 中所有的 通用 单词。你可以按 任意顺序 返回答案。 示例 1： 输入：words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"] 输出：["facebook","google","leetcode"] 示例 2： 输入：words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"] 输出：["leetcode"] 示例 3： 输入：words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"] 输出：["cccbb"] 提示： * 1 <= words1.length, words2.length <= 104 * 1 <= words1[i].length, words2[i].length <= 10 * words1[i] 和 words2[i] 仅由小写英文字母组成 * words1 中的所有字符串 互不相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个计数器来记录 words2 中所有单词的最大字符频率，然后检查 words1 中的每个单词是否满足这些频率要求。

算法步骤:
1. 计算 words2 中所有单词的最大字符频率。
2. 遍历 words1 中的每个单词，检查其字符频率是否满足 words2 中的最大字符频率要求。
3. 将满足条件的单词加入结果列表。

关键点:
- 使用 Counter 来统计字符频率。
- 通过遍历和比较字符频率来判断是否为通用单词。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 words1 的长度，m 是 words2 的长度。
空间复杂度: O(1)，因为字符频率计数器的大小是固定的（26 个字母）。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import Counter

def word_subsets(words1: List[str], words2: List[str]) -> List[str]:
    # 计算 words2 中所有单词的最大字符频率
    max_count = Counter()
    for word in words2:
        word_count = Counter(word)
        for char, count in word_count.items():
            max_count[char] = max(max_count[char], count)
    
    # 检查 words1 中的每个单词是否满足最大字符频率要求
    result = []
    for word in words1:
        word_count = Counter(word)
        if all(word_count[char] >= max_count[char] for char in max_count):
            result.append(word)
    
    return result

Solution = create_solution(word_subsets)