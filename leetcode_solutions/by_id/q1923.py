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
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
