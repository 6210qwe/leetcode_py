# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2099
标题: Number of Strings That Appear as Substrings in Word
难度: easy
链接: https://leetcode.cn/problems/number-of-strings-that-appear-as-substrings-in-word/
题目类型: 数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1967. 作为子字符串出现在单词中的字符串数目 - 给你一个字符串数组 patterns 和一个字符串 word ，统计 patterns 中有多少个字符串是 word 的子字符串。返回字符串数目。 子字符串 是字符串中的一个连续字符序列。 示例 1： 输入：patterns = ["a","abc","bc","d"], word = "abc" 输出：3 解释： - "a" 是 "abc" 的子字符串。 - "abc" 是 "abc" 的子字符串。 - "bc" 是 "abc" 的子字符串。 - "d" 不是 "abc" 的子字符串。 patterns 中有 3 个字符串作为子字符串出现在 word 中。 示例 2： 输入：patterns = ["a","b","c"], word = "aaaaabbbbb" 输出：2 解释： - "a" 是 "aaaaabbbbb" 的子字符串。 - "b" 是 "aaaaabbbbb" 的子字符串。 - "c" 不是 "aaaaabbbbb" 的字符串。 patterns 中有 2 个字符串作为子字符串出现在 word 中。 示例 3： 输入：patterns = ["a","a","a"], word = "ab" 输出：3 解释：patterns 中的每个字符串都作为子字符串出现在 word "ab" 中。 提示： * 1 <= patterns.length <= 100 * 1 <= patterns[i].length <= 100 * 1 <= word.length <= 100 * patterns[i] 和 word 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 遍历 patterns 数组，检查每个 pattern 是否是 word 的子字符串。

算法步骤:
1. 初始化计数器 count 为 0。
2. 遍历 patterns 数组，对于每个 pattern，使用 in 操作符检查它是否是 word 的子字符串。
3. 如果是，则将计数器 count 增加 1。
4. 返回计数器 count。

关键点:
- 使用 in 操作符可以高效地检查子字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 patterns 的长度，m 是 word 的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def number_of_substrings(patterns: List[str], word: str) -> int:
    """
    函数式接口 - 统计 patterns 中有多少个字符串是 word 的子字符串。
    """
    count = 0
    for pattern in patterns:
        if pattern in word:
            count += 1
    return count


Solution = create_solution(number_of_substrings)