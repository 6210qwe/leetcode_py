# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2580
标题: Circular Sentence
难度: easy
链接: https://leetcode.cn/problems/circular-sentence/
题目类型: 字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2490. 回环句 - 句子 是由单个空格分隔的一组单词，且不含前导或尾随空格。 * 例如，"Hello World"、"HELLO"、"hello world hello world" 都是符合要求的句子。 单词 仅 由大写和小写英文字母组成。且大写和小写字母会视作不同字符。 如果句子满足下述全部条件，则认为它是一个 回环句 ： * 句子中每个单词的最后一个字符等于下一个单词的第一个字符。 * 最后一个单词的最后一个字符和第一个单词的第一个字符相等。 例如，"leetcode exercises sound delightful"、"eetcode"、"leetcode eats soul" 都是回环句。然而，"Leetcode is cool"、"happy Leetcode"、"Leetcode" 和 "I like Leetcode" 都 不 是回环句。 给你一个字符串 sentence ，请你判断它是不是一个回环句。如果是，返回 true ；否则，返回 false 。 示例 1： 输入：sentence = "leetcode exercises sound delightful" 输出：true 解释：句子中的单词是 ["leetcode", "exercises", "sound", "delightful"] 。 - leetcode 的最后一个字符和 exercises 的第一个字符相等。 - exercises 的最后一个字符和 sound 的第一个字符相等。 - sound 的最后一个字符和 delightful 的第一个字符相等。 - delightful 的最后一个字符和 leetcode 的第一个字符相等。 这个句子是回环句。 示例 2： 输入：sentence = "eetcode" 输出：true 解释：句子中的单词是 ["eetcode"] 。 - eetcode 的最后一个字符和 eetcode 的第一个字符相等。 这个句子是回环句。 示例 3： 输入：sentence = "Leetcode is cool" 输出：false 解释：句子中的单词是 ["Leetcode", "is", "cool"] 。 - Leetcode 的最后一个字符和 is 的第一个字符 不 相等。 这个句子 不 是回环句。 提示： * 1 <= sentence.length <= 500 * sentence 仅由大小写英文字母和空格组成 * sentence 中的单词由单个空格进行分隔 * 不含任何前导或尾随空格
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 检查每个单词的最后一个字符是否与下一个单词的第一个字符相同，并检查最后一个单词的最后一个字符是否与第一个单词的第一个字符相同。

算法步骤:
1. 将句子按空格分割成单词列表。
2. 遍历单词列表，检查每个单词的最后一个字符是否与下一个单词的第一个字符相同。
3. 检查最后一个单词的最后一个字符是否与第一个单词的第一个字符相同。

关键点:
- 使用 `split` 方法将句子分割成单词列表。
- 通过遍历和比较相邻单词的字符来验证回环条件。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是句子的长度。我们需要遍历整个句子一次。
空间复杂度: O(1)，我们只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_circular_sentence(sentence: str) -> bool:
    """
    判断给定的句子是否为回环句。
    
    :param sentence: 输入的句子
    :return: 是否为回环句
    """
    words = sentence.split()
    n = len(words)
    
    # 检查每个单词的最后一个字符是否与下一个单词的第一个字符相同
    for i in range(n):
        if words[i][-1] != words[(i + 1) % n][0]:
            return False
    
    return True


Solution = create_solution(is_circular_sentence)