# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1045
标题: Check If Word Is Valid After Substitutions
难度: medium
链接: https://leetcode.cn/problems/check-if-word-is-valid-after-substitutions/
题目类型: 栈、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1003. 检查替换后的词是否有效 - 给你一个字符串 s ，请你判断它是否 有效 。 字符串 s 有效 需要满足：假设开始有一个空字符串 t = "" ，你可以执行 任意次 下述操作将 t 转换为 s ： * 将字符串 "abc" 插入到 t 中的任意位置。形式上，t 变为 tleft + "abc" + tright，其中 t == tleft + tright 。注意，tleft 和 tright 可能为 空 。 如果字符串 s 有效，则返回 true；否则，返回 false。 示例 1： 输入：s = "aabcbc" 输出：true 解释： "" -> "abc" -> "aabcbc" 因此，"aabcbc" 有效。 示例 2： 输入：s = "abcabcababcc" 输出：true 解释： "" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc" 因此，"abcabcababcc" 有效。 示例 3： 输入：s = "abccba" 输出：false 解释：执行操作无法得到 "abccba" 。 提示： * 1 <= s.length <= 2 * 104 * s 由字母 'a'、'b' 和 'c' 组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈来检查字符串的有效性。

算法步骤:
1. 初始化一个空栈。
2. 遍历字符串中的每个字符：
   - 如果字符是 'a' 或 'b'，将其压入栈中。
   - 如果字符是 'c'，检查栈顶是否有 'b' 和 'a'，如果有则弹出 'b' 和 'a'，否则返回 False。
3. 最后检查栈是否为空，如果为空则返回 True，否则返回 False。

关键点:
- 使用栈来匹配 "abc" 子序列。
- 每次遇到 'c' 时，确保栈顶有 'b' 和 'a'。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 s 的长度。每个字符最多只会被压入和弹出栈一次。
空间复杂度: O(n)，在最坏情况下，栈中可能会存储所有字符。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def is_valid(s: str) -> bool:
    """
    函数式接口 - 判断字符串 s 是否有效
    """
    stack = []
    for char in s:
        if char == 'a':
            stack.append(char)
        elif char == 'b':
            if not stack or stack[-1] != 'a':
                return False
            stack.append(char)
        elif char == 'c':
            if len(stack) < 2 or stack[-1] != 'b' or stack[-2] != 'a':
                return False
            stack.pop()  # 弹出 'b'
            stack.pop()  # 弹出 'a'
    
    return len(stack) == 0


Solution = create_solution(is_valid)