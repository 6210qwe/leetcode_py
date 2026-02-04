# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 827
标题: Expressive Words
难度: medium
链接: https://leetcode.cn/problems/expressive-words/
题目类型: 数组、双指针、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
809. 情感丰富的文字 - 有时候人们会用重复写一些字母来表示额外的感受，比如 "hello" -> "heeellooo", "hi" -> "hiii"。我们将相邻字母都相同的一串字符定义为相同字母组，例如："h", "eee", "ll", "ooo"。 对于一个给定的字符串 S ，如果另一个单词能够通过将一些字母组扩张从而使其和 S 相同，我们将这个单词定义为可扩张的（stretchy）。扩张操作定义如下：选择一个字母组（包含字母 c ），然后往其中添加相同的字母 c 使其长度达到 3 或以上。 例如，以 "hello" 为例，我们可以对字母组 "o" 扩张得到 "hellooo"，但是无法以同样的方法得到 "helloo" 因为字母组 "oo" 长度小于 3。此外，我们可以进行另一种扩张 "ll" -> "lllll" 以获得 "helllllooo"。如果 s = "helllllooo"，那么查询词 "hello" 是可扩张的，因为可以对它执行这两种扩张操作使得 query = "hello" -> "hellooo" -> "helllllooo" = s。 输入一组查询单词，输出其中可扩张的单词数量。 示例： 输入： s = "heeellooo" words = ["hello", "hi", "helo"] 输出：1 解释： 我们能通过扩张 "hello" 的 "e" 和 "o" 来得到 "heeellooo"。 我们不能通过扩张 "helo" 来得到 "heeellooo" 因为 "ll" 的长度小于 3 。 提示： * 1 <= s.length, words.length <= 100 * 1 <= words[i].length <= 100 * s 和所有在 words 中的单词都只由小写字母组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针遍历字符串，比较每个字母组的长度是否满足扩张条件。

算法步骤:
1. 定义一个辅助函数 `group`，用于生成字符串中每个字母组及其长度。
2. 遍历每个查询单词，使用双指针逐个比较字母组。
3. 如果当前字母组不匹配，返回 False。
4. 如果当前字母组匹配但长度不满足扩张条件，返回 False。
5. 如果所有字母组都匹配且满足扩张条件，计数器加一。

关键点:
- 使用双指针遍历字符串，比较每个字母组的长度。
- 确保扩展后的字母组长度至少为 3。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是查询单词的数量，m 是每个单词的平均长度。
空间复杂度: O(1)，只需要常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def expressive_words(s: str, words: List[str]) -> int:
    def group(word):
        i = 0
        while i < len(word):
            count = 1
            while i + 1 < len(word) and word[i] == word[i + 1]:
                i += 1
                count += 1
            yield word[i], count
            i += 1
    
    def is_stretchy(s, word):
        s_groups = group(s)
        word_groups = group(word)
        
        for (s_char, s_count), (word_char, word_count) in zip(s_groups, word_groups):
            if s_char != word_char or (s_count < word_count) or (s_count < 3 and s_count != word_count):
                return False
        return next(s_groups, None) is None and next(word_groups, None) is None
    
    return sum(is_stretchy(s, word) for word in words)

Solution = create_solution(expressive_words)