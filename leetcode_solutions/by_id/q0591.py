# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 591
标题: Tag Validator
难度: hard
链接: https://leetcode.cn/problems/tag-validator/
题目类型: 栈、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
591. 标签验证器 - 给定一个表示代码片段的字符串，你需要实现一个验证器来解析这段代码，并返回它是否合法。合法的代码片段需要遵守以下的所有规则： 1. 代码必须被合法的闭合标签包围。否则，代码是无效的。 2. 闭合标签（不一定合法）要严格符合格式：<TAG_NAME>TAG_CONTENT</TAG_NAME>。其中，<TAG_NAME>是起始标签，</TAG_NAME>是结束标签。起始和结束标签中的 TAG_NAME 应当相同。当且仅当 TAG_NAME 和 TAG_CONTENT 都是合法的，闭合标签才是合法的。 3. 合法的 TAG_NAME 仅含有大写字母，长度在范围 [1,9] 之间。否则，该 TAG_NAME 是不合法的。 4. 合法的 TAG_CONTENT 可以包含其他合法的闭合标签，cdata （请参考规则7）和任意字符（注意参考规则1）除了不匹配的<、不匹配的起始和结束标签、不匹配的或带有不合法 TAG_NAME 的闭合标签。否则，TAG_CONTENT 是不合法的。 5. 一个起始标签，如果没有具有相同 TAG_NAME 的结束标签与之匹配，是不合法的。反之亦然。不过，你也需要考虑标签嵌套的问题。 6. 一个<，如果你找不到一个后续的>与之匹配，是不合法的。并且当你找到一个<或</时，所有直到下一个>的前的字符，都应当被解析为 TAG_NAME（不一定合法）。 7. cdata 有如下格式：<![CDATA[CDATA_CONTENT]]>。CDATA_CONTENT 的范围被定义成 <![CDATA[ 和后续的第一个 ]]>之间的字符。 8. CDATA_CONTENT 可以包含任意字符。cdata 的功能是阻止验证器解析CDATA_CONTENT，所以即使其中有一些字符可以被解析为标签（无论合法还是不合法），也应该将它们视为常规字符。 示例 1： 输入：code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>" 输出：true 解释： 代码被闭合的标签包围：<DIV> 和 </DIV>。 TAG_NAME 是合法的，TAG_CONTENT 只包含一些字母和 cdata。 尽管 CDATA_CONTENT 有一个非法 TAG_NAME 的未匹配开始标签，它可以被认为是普通文本，不被解析为一个标签。 所以 TAG_CONTENT 是合法的，并且代码是合法的。因此返回 true。 示例 2： 输入：code = "<DIV>>> ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>" 输出：true 解释： 我们首先将代码分割为：start_tag|tag_content|end_tag。 start_tag -> "<DIV>" end_tag -> "</DIV>" tag_content 也可以被分割为：text1|cdata|text2。 text1 -> ">> ![cdata[]] " cdata -> "<![CDATA[<div>]>]]>"，其中 CDATA_CONTENT 是 "<div>]>" text2 -> "]]>>]" start_tag 不是 "<DIV>>>" 的原因是规则 6。 cdata 不是 "<![CDATA[<div>]>]]>]]>" 的原因是规则 7。 示例 3： 输入：code = "<A> <B> </A> </B>" 输出：false 解释：不平衡。如果 "<A>" 是闭合的，那么 "<B>" 一定没有匹配，反之亦然。 提示： * 1 <= code.length <= 500 * code 只包含英文字母，数字，'<'，'>'，'/'，'!'，'['，']'，'.' 和 ' '。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用栈来处理标签的嵌套和匹配问题。同时，处理 CDATA 部分，确保其不会被误解析为标签。

算法步骤:
1. 初始化一个空栈，用于存储未匹配的起始标签。
2. 遍历输入字符串 `code`，使用指针 `i` 来追踪当前的位置。
3. 如果遇到 `<`，检查接下来的部分：
   - 如果是 `<![CDATA[`，则跳过 CDATA 部分。
   - 如果是 `</`，则尝试匹配栈顶的起始标签。
   - 如果是 `<`，则提取并验证标签名，将其压入栈中。
4. 如果遇到 `>`，检查栈是否为空，如果不为空则弹出栈顶元素。
5. 最后，检查栈是否为空，如果为空则说明所有标签都已匹配，返回 `True`，否则返回 `False`。

关键点:
- 使用栈来处理标签的嵌套和匹配。
- 处理 CDATA 部分，确保其不会被误解析为标签。
- 验证标签名是否合法。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 `code` 的长度。我们只需要遍历一次字符串。
空间复杂度: O(n)，最坏情况下，栈中可能会存储所有的起始标签。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(code: str) -> bool:
    """
    函数式接口 - 实现标签验证器
    """
    def is_valid_tag_name(tag_name: str) -> bool:
        return 1 <= len(tag_name) <= 9 and all(c.isupper() for c in tag_name)

    stack = []
    i = 0
    while i < len(code):
        if code[i] == '<':
            if i + 9 < len(code) and code[i:i+9] == '<![CDATA[':
                j = code.find(']]>', i)
                if j == -1:
                    return False
                i = j + 3
            elif i + 2 < len(code) and code[i:i+2] == '</':
                j = code.find('>', i)
                if j == -1:
                    return False
                tag_name = code[i+2:j]
                if not stack or stack.pop() != tag_name:
                    return False
                i = j + 1
            else:
                j = code.find('>', i)
                if j == -1:
                    return False
                tag_name = code[i+1:j]
                if not is_valid_tag_name(tag_name):
                    return False
                stack.append(tag_name)
                i = j + 1
        else:
            i += 1

    return not stack


Solution = create_solution(solution_function_name)