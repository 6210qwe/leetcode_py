# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100259
标题: Words Frequency LCCI
难度: medium
链接: https://leetcode.cn/problems/words-frequency-lcci/
题目类型: 设计、字典树、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 16.02. 单词频率 - 设计一个方法，找出任意指定单词在一本书中的出现频率。 你的实现应该支持如下操作： * WordsFrequency(book)构造函数，参数为字符串数组构成的一本书 * get(word)查询指定单词在书中出现的频率 示例： WordsFrequency wordsFrequency = new WordsFrequency({"i", "have", "an", "apple", "he", "have", "a", "pen"}); wordsFrequency.get("you"); //返回0，"you"没有出现过 wordsFrequency.get("have"); //返回2，"have"出现2次 wordsFrequency.get("an"); //返回1 wordsFrequency.get("apple"); //返回1 wordsFrequency.get("pen"); //返回1 提示： * book[i]中只包含小写字母 * 1 <= book.length <= 100000 * 1 <= book[i].length <= 10 * get函数的调用次数不会超过100000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表来存储每个单词的频率，这样可以在 O(1) 时间内进行查询。

算法步骤:
1. 在构造函数中，遍历书中的每个单词，并使用哈希表记录每个单词的频率。
2. 在 get 方法中，直接从哈希表中获取指定单词的频率。

关键点:
- 使用哈希表来存储单词频率，以实现高效的查询。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 构造函数的时间复杂度，其中 n 是书中的单词数量。get 方法的时间复杂度是 O(1)。
空间复杂度: O(n) - 哈希表的空间复杂度，其中 n 是书中的单词数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class WordsFrequency:

    def __init__(self, book: List[str]):
        self.word_count = {}
        for word in book:
            if word in self.word_count:
                self.word_count[word] += 1
            else:
                self.word_count[word] = 1

    def get(self, word: str) -> int:
        return self.word_count.get(word, 0)


Solution = create_solution(WordsFrequency)