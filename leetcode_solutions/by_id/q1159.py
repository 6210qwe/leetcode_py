# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1159
标题: Smallest Subsequence of Distinct Characters
难度: medium
链接: https://leetcode.cn/problems/smallest-subsequence-of-distinct-characters/
题目类型: 栈、贪心、字符串、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1081. 不同字符的最小子序列 - 返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。 示例 1： 输入：s = "bcabc" 输出："abc" 示例 2： 输入：s = "cbacdcbc" 输出："acdb" 提示： * 1 <= s.length <= 1000 * s 由小写英文字母组成 注意：该题与 316 https://leetcode.cn/problems/remove-duplicate-letters/ [https://leetcode.cn/problems/remove-duplicate-letters/] 相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法和单调栈来构建字典序最小的子序列。

算法步骤:
1. 统计每个字符的最后出现位置。
2. 使用一个栈来构建结果字符串。
3. 遍历字符串，对于每个字符：
   - 如果该字符已经在栈中，则跳过。
   - 否则，比较当前字符和栈顶字符，如果当前字符比栈顶字符小且栈顶字符在后面还会出现，则弹出栈顶字符。
   - 将当前字符压入栈中。
4. 最终栈中的字符即为所求的最小子序列。

关键点:
- 使用单调栈来保持字典序最小。
- 记录每个字符的最后出现位置以决定是否弹出栈顶字符。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 s 的长度。每个字符最多只会被压入和弹出栈一次。
空间复杂度: O(1) 或 O(26)，因为栈的最大长度不会超过字符集的大小（26个小写字母）。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def smallest_subsequence(s: str) -> str:
    """
    函数式接口 - 返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。
    """
    # 统计每个字符的最后出现位置
    last_occurrence = {char: i for i, char in enumerate(s)}
    
    # 使用栈来构建结果字符串
    stack = []
    
    # 遍历字符串
    for i, char in enumerate(s):
        if char in stack:
            continue
        
        # 比较当前字符和栈顶字符
        while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
            stack.pop()
        
        # 将当前字符压入栈中
        stack.append(char)
    
    return ''.join(stack)


Solution = create_solution(smallest_subsequence)