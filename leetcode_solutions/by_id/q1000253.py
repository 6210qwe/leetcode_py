# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000253
标题: 最小覆盖子串
难度: hard
链接: https://leetcode.cn/problems/M1oyTv/
题目类型: 哈希表、字符串、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 017. 最小覆盖子串 - 给定两个字符串 s 和 t 。返回 s 中包含 t 的所有字符的最短子字符串。如果 s 中不存在符合条件的子字符串，则返回空字符串 "" 。 如果 s 中存在多个符合条件的子字符串，返回任意一个。 注意： 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。 示例 1： 输入：s = "ADOBECODEBANC", t = "ABC" 输出："BANC" 解释：最短子字符串 "BANC" 包含了字符串 t 的所有字符 'A'、'B'、'C' 示例 2： 输入：s = "a", t = "a" 输出："a" 示例 3： 输入：s = "a", t = "aa" 输出："" 解释：t 中两个字符 'a' 均应包含在 s 的子串中，因此没有符合条件的子字符串，返回空字符串。 提示： * 1 <= s.length, t.length <= 105 * s 和 t 由英文字母组成 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？ 注意：本题与主站 76 题相似（本题答案不唯一）：https://leetcode.cn/problems/minimum-window-substring/ [https://leetcode.cn/problems/minimum-window-substring/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 滑动窗口 + 计数匹配（need / window）

算法步骤:
1. 统计 t 中每个字符需要的次数 need
2. 使用滑动窗口在 s 上移动，维护 window 计数、以及已满足的字符种类数 formed
3. 右指针扩展窗口，更新 window；当某字符计数满足 need 时，formed += 1
4. 当 formed == required（需要满足的字符种类数）时，尝试收缩左边界：
   - 更新最短区间
   - 移动左指针并更新 window；若某字符计数不再满足 need，则 formed -= 1
5. 最终返回记录到的最短子串；若不存在返回 ""

关键点:
- 题目要求覆盖 t 的所有字符（包含重复次数）
- 用 formed/required 避免每次都全量比较计数
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - n 为 s 长度
空间复杂度: O(Σ) - 字符计数表（英文字母可视作 O(1)）
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_window(s: str, t: str) -> str:
    """
    函数式接口 - 最小覆盖子串
    """
    if not t or not s:
        return ""

    from collections import Counter, defaultdict

    need = Counter(t)
    required = len(need)
    window = defaultdict(int)

    formed = 0
    left = 0
    best_len = float("inf")
    best_l = 0

    for right, ch in enumerate(s):
        window[ch] += 1
        if ch in need and window[ch] == need[ch]:
            formed += 1

        while formed == required and left <= right:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_l = left

            left_ch = s[left]
            window[left_ch] -= 1
            if left_ch in need and window[left_ch] < need[left_ch]:
                formed -= 1
            left += 1

    if best_len == float("inf"):
        return ""
    return s[best_l:best_l + best_len]


Solution = create_solution(min_window)
