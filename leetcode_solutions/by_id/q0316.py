# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 316
标题: Remove Duplicate Letters
难度: medium
链接: https://leetcode.cn/problems/remove-duplicate-letters/
题目类型: 栈、贪心、字符串、单调栈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
316. 去除重复字母 - 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。 示例 1： 输入：s = "bcabc" 输出："abc" 示例 2： 输入：s = "cbacdcbc" 输出："acdb" 提示： * 1 <= s.length <= 104 * s 由小写英文字母组成 注意：该题与 1081 https://leetcode.cn/problems/smallest-subsequence-of-distinct-characters [https://leetcode.cn/problems/smallest-subsequence-of-distinct-characters] 相同
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用单调栈，维护字典序最小的结果，同时保证每个字符至少出现一次

算法步骤:
1. 统计每个字符的最后出现位置
2. 使用栈维护结果，保持字典序最小
3. 如果当前字符小于栈顶且栈顶字符后面还会出现，则弹出栈顶
4. 使用集合记录栈中已存在的字符，避免重复

关键点:
- 使用单调栈贪心策略
- 时间复杂度O(n)，空间复杂度O(1)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历字符串一次
空间复杂度: O(1) - 字符集大小固定
"""

# ============================================================================
# 代码实现
# ============================================================================

from leetcode_solutions.utils.solution import create_solution


def remove_duplicate_letters(s: str) -> str:
    """
    函数式接口 - 去除重复字母
    
    实现思路:
    使用单调栈，维护字典序最小的结果，同时保证每个字符至少出现一次。
    
    Args:
        s: 字符串
        
    Returns:
        去除重复字母后字典序最小的字符串
        
    Example:
        >>> remove_duplicate_letters("bcabc")
        'abc'
    """
    # 统计每个字符的最后出现位置
    last_occurrence = {char: i for i, char in enumerate(s)}
    
    stack = []
    in_stack = set()
    
    for i, char in enumerate(s):
        if char in in_stack:
            continue
        
        # 如果当前字符小于栈顶，且栈顶字符后面还会出现，则弹出栈顶
        while stack and char < stack[-1] and last_occurrence[stack[-1]] > i:
            in_stack.remove(stack.pop())
        
        stack.append(char)
        in_stack.add(char)
    
    return ''.join(stack)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(remove_duplicate_letters)
