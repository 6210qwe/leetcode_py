# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2594
标题: Count Pairs Of Similar Strings
难度: easy
链接: https://leetcode.cn/problems/count-pairs-of-similar-strings/
题目类型: 位运算、数组、哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2506. 统计相似字符串对的数目 - 给你一个下标从 0 开始的字符串数组 words 。 如果两个字符串由相同的字符组成，则认为这两个字符串 相似 。 * 例如，"abca" 和 "cba" 相似，因为它们都由字符 'a'、'b'、'c' 组成。 * 然而，"abacba" 和 "bcfd" 不相似，因为它们不是相同字符组成的。 请你找出满足字符串 words[i] 和 words[j] 相似的下标对 (i, j) ，并返回下标对的数目，其中 0 <= i < j <= words.length - 1 。 示例 1： 输入：words = ["aba","aabb","abcd","bac","aabc"] 输出：2 解释：共有 2 对满足条件： - i = 0 且 j = 1 ：words[0] 和 words[1] 只由字符 'a' 和 'b' 组成。 - i = 3 且 j = 4 ：words[3] 和 words[4] 只由字符 'a'、'b' 和 'c' 。 示例 2： 输入：words = ["aabb","ab","ba"] 输出：3 解释：共有 3 对满足条件： - i = 0 且 j = 1 ：words[0] 和 words[1] 只由字符 'a' 和 'b' 组成。 - i = 0 且 j = 2 ：words[0] 和 words[2] 只由字符 'a' 和 'b' 组成。 - i = 1 且 j = 2 ：words[1] 和 words[2] 只由字符 'a' 和 'b' 组成。 示例 3： 输入：words = ["nba","cba","dba"] 输出：0 解释：不存在满足条件的下标对，返回 0 。 提示： * 1 <= words.length <= 100 * 1 <= words[i].length <= 100 * words[i] 仅由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用位掩码来表示每个字符串的字符集，并使用哈希表来统计每个字符集出现的次数。

算法步骤:
1. 初始化一个哈希表 `char_mask_count` 来记录每种字符集出现的次数。
2. 遍历每个字符串，计算其字符集的位掩码。
3. 将位掩码作为键存储在哈希表中，并更新其计数。
4. 计算所有字符集的组合数，累加到结果中。

关键点:
- 使用位掩码来表示字符集，可以高效地进行比较。
- 使用哈希表来统计每种字符集的出现次数，可以快速查找和更新。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是字符串数组的长度，m 是每个字符串的最大长度。
空间复杂度: O(n)，哈希表的空间复杂度为 O(n)。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_similar_pairs(words: List[str]) -> int:
    """
    函数式接口 - 统计相似字符串对的数目
    """
    def get_char_mask(word: str) -> int:
        mask = 0
        for char in word:
            mask |= 1 << (ord(char) - ord('a'))
        return mask

    char_mask_count = {}
    result = 0

    for word in words:
        mask = get_char_mask(word)
        if mask in char_mask_count:
            result += char_mask_count[mask]
            char_mask_count[mask] += 1
        else:
            char_mask_count[mask] = 1

    return result


Solution = create_solution(count_similar_pairs)