# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1934
标题: Evaluate the Bracket Pairs of a String
难度: medium
链接: https://leetcode.cn/problems/evaluate-the-bracket-pairs-of-a-string/
题目类型: 数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1807. 替换字符串中的括号内容 - 给你一个字符串 s ，它包含一些括号对，每个括号中包含一个 非空 的键。 * 比方说，字符串 "(name)is(age)yearsold" 中，有 两个 括号对，分别包含键 "name" 和 "age" 。 你知道许多键对应的值，这些关系由二维字符串数组 knowledge 表示，其中 knowledge[i] = [keyi, valuei] ，表示键 keyi 对应的值为 valuei 。 你需要替换 所有 的括号对。当你替换一个括号对，且它包含的键为 keyi 时，你需要： * 将 keyi 和括号用对应的值 valuei 替换。 * 如果从 knowledge 中无法得知某个键对应的值，你需要将 keyi 和括号用问号 "?" 替换（不需要引号）。 knowledge 中每个键最多只会出现一次。s 中不会有嵌套的括号。 请你返回替换 所有 括号对后的结果字符串。 示例 1： 输入：s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]] 输出："bobistwoyearsold" 解释： 键 "name" 对应的值为 "bob" ，所以将 "(name)" 替换为 "bob" 。 键 "age" 对应的值为 "two" ，所以将 "(age)" 替换为 "two" 。 示例 2： 输入：s = "hi(name)", knowledge = [["a","b"]] 输出："hi?" 解释：由于不知道键 "name" 对应的值，所以用 "?" 替换 "(name)" 。 示例 3： 输入：s = "(a)(a)(a)aaa", knowledge = [["a","yes"]] 输出："yesyesyesaaa" 解释：相同的键在 s 中可能会出现多次。 键 "a" 对应的值为 "yes" ，所以将所有的 "(a)" 替换为 "yes" 。 注意，不在括号里的 "a" 不需要被替换。 提示： * 1 <= s.length <= 105 * 0 <= knowledge.length <= 105 * knowledge[i].length == 2 * 1 <= keyi.length, valuei.length <= 10 * s 只包含小写英文字母和圆括号 '(' 和 ')' 。 * s 中每一个左圆括号 '(' 都有对应的右圆括号 ')' 。 * s 中每对括号内的键都不会为空。 * s 中不会有嵌套括号对。 * keyi 和 valuei 只包含小写英文字母。 * knowledge 中的 keyi 不会重复。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储键值对，并遍历字符串进行替换。

算法步骤:
1. 构建一个哈希表，存储 knowledge 中的键值对。
2. 遍历字符串 s，使用一个标志变量 in_brackets 来判断当前是否在括号内。
3. 如果遇到左括号，设置 in_brackets 为 True，并开始记录括号内的键。
4. 如果遇到右括号，设置 in_brackets 为 False，并根据哈希表查找并替换括号内的键。
5. 如果不在括号内，直接将字符添加到结果字符串中。

关键点:
- 使用哈希表快速查找键值对。
- 通过标志变量 in_brackets 控制括号内的键的记录。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是字符串 s 的长度，m 是 knowledge 的长度。
空间复杂度: O(m)，用于存储哈希表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def evaluate_bracket_pairs(s: str, knowledge: List[List[str]]) -> str:
    """
    函数式接口 - 替换字符串中的括号内容
    """
    # 构建哈希表
    knowledge_dict = {key: value for key, value in knowledge}
    
    result = []
    in_brackets = False
    current_key = []
    
    for char in s:
        if char == '(':
            in_brackets = True
            current_key = []
        elif char == ')':
            in_brackets = False
            key = ''.join(current_key)
            result.append(knowledge_dict.get(key, '?'))
        elif in_brackets:
            current_key.append(char)
        else:
            result.append(char)
    
    return ''.join(result)


Solution = create_solution(evaluate_bracket_pairs)