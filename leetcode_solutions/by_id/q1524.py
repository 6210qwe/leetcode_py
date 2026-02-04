# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1524
标题: String Matching in an Array
难度: easy
链接: https://leetcode.cn/problems/string-matching-in-an-array/
题目类型: 数组、字符串、字符串匹配
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1408. 数组中的字符串匹配 - 给你一个字符串数组 words ，数组中的每个字符串都可以看作是一个单词。请你按 任意 顺序返回 words 中是其他单词的 子字符串 的所有单词。 示例 1： 输入：words = ["mass","as","hero","superhero"] 输出：["as","hero"] 解释："as" 是 "mass" 的子字符串，"hero" 是 "superhero" 的子字符串。 ["hero","as"] 也是有效的答案。 示例 2： 输入：words = ["leetcode","et","code"] 输出：["et","code"] 解释："et" 和 "code" 都是 "leetcode" 的子字符串。 示例 3： 输入：words = ["blue","green","bu"] 输出：[] 提示： * 1 <= words.length <= 100 * 1 <= words[i].length <= 30 * words[i] 仅包含小写英文字母。 * 题目数据 保证 words 的每个字符串都是独一无二的。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双重循环来检查每个字符串是否是其他字符串的子字符串。

算法步骤:
1. 初始化一个空列表 `result` 用于存储结果。
2. 对于每个字符串 `word`，检查它是否是其他字符串的子字符串。
3. 如果是，则将其添加到 `result` 列表中。
4. 返回 `result` 列表。

关键点:
- 使用 Python 的 `in` 操作符来检查子字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 * m)，其中 n 是 words 的长度，m 是 words 中最长字符串的长度。
空间复杂度: O(1)，除了输入和输出外，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(words: List[str]) -> List[str]:
    """
    函数式接口 - 实现最优解法
    """
    result = []
    for i, word in enumerate(words):
        for j, other_word in enumerate(words):
            if i != j and word in other_word:
                result.append(word)
                break
    return result


Solution = create_solution(solution_function_name)