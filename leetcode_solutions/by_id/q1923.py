# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1923
标题: Sentence Similarity III
难度: medium
链接: https://leetcode.cn/problems/sentence-similarity-iii/
题目类型: 数组、双指针、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1813. 句子相似性 III - 给定两个字符串 sentence1 和 sentence2，每个表示由一些单词组成的一个句子。句子是一系列由 单个 空格分隔的 单词，且开头和结尾没有多余空格。每个单词都只包含大写和小写英文字母。 如果两个句子 s1 和 s2 ，可以通过往其中一个句子插入一个任意的句子（可以是空句子）而得到另一个句子，那么我们称这两个句子是 相似的 。注意，插入的句子必须与现有单词用空白隔开。 比方说， * s1 = "Hello Jane" 与 s2 = "Hello my name is Jane"，我们可以往 s1 中 "Hello" 和 "Jane" 之间插入 "my name is" 得到 s2 。 * s1 = "Frog cool" 与 s2 = "Frogs are cool" 不是相似的，因为尽管往 s1 中插入 "s are"，它没有与 "Frog" 用空格隔开。 给你两个句子 sentence1 和 sentence2 ，如果 sentence1 和 sentence2 是 相似 的，请你返回 true ，否则返回 false 。 示例 1： 输入：sentence1 = "My name is Haley", sentence2 = "My Haley" 输出：true 解释：可以往 sentence2 中 "My" 和 "Haley" 之间插入 "name is" ，得到 sentence1 。 示例 2： 输入：sentence1 = "of", sentence2 = "A lot of words" 输出：false 解释：没法往这两个句子中的一个句子只插入一个句子就得到另一个句子。 示例 3： 输入：sentence1 = "Eating right now", sentence2 = "Eating" 输出：true 解释：可以往 sentence2 的结尾插入 "right now" 得到 sentence1 。 提示： * 1 <= sentence1.length, sentence2.length <= 100 * sentence1 和 sentence2 都只包含大小写英文字母和空格。 * sentence1 和 sentence2 中的单词都只由单个空格隔开。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针方法比较两个句子的单词，确保在插入一个句子后能够匹配。

算法步骤:
1. 将两个句子分别按空格分割成单词列表。
2. 使用双指针遍历两个单词列表，确保在插入一个句子后能够匹配。
3. 如果两个指针都能到达各自列表的末尾，则说明两个句子是相似的。

关键点:
- 使用双指针方法可以有效地比较两个句子的单词，时间复杂度为 O(n)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是较长句子的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def are_sentences_similar(sentence1: str, sentence2: str) -> bool:
    """
    判断两个句子是否相似
    """
    words1 = sentence1.split()
    words2 = sentence2.split()

    i, j = 0, 0
    while i < len(words1) and j < len(words2) and words1[i] == words2[j]:
        i += 1
        j += 1

    # 如果两个指针都到达了各自列表的末尾，说明完全匹配
    if i == len(words1) and j == len(words2):
        return True

    # 从末尾开始比较
    while i < len(words1) and j < len(words2) and words1[-i-1] == words2[-j-1]:
        i += 1
        j += 1

    return i == len(words1) or j == len(words2)


Solution = create_solution(are_sentences_similar)