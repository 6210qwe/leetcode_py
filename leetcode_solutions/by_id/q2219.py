# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2219
标题: Maximum Number of Words Found in Sentences
难度: easy
链接: https://leetcode.cn/problems/maximum-number-of-words-found-in-sentences/
题目类型: 数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2114. 句子中的最多单词数 - 一个 句子 由一些 单词 以及它们之间的单个空格组成，句子的开头和结尾不会有多余空格。 给你一个字符串数组 sentences ，其中 sentences[i] 表示单个 句子 。 请你返回单个句子里 单词的最多数目 。 示例 1： 输入：sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"] 输出：6 解释： - 第一个句子 "alice and bob love leetcode" 总共有 5 个单词。 - 第二个句子 "i think so too" 总共有 4 个单词。 - 第三个句子 "this is great thanks very much" 总共有 6 个单词。 所以，单个句子中有最多单词数的是第三个句子，总共有 6 个单词。 示例 2： 输入：sentences = ["please wait", "continue to fight", "continue to win"] 输出：3 解释：可能有多个句子有相同单词数。 这个例子中，第二个句子和第三个句子（加粗斜体）有相同数目的单词数。 提示： * 1 <= sentences.length <= 100 * 1 <= sentences[i].length <= 100 * sentences[i] 只包含小写英文字母和 ' ' 。 * sentences[i] 的开头和结尾都没有空格。 * sentences[i] 中所有单词由单个空格隔开。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 遍历每个句子，计算每个句子中的单词数，并记录最大值。

算法步骤:
1. 初始化一个变量 `max_words` 为 0，用于记录最大单词数。
2. 遍历每个句子，使用 `split` 方法将句子分割成单词列表，并计算单词数。
3. 更新 `max_words` 为当前句子的单词数和 `max_words` 中的较大值。
4. 返回 `max_words`。

关键点:
- 使用 `split` 方法可以方便地将句子分割成单词列表。
- 通过遍历一次句子数组，可以在 O(n) 时间复杂度内解决问题。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是句子的数量，m 是每个句子的平均长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_number_of_words(sentences: List[str]) -> int:
    """
    函数式接口 - 计算句子中最多单词数
    """
    max_words = 0
    for sentence in sentences:
        word_count = len(sentence.split())
        max_words = max(max_words, word_count)
    return max_words


Solution = create_solution(max_number_of_words)