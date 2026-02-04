# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2292
标题: Counting Words With a Given Prefix
难度: easy
链接: https://leetcode.cn/problems/counting-words-with-a-given-prefix/
题目类型: 数组、字符串、字符串匹配
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2185. 统计包含给定前缀的字符串 - 给你一个字符串数组 words 和一个字符串 pref 。 返回 words 中以 pref 作为 前缀 的字符串的数目。 字符串 s 的 前缀 就是 s 的任一前导连续字符串。 示例 1： 输入：words = ["pay","attention","practice","attend"], pref = "at" 输出：2 解释：以 "at" 作为前缀的字符串有两个，分别是："attention" 和 "attend" 。 示例 2： 输入：words = ["leetcode","win","loops","success"], pref = "code" 输出：0 解释：不存在以 "code" 作为前缀的字符串。 提示： * 1 <= words.length <= 100 * 1 <= words[i].length, pref.length <= 100 * words[i] 和 pref 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 逐个检查每个单词是否以给定的前缀开头。

算法步骤:
1. 初始化一个计数器为 0。
2. 遍历字符串数组 words，对于每个单词，检查其是否以 pref 作为前缀。
3. 如果是，则将计数器加 1。
4. 返回计数器的值。

关键点:
- 使用 Python 的字符串方法 `startswith` 来检查前缀。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 words 的长度，m 是 pref 的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def prefix_count(words: List[str], pref: str) -> int:
    """
    函数式接口 - 统计包含给定前缀的字符串数量
    """
    count = 0
    for word in words:
        if word.startswith(pref):
            count += 1
    return count


Solution = create_solution(prefix_count)