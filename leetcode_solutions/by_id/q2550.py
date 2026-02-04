# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2550
标题: Words Within Two Edits of Dictionary
难度: medium
链接: https://leetcode.cn/problems/words-within-two-edits-of-dictionary/
题目类型: 字典树、数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2452. 距离字典两次编辑以内的单词 - 给你两个字符串数组 queries 和 dictionary 。数组中所有单词都只包含小写英文字母，且长度都相同。 一次 编辑 中，你可以从 queries 中选择一个单词，将任意一个字母修改成任何其他字母。从 queries 中找到所有满足以下条件的字符串：不超过 两次编辑内，字符串与 dictionary 中某个字符串相同。 请你返回 queries 中的单词列表，这些单词距离 dictionary 中的单词 编辑次数 不超过 两次 。单词返回的顺序需要与 queries 中原本顺序相同。 示例 1： 输入：queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"] 输出：["word","note","wood"] 解释： - 将 "word" 中的 'r' 换成 'o' ，得到 dictionary 中的单词 "wood" 。 - 将 "note" 中的 'n' 换成 'j' 且将 't' 换成 'k' ，得到 "joke" 。 - "ants" 需要超过 2 次编辑才能得到 dictionary 中的单词。 - "wood" 不需要修改（0 次编辑），就得到 dictionary 中相同的单词。 所以我们返回 ["word","note","wood"] 。 示例 2： 输入：queries = ["yes"], dictionary = ["not"] 输出：[] 解释： "yes" 需要超过 2 次编辑才能得到 "not" 。 所以我们返回空数组。 提示： * 1 <= queries.length, dictionary.length <= 100 * n == queries[i].length == dictionary[j].length * 1 <= n <= 100 * 所有 queries[i] 和 dictionary[j] 都只包含小写英文字母。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双重循环遍历每个查询词和字典中的每个词，并计算它们之间的编辑距离。如果编辑距离不超过2，则将该查询词加入结果列表。

算法步骤:
1. 初始化一个空的结果列表 res。
2. 对于每个查询词 query，遍历字典中的每个词 word。
3. 计算 query 和 word 之间的编辑距离。
4. 如果编辑距离不超过2，则将 query 加入结果列表 res 并跳出当前循环。
5. 返回结果列表 res。

关键点:
- 使用双重循环遍历查询词和字典词。
- 计算编辑距离时，逐字符比较并计数不同字符的数量。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * k)，其中 m 是 queries 的长度，n 是 dictionary 的长度，k 是单词的长度。
空间复杂度: O(1)，除了结果列表外，不使用额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def solution_function_name(queries: List[str], dictionary: List[str]) -> List[str]:
    """
    函数式接口 - 实现
    """
    def edit_distance(word1: str, word2: str) -> int:
        """计算两个单词之间的编辑距离（仅考虑替换操作）"""
        return sum(c1 != c2 for c1, c2 in zip(word1, word2))

    res = []
    for query in queries:
        for word in dictionary:
            if edit_distance(query, word) <= 2:
                res.append(query)
                break
    return res

Solution = create_solution(solution_function_name)