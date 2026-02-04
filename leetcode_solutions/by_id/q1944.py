# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1944
标题: Truncate Sentence
难度: easy
链接: https://leetcode.cn/problems/truncate-sentence/
题目类型: 数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1816. 截断句子 - 句子 是一个单词列表，列表中的单词之间用单个空格隔开，且不存在前导或尾随空格。每个单词仅由大小写英文字母组成（不含标点符号）。 * 例如，"Hello World"、"HELLO" 和 "hello world hello world" 都是句子。 给你一个句子 s 和一个整数 k ，请你将 s 截断 ， 使截断后的句子仅含 前 k 个单词。返回 截断 s 后得到的句子。 示例 1： 输入：s = "Hello how are you Contestant", k = 4 输出："Hello how are you" 解释： s 中的单词为 ["Hello", "how" "are", "you", "Contestant"] 前 4 个单词为 ["Hello", "how", "are", "you"] 因此，应当返回 "Hello how are you" 示例 2： 输入：s = "What is the solution to this problem", k = 4 输出："What is the solution" 解释： s 中的单词为 ["What", "is" "the", "solution", "to", "this", "problem"] 前 4 个单词为 ["What", "is", "the", "solution"] 因此，应当返回 "What is the solution" 示例 3： 输入：s = "chopper is not a tanuki", k = 5 输出："chopper is not a tanuki" 提示： * 1 <= s.length <= 500 * k 的取值范围是 [1, s 中单词的数目] * s 仅由大小写英文字母和空格组成 * s 中的单词之间由单个空格隔开 * 不存在前导或尾随空格
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过遍历字符串并计数空格来找到前 k 个单词的结束位置。

算法步骤:
1. 初始化一个计数器 `count` 用于记录遇到的空格数。
2. 遍历字符串 `s`，每遇到一个空格就增加 `count`。
3. 当 `count` 达到 `k` 时，记录当前索引位置 `end_index`。
4. 返回从开始到 `end_index` 的子字符串。

关键点:
- 使用单次遍历来减少时间复杂度。
- 通过记录空格数来确定截断位置。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 s 的长度。最坏情况下需要遍历整个字符串。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def truncate_sentence(s: str, k: int) -> str:
    """
    函数式接口 - 截断句子
    """
    count = 0
    end_index = 0
    
    for i, char in enumerate(s):
        if char == ' ':
            count += 1
            if count == k:
                end_index = i
                break
    else:
        # 如果没有提前退出循环，说明 k 等于单词总数
        end_index = len(s)
    
    return s[:end_index]


Solution = create_solution(truncate_sentence)