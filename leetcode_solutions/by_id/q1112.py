# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1112
标题: Find Words That Can Be Formed by Characters
难度: easy
链接: https://leetcode.cn/problems/find-words-that-can-be-formed-by-characters/
题目类型: 数组、哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1160. 拼写单词 - 给定一个字符串数组 words 和一个字符串 chars。 如果字符串可以由 chars 中的字符组成（每个字符在 每个 words 中只能使用一次），则认为它是好的。 返回 words 中所有好的字符串的长度之和。 示例 1： 输入：words = ["cat","bt","hat","tree"], chars = "atach" 输出：6 解释： 可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。 示例 2： 输入：words = ["hello","world","leetcode"], chars = "welldonehoneyr" 输出：10 解释： 可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。 提示： * 1 <= words.length <= 1000 * 1 <= words[i].length, chars.length <= 100 * words[i] 和 chars 中都仅包含小写英文字母
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录 chars 中每个字符的出现次数，然后遍历每个 word，检查其是否可以由 chars 中的字符组成。

算法步骤:
1. 使用 Counter 计算 chars 中每个字符的出现次数。
2. 遍历每个 word，使用 Counter 计算 word 中每个字符的出现次数。
3. 对于每个 word，检查其字符出现次数是否不超过 chars 中的字符出现次数。
4. 如果满足条件，则将 word 的长度累加到结果中。

关键点:
- 使用 Counter 进行字符计数，简化了字符频率的比较。
- 通过遍历和计数，确保每个 word 的字符都在 chars 中且数量足够。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 chars 的长度，m 是 words 中所有字符串的总长度。
空间复杂度: O(1)，因为只使用了常数级的额外空间（字母表大小固定为 26）。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import Counter

def count_characters(words: List[str], chars: str) -> int:
    """
    函数式接口 - 计算可以由 chars 中的字符组成的 words 中所有字符串的长度之和
    """
    # 计算 chars 中每个字符的出现次数
    char_count = Counter(chars)
    
    total_length = 0
    
    for word in words:
        word_count = Counter(word)
        # 检查 word 中每个字符的出现次数是否不超过 chars 中的字符出现次数
        if all(word_count[char] <= char_count[char] for char in word_count):
            total_length += len(word)
    
    return total_length

Solution = create_solution(count_characters)