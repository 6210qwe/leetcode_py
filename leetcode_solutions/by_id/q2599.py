# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2599
标题: Take K of Each Character From Left and Right
难度: medium
链接: https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/
题目类型: 哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2516. 每种字符至少取 K 个 - 给你一个由字符 'a'、'b'、'c' 组成的字符串 s 和一个非负整数 k 。每分钟，你可以选择取走 s 最左侧 还是 最右侧 的那个字符。 你必须取走每种字符 至少 k 个，返回需要的 最少 分钟数；如果无法取到，则返回 -1 。 示例 1： 输入：s = "aabaaaacaabc", k = 2 输出：8 解释： 从 s 的左侧取三个字符，现在共取到两个字符 'a' 、一个字符 'b' 。 从 s 的右侧取五个字符，现在共取到四个字符 'a' 、两个字符 'b' 和两个字符 'c' 。 共需要 3 + 5 = 8 分钟。 可以证明需要的最少分钟数是 8 。 示例 2： 输入：s = "a", k = 1 输出：-1 解释：无法取到一个字符 'b' 或者 'c'，所以返回 -1 。 提示： * 1 <= s.length <= 105 * s 仅由字母 'a'、'b'、'c' 组成 * 0 <= k <= s.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针和滑动窗口来找到满足条件的最短子串。

算法步骤:
1. 统计字符串中每个字符的总数。
2. 如果任一字符的总数小于 k，则返回 -1。
3. 使用双指针从两端向中间收缩，确保每种字符至少有 k 个。
4. 计算并更新最小长度。

关键点:
- 使用双指针和滑动窗口来高效地找到满足条件的最短子串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def take_characters(s: str, k: int) -> int:
    """
    函数式接口 - 返回需要的最少分钟数
    """
    # 统计字符串中每个字符的总数
    count = [0] * 3
    for char in s:
        count[ord(char) - ord('a')] += 1
    
    # 如果任一字符的总数小于 k，则返回 -1
    if any(c < k for c in count):
        return -1
    
    # 初始化双指针
    left, right = 0, len(s) - 1
    min_length = len(s)
    
    while left <= right:
        # 从左端取字符
        while left < len(s) and all(count[c] >= k for c in range(3)):
            count[ord(s[left]) - ord('a')] -= 1
            left += 1
        
        # 从右端取字符
        while right >= 0 and all(count[c] >= k for c in range(3)):
            count[ord(s[right]) - ord('a')] -= 1
            right -= 1
        
        # 更新最小长度
        min_length = min(min_length, left + (len(s) - 1 - right))
        
        # 移动指针
        if left < len(s):
            count[ord(s[left]) - ord('a')] += 1
            left += 1
        if right >= 0:
            count[ord(s[right]) - ord('a')] += 1
            right -= 1
    
    return min_length


Solution = create_solution(take_characters)