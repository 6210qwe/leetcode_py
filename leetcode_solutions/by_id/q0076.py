# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 76
标题: Minimum Window Substring
难度: hard
链接: https://leetcode.cn/problems/minimum-window-substring/
题目类型: 哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
76. 最小覆盖子串 - 给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口 子串，使得该子串包含 t 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 ""。 测试用例保证答案唯一。 示例 1： 输入：s = "ADOBECODEBANC", t = "ABC" 输出："BANC" 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。 示例 2： 输入：s = "a", t = "a" 输出："a" 解释：整个字符串 s 是最小覆盖子串。 示例 3: 输入: s = "a", t = "aa" 输出: "" 解释: t 中两个字符 'a' 均应包含在 s 的子串中， 因此没有符合条件的子字符串，返回空字符串。 提示： * m == s.length * n == t.length * 1 <= m, n <= 105 * s 和 t 由英文字母组成 进阶：你能设计一个在 O(m + n) 时间内解决此问题的算法吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 滑动窗口，使用双指针维护一个包含t中所有字符的窗口

算法步骤:
1. 统计t中每个字符的出现次数，存储在need字典中
2. 使用双指针left和right维护滑动窗口
3. 扩展窗口（right++）：
   - 将s[right]加入窗口
   - 如果窗口包含t中所有字符，尝试收缩窗口
4. 收缩窗口（left++）：
   - 如果窗口仍然包含t中所有字符，更新最小窗口
   - 否则停止收缩
5. 返回最小窗口

关键点:
- 使用need字典记录需要的字符及其数量
- 使用valid变量记录窗口中满足条件的字符数量
- 时间复杂度O(m+n)，空间复杂度O(m+n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m+n) - m和n分别为两个字符串的长度
空间复杂度: O(m+n) - 存储字符计数
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Dict
from leetcode_solutions.utils.solution import create_solution


def min_window(s: str, t: str) -> str:
    """
    函数式接口 - 滑动窗口
    
    实现思路:
    使用滑动窗口维护一个包含t中所有字符的最小窗口。
    
    Args:
        s: 源字符串
        t: 目标字符串
        
    Returns:
        s中包含t中所有字符的最短窗口子串
        
    Example:
        >>> min_window("ADOBECODEBANC", "ABC")
        'BANC'
    """
    if not s or not t or len(s) < len(t):
        return ""
    
    # 统计t中每个字符的出现次数
    need: Dict[str, int] = {}
    for char in t:
        need[char] = need.get(char, 0) + 1
    
    # 窗口中的字符计数
    window: Dict[str, int] = {}
    left, right = 0, 0
    valid = 0  # 窗口中满足条件的字符数量
    start, min_len = 0, float('inf')
    
    while right < len(s):
        # 扩展窗口
        char = s[right]
        right += 1
        
        if char in need:
            window[char] = window.get(char, 0) + 1
            if window[char] == need[char]:
                valid += 1
        
        # 收缩窗口
        while valid == len(need):
            # 更新最小窗口
            if right - left < min_len:
                start = left
                min_len = right - left
            
            # 移除left指向的字符
            char = s[left]
            left += 1
            
            if char in need:
                if window[char] == need[char]:
                    valid -= 1
                window[char] -= 1
    
    return "" if min_len == float('inf') else s[start:start + min_len]


# 自动生成Solution类（无需手动编写）
Solution = create_solution(min_window)
