# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 889
标题: Buddy Strings
难度: easy
链接: https://leetcode.cn/problems/buddy-strings/
题目类型: 哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
859. 亲密字符串 - 给你两个字符串 s 和 goal ，只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果，就返回 true ；否则返回 false 。 交换字母的定义是：取两个下标 i 和 j （下标从 0 开始）且满足 i != j ，接着交换 s[i] 和 s[j] 处的字符。 * 例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。 示例 1： 输入：s = "ab", goal = "ba" 输出：true 解释：你可以交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba"，此时 s 和 goal 相等。 示例 2： 输入：s = "ab", goal = "ab" 输出：false 解释：你只能交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba"，此时 s 和 goal 不相等。 示例 3： 输入：s = "aa", goal = "aa" 输出：true 解释：你可以交换 s[0] = 'a' 和 s[1] = 'a' 生成 "aa"，此时 s 和 goal 相等。 提示： * 1 <= s.length, goal.length <= 2 * 104 * s 和 goal 由小写英文字母组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 检查两个字符串是否可以通过交换两个字符使其相等。

算法步骤:
1. 如果 s 和 goal 长度不同，直接返回 False。
2. 如果 s 和 goal 完全相同，检查 s 中是否有重复字符，如果有则返回 True，否则返回 False。
3. 找到 s 和 goal 中不同的字符对，如果超过两对，则返回 False。
4. 检查这两对字符是否可以通过交换使 s 变成 goal。

关键点:
- 使用计数器来检查是否有重复字符。
- 使用列表来存储不同字符对，并检查这些对是否可以通过交换使 s 变成 goal。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 s 的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def buddy_strings(s: str, goal: str) -> bool:
    """
    函数式接口 - 判断两个字符串是否可以通过交换两个字符使其相等
    """
    if len(s) != len(goal):
        return False

    if s == goal:
        # 检查 s 中是否有重复字符
        seen = set()
        for char in s:
            if char in seen:
                return True
            seen.add(char)
        return False

    # 找到 s 和 goal 中不同的字符对
    diff = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diff.append((s[i], goal[i]))
            if len(diff) > 2:
                return False

    # 检查这两对字符是否可以通过交换使 s 变成 goal
    return len(diff) == 2 and diff[0] == diff[1][::-1]


Solution = create_solution(buddy_strings)