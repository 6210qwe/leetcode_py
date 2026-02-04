# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1282
标题: Number of Valid Words for Each Puzzle
难度: hard
链接: https://leetcode.cn/problems/number-of-valid-words-for-each-puzzle/
题目类型: 位运算、字典树、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1178. 猜字谜 - 外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。 字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底： * 单词 word 中包含谜面 puzzle 的第一个字母。 * 单词 word 中的每一个字母都可以在谜面 puzzle 中找到。 例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）都不能作为谜底。 返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜底的单词数目。 示例： 输入： words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"] 输出：[1,1,3,2,4,0] 解释： 1 个单词可以作为 "aboveyz" 的谜底 : "aaaa" 1 个单词可以作为 "abrodyz" 的谜底 : "aaaa" 3 个单词可以作为 "abslute" 的谜底 : "aaaa", "asas", "able" 2 个单词可以作为 "absoryz" 的谜底 : "aaaa", "asas" 4 个单词可以作为 "actresz" 的谜底 : "aaaa", "asas", "actt", "access" 没有单词可以作为 "gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。 提示： * 1 <= words.length <= 10^5 * 4 <= words[i].length <= 50 * 1 <= puzzles.length <= 10^4 * puzzles[i].length == 7 * words[i][j], puzzles[i][j] 都是小写英文字母。 * 每个 puzzles[i] 所包含的字符都不重复。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用位掩码和哈希表来高效地解决这个问题。

算法步骤:
1. 将每个单词转换为一个位掩码，表示其包含的字母。
2. 将每个谜面的第一个字母和其余字母分别转换为位掩码。
3. 使用哈希表统计每个位掩码出现的次数。
4. 对于每个谜面，计算所有可能的子集，并检查这些子集在哈希表中的计数。

关键点:
- 使用位掩码表示字母集合，可以高效地进行集合操作。
- 通过哈希表统计位掩码的频率，可以在 O(1) 时间内查询。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m * 2^6)，其中 n 是 words 的长度，m 是 puzzles 的长度。每个谜面最多有 2^6 个子集。
空间复杂度: O(n)，用于存储哈希表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from collections import Counter

def find_num_of_valid_words(words: List[str], puzzles: List[str]) -> List[int]:
    def get_mask(word: str) -> int:
        mask = 0
        for char in word:
            mask |= 1 << (ord(char) - ord('a'))
        return mask

    # 统计每个单词的位掩码
    word_count = Counter(get_mask(word) for word in words)

    result = []
    for puzzle in puzzles:
        first_char = puzzle[0]
        rest = puzzle[1:]
        rest_mask = get_mask(rest)
        submasks = [rest_mask]

        # 生成 rest 的所有子集
        x = rest_mask
        while x:
            submasks.append(x)
            x = (x - 1) & rest_mask

        count = 0
        for submask in submasks:
            count += word_count[submask | (1 << (ord(first_char) - ord('a')))]
        result.append(count)

    return result

Solution = create_solution(find_num_of_valid_words)