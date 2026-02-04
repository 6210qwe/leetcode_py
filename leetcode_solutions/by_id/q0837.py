# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 837
标题: Most Common Word
难度: easy
链接: https://leetcode.cn/problems/most-common-word/
题目类型: 数组、哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
819. 最常见的单词 - 给你一个字符串 paragraph 和一个表示禁用词的字符串数组 banned ，返回出现频率最高的非禁用词。题目数据 保证 至少存在一个非禁用词，且答案 唯一 。 paragraph 中的单词 不区分大小写 ，答案应以 小写 形式返回。 注意 单词不包含标点符号。 示例 1： 输入：paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"] 输出："ball" 解释： "hit" 出现了 3 次，但它是禁用词。 "ball" 出现了两次（没有其他单词出现这么多次），因此它是段落中出现频率最高的非禁用词。 请注意，段落中的单词不区分大小写， 标点符号会被忽略（即使它们紧挨着单词，如 "ball,"）， 并且尽管 "hit" 出现的次数更多，但它不能作为答案，因为它是禁用词。 示例 2： 输入：paragraph = "a.", banned = [] 输出："a" 提示： * 1 <= paragraph.length <= 1000 * paragraph 由英文字母、空格 ' '、和以下符号组成："!?',;." * 0 <= banned.length <= 100 * 1 <= banned[i].length <= 10 * banned[i] 仅由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表统计每个单词的出现频率，并过滤掉禁用词，找到出现频率最高的非禁用词。

算法步骤:
1. 将段落中的所有字符转换为小写。
2. 使用正则表达式提取所有单词。
3. 使用哈希表统计每个单词的出现频率。
4. 过滤掉禁用词。
5. 找到出现频率最高的非禁用词。

关键点:
- 使用正则表达式处理标点符号。
- 使用哈希表进行频率统计。
- 过滤禁用词并找到最大频率的单词。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 paragraph 的长度，m 是 banned 的长度。
空间复杂度: O(n + m)，用于存储单词频率和禁用词集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
import re
from collections import Counter
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def most_common_word(paragraph: str, banned: List[str]) -> str:
    """
    返回出现频率最高的非禁用词。
    """
    # 将段落中的所有字符转换为小写
    paragraph = paragraph.lower()
    
    # 使用正则表达式提取所有单词
    words = re.findall(r'\b\w+\b', paragraph)
    
    # 使用哈希表统计每个单词的出现频率
    word_count = Counter(words)
    
    # 过滤掉禁用词
    for ban in banned:
        if ban in word_count:
            del word_count[ban]
    
    # 找到出现频率最高的非禁用词
    return max(word_count, key=word_count.get)


Solution = create_solution(most_common_word)