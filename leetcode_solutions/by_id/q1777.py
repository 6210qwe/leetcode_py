# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1777
标题: Determine if Two Strings Are Close
难度: medium
链接: https://leetcode.cn/problems/determine-if-two-strings-are-close/
题目类型: 哈希表、字符串、计数、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1657. 确定两个字符串是否接近 - 如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 接近 ： * 操作 1：交换任意两个 现有 字符。 * 例如，abcde -> aecdb * 操作 2：将一个 现有 字符的每次出现转换为另一个 现有 字符，并对另一个字符执行相同的操作。 * 例如，aacabb -> bbcbaa（所有 a 转化为 b ，而所有的 b 转换为 a ） 你可以根据需要对任意一个字符串多次使用这两种操作。 给你两个字符串，word1 和 word2 。如果 word1 和 word2 接近 ，就返回 true ；否则，返回 false 。 示例 1： 输入：word1 = "abc", word2 = "bca" 输出：true 解释：2 次操作从 word1 获得 word2 。 执行操作 1："abc" -> "acb" 执行操作 1："acb" -> "bca" 示例 2： 输入：word1 = "a", word2 = "aa" 输出：false 解释：不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。 示例 3： 输入：word1 = "cabbba", word2 = "abbccc" 输出：true 解释：3 次操作从 word1 获得 word2 。 执行操作 1："cabbba" -> "caabbb" 执行操作 2："caabbb" -> "baaccc" 执行操作 2："baaccc" -> "abbccc" 提示： * 1 <= word1.length, word2.length <= 105 * word1 和 word2 仅包含小写英文字母
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 两个字符串接近的条件是它们包含相同的字符集，并且每个字符的频率分布相同。

算法步骤:
1. 检查两个字符串的长度是否相等，如果不等则直接返回 False。
2. 使用 Counter 计算两个字符串中每个字符的频率。
3. 比较两个字符串的字符集是否相同。
4. 比较两个字符串的字符频率分布是否相同。

关键点:
- 使用 Counter 来统计字符频率和字符集。
- 比较字符集和频率分布。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是字符串的长度。Counter 的操作是 O(n)，排序操作是 O(n log n)。
空间复杂度: O(n)，用于存储 Counter 的结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from collections import Counter


def close_strings(word1: str, word2: str) -> bool:
    """
    函数式接口 - 判断两个字符串是否接近
    """
    # 检查两个字符串的长度是否相等
    if len(word1) != len(word2):
        return False
    
    # 使用 Counter 计算两个字符串中每个字符的频率
    counter1 = Counter(word1)
    counter2 = Counter(word2)
    
    # 比较两个字符串的字符集是否相同
    if set(counter1.keys()) != set(counter2.keys()):
        return False
    
    # 比较两个字符串的字符频率分布是否相同
    if sorted(counter1.values()) != sorted(counter2.values()):
        return False
    
    return True


Solution = create_solution(close_strings)