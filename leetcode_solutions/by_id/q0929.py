# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 929
标题: Groups of Special-Equivalent Strings
难度: medium
链接: https://leetcode.cn/problems/groups-of-special-equivalent-strings/
题目类型: 数组、哈希表、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
893. 特殊等价字符串组 - 给你一个字符串数组 words。 一步操作中，你可以交换字符串 words[i] 的任意两个偶数下标对应的字符或任意两个奇数下标对应的字符。 对两个字符串 words[i] 和 words[j] 而言，如果经过任意次数的操作，words[i] == words[j] ，那么这两个字符串是 特殊等价 的。 * 例如，words[i] = "zzxy" 和 words[j] = "xyzz" 是一对 特殊等价 字符串，因为可以按 "zzxy" -> "xzzy" -> "xyzz" 的操作路径使 words[i] == words[j] 。 现在规定，words 的 一组特殊等价字符串 就是 words 的一个同时满足下述条件的非空子集： * 该组中的每一对字符串都是 特殊等价 的 * 该组字符串已经涵盖了该类别中的所有特殊等价字符串，容量达到理论上的最大值（也就是说，如果一个字符串不在该组中，那么这个字符串就 不会 与该组内任何字符串特殊等价） 返回 words 中 特殊等价字符串组 的数量。 示例 1： 输入：words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"] 输出：3 解释： 其中一组为 ["abcd", "cdab", "cbad"]，因为它们是成对的特殊等价字符串，且没有其他字符串与这些字符串特殊等价。 另外两组分别是 ["xyzz", "zzxy"] 和 ["zzyx"]。特别需要注意的是，"zzxy" 不与 "zzyx" 特殊等价。 示例 2： 输入：words = ["abc","acb","bac","bca","cab","cba"] 输出：3 解释：3 组 ["abc","cba"]，["acb","bca"]，["bac","cab"] 提示： * 1 <= words.length <= 1000 * 1 <= words[i].length <= 20 * 所有 words[i] 都只由小写字母组成。 * 所有 words[i] 都具有相同的长度。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过将每个字符串的偶数和奇数位置的字符分别排序，生成一个唯一的标识符来表示其特殊等价类。

算法步骤:
1. 对于每个字符串，将其偶数位置的字符和奇数位置的字符分别提取出来并排序。
2. 将排序后的偶数位置字符和奇数位置字符拼接成一个新的字符串，作为该字符串的唯一标识符。
3. 使用一个集合来存储这些唯一标识符，集合的大小即为特殊等价字符串组的数量。

关键点:
- 通过排序和拼接生成唯一标识符，确保相同特殊等价类的字符串具有相同的标识符。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m log m)，其中 n 是字符串数组的长度，m 是每个字符串的最大长度。每个字符串需要进行两次排序，每次排序的时间复杂度为 O(m log m)。
空间复杂度: O(n * m)，用于存储每个字符串的唯一标识符。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def num_special_equiv_groups(words: List[str]) -> int:
    """
    函数式接口 - 计算特殊等价字符串组的数量
    """
    def get_identifier(s: str) -> str:
        even_chars = []
        odd_chars = []
        for i, char in enumerate(s):
            if i % 2 == 0:
                even_chars.append(char)
            else:
                odd_chars.append(char)
        even_chars.sort()
        odd_chars.sort()
        return ''.join(even_chars) + ''.join(odd_chars)

    unique_identifiers = set()
    for word in words:
        identifier = get_identifier(word)
        unique_identifiers.add(identifier)

    return len(unique_identifiers)


Solution = create_solution(num_special_equiv_groups)