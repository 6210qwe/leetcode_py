# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2881
标题: Split Strings by Separator
难度: easy
链接: https://leetcode.cn/problems/split-strings-by-separator/
题目类型: 数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2788. 按分隔符拆分字符串 - 给你一个字符串数组 words 和一个字符 separator ，请你按 separator 拆分 words 中的每个字符串。 返回一个由拆分后的新字符串组成的字符串数组，不包括空字符串 。 注意 * separator 用于决定拆分发生的位置，但它不包含在结果字符串中。 * 拆分可能形成两个以上的字符串。 * 结果字符串必须保持初始相同的先后顺序。 示例 1： 输入：words = ["one.two.three","four.five","six"], separator = "." 输出：["one","two","three","four","five","six"] 解释：在本示例中，我们进行下述拆分： "one.two.three" 拆分为 "one", "two", "three" "four.five" 拆分为 "four", "five" "six" 拆分为 "six" 因此，结果数组为 ["one","two","three","four","five","six"] 。 示例 2： 输入：words = ["$easy$","$problem$"], separator = "$" 输出：["easy","problem"] 解释：在本示例中，我们进行下述拆分： "$easy$" 拆分为 "easy"（不包括空字符串） "$problem$" 拆分为 "problem"（不包括空字符串） 因此，结果数组为 ["easy","problem"] 。 示例 3： 输入：words = ["|||"], separator = "|" 输出：[] 解释：在本示例中，"|||" 的拆分结果将只包含一些空字符串，所以我们返回一个空数组 [] 。 提示： * 1 <= words.length <= 100 * 1 <= words[i].length <= 20 * words[i] 中的字符要么是小写英文字母，要么就是字符串 ".,|$#@" 中的字符（不包括引号） * separator 是字符串 ".,|$#@" 中的某个字符（不包括引号）
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Python 内置的 split 方法对每个字符串进行拆分，并过滤掉空字符串。

算法步骤:
1. 初始化一个空列表 result 用于存储最终结果。
2. 遍历 words 数组中的每个字符串，使用 split 方法按 separator 拆分。
3. 将拆分后的非空字符串添加到 result 列表中。
4. 返回 result 列表。

关键点:
- 使用 split 方法可以方便地按指定分隔符拆分字符串。
- 过滤掉空字符串以满足题目要求。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 words 的长度，m 是每个字符串的平均长度。
空间复杂度: O(n * m)，存储拆分后的结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def split_strings_by_separator(words: List[str], separator: str) -> List[str]:
    """
    函数式接口 - 按分隔符拆分字符串
    """
    result = []
    for word in words:
        # 按 separator 拆分字符串并过滤掉空字符串
        parts = [part for part in word.split(separator) if part]
        result.extend(parts)
    return result


Solution = create_solution(split_strings_by_separator)