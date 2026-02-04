# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2736
标题: Minimum Additions to Make Valid String
难度: medium
链接: https://leetcode.cn/problems/minimum-additions-to-make-valid-string/
题目类型: 栈、贪心、字符串、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2645. 构造有效字符串的最少插入数 - 给你一个字符串 word ，你可以向其中任何位置插入 "a"、"b" 或 "c" 任意次，返回使 word 有效 需要插入的最少字母数。 如果字符串可以由 "abc" 串联多次得到，则认为该字符串 有效 。 示例 1： 输入：word = "b" 输出：2 解释：在 "b" 之前插入 "a" ，在 "b" 之后插入 "c" 可以得到有效字符串 "abc" 。 示例 2： 输入：word = "aaa" 输出：6 解释：在每个 "a" 之后依次插入 "b" 和 "c" 可以得到有效字符串 "abcabcabc" 。 示例 3： 输入：word = "abc" 输出：0 解释：word 已经是有效字符串，不需要进行修改。 提示： * 1 <= word.length <= 50 * word 仅由字母 "a"、"b" 和 "c" 组成。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，逐个字符检查并计算需要插入的字符数。

算法步骤:
1. 初始化一个期望字符 `expected` 为 'a'。
2. 遍历字符串 `word` 的每个字符 `char`：
   - 如果 `char` 不等于 `expected`，则计算需要插入的字符数，并更新 `expected`。
   - 更新 `expected` 为下一个期望字符（'a' -> 'b' -> 'c' -> 'a'）。
3. 返回总插入字符数。

关键点:
- 使用贪心算法逐个字符检查并计算需要插入的字符数。
- 通过维护一个期望字符 `expected` 来判断当前字符是否符合预期。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 `word` 的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_add_to_make_valid(word: str) -> int:
    """
    函数式接口 - 计算使 word 有效需要插入的最少字母数
    """
    expected = 'a'
    insertions = 0
    
    for char in word:
        while char != expected:
            insertions += 1
            if expected == 'a':
                expected = 'b'
            elif expected == 'b':
                expected = 'c'
            else:
                expected = 'a'
        
        # 更新期望字符
        if expected == 'a':
            expected = 'b'
        elif expected == 'b':
            expected = 'c'
        else:
            expected = 'a'
    
    # 处理剩余的不完整 "abc"
    if expected == 'b':
        insertions += 2
    elif expected == 'c':
        insertions += 1
    
    return insertions


Solution = create_solution(min_add_to_make_valid)