# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1526
标题: HTML Entity Parser
难度: medium
链接: https://leetcode.cn/problems/html-entity-parser/
题目类型: 哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1410. HTML 实体解析器 - 「HTML 实体解析器」 是一种特殊的解析器，它将 HTML 代码作为输入，并用字符本身替换掉所有这些特殊的字符实体。 HTML 里这些特殊字符和它们对应的字符实体包括： * 双引号：字符实体为 &quot; ，对应的字符是 " 。 * 单引号：字符实体为 &apos; ，对应的字符是 ' 。 * 与符号：字符实体为 &amp; ，对应对的字符是 & 。 * 大于号：字符实体为 &gt; ，对应的字符是 > 。 * 小于号：字符实体为 &lt; ，对应的字符是 < 。 * 斜线号：字符实体为 &frasl; ，对应的字符是 / 。 给你输入字符串 text ，请你实现一个 HTML 实体解析器，返回解析器解析后的结果。 示例 1： 输入：text = "&amp; is an HTML entity but &ambassador; is not." 输出："& is an HTML entity but &ambassador; is not." 解释：解析器把字符实体 &amp; 用 & 替换 示例 2： 输入：text = "and I quote: &quot;...&quot;" 输出："and I quote: \"...\"" 示例 3： 输入：text = "Stay home! Practice on Leetcode :)" 输出："Stay home! Practice on Leetcode :)" 示例 4： 输入：text = "x &gt; y &amp;&amp; x &lt; y is always false" 输出："x > y && x < y is always false" 示例 5： 输入：text = "leetcode.com&frasl;problemset&frasl;all" 输出："leetcode.com/problemset/all" 提示： * 1 <= text.length <= 10^5 * 字符串可能包含 256 个ASCII 字符中的任意字符。
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
