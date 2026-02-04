# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 749
标题: Shortest Completing Word
难度: easy
链接: https://leetcode.cn/problems/shortest-completing-word/
题目类型: 数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
748. 最短补全词 - 给你一个字符串 licensePlate 和一个字符串数组 words ，请你找出 words 中的 最短补全词 。 补全词 是一个包含 licensePlate 中所有字母的单词。忽略 licensePlate 中的 数字和空格 。不区分大小写。如果某个字母在 licensePlate 中出现不止一次，那么该字母在补全词中的出现次数应当一致或者更多。 例如：licensePlate = "aBc 12c"，那么它的补全词应当包含字母 'a'、'b' （忽略大写）和两个 'c' 。可能的 补全词 有 "abccdef"、"caaacab" 以及 "cbca" 。 请返回 words 中的 最短补全词 。题目数据保证一定存在一个最短补全词。当有多个单词都符合最短补全词的匹配条件时取 words 中 第一个 出现的那个。 示例 1： 输入：licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"] 输出："steps" 解释：最短补全词应该包括 "s"、"p"、"s"（忽略大小写） 以及 "t"。 "step" 包含 "t"、"p"，但只包含一个 "s"，所以它不符合条件。 "steps" 包含 "t"、"p" 和两个 "s"。 "stripe" 缺一个 "s"。 "stepple" 缺一个 "s"。 因此，"steps" 是唯一一个包含所有字母的单词，也是本例的答案。 示例 2： 输入：licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"] 输出："pest" 解释：licensePlate 只包含字母 "s" 。所有的单词都包含字母 "s" ，其中 "pest"、"stew"、和 "show" 三者最短。答案是 "pest" ，因为它是三个单词中在 words 里最靠前的那个。 提示： * 1 <= licensePlate.length <= 7 * licensePlate 由数字、大小写字母或空格 ' ' 组成 * 1 <= words.length <= 1000 * 1 <= words[i].length <= 15 * words[i] 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表统计 `licensePlate` 中的字母频率，然后遍历 `words`，找到第一个满足条件的最短补全词。

算法步骤:
1. 统计 `licensePlate` 中的字母频率。
2. 遍历 `words`，对于每个单词，检查其是否包含 `licensePlate` 中的所有字母且频率不低于 `licensePlate` 中的频率。
3. 如果满足条件，更新当前最短补全词。
4. 返回最短补全词。

关键点:
- 使用 `collections.Counter` 来统计字母频率。
- 使用 `all` 函数来检查单词是否满足条件。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 `words` 的长度，m 是单词的平均长度。
空间复杂度: O(1)，因为字母表的大小是固定的。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import Counter

def shortest_completing_word(license_plate: str, words: List[str]) -> str:
    """
    找出 words 中的最短补全词。
    """
    # 统计 licensePlate 中的字母频率
    license_counter = Counter(c.lower() for c in license_plate if c.isalpha())
    
    # 初始化最短补全词
    shortest_word = None
    
    # 遍历 words
    for word in words:
        word_counter = Counter(word)
        # 检查 word 是否包含 licensePlate 中的所有字母且频率不低于 licensePlate 中的频率
        if all(word_counter[letter] >= count for letter, count in license_counter.items()):
            if shortest_word is None or len(word) < len(shortest_word):
                shortest_word = word
    
    return shortest_word

Solution = create_solution(shortest_completing_word)