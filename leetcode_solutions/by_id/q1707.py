# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1707
标题: Check If String Is Transformable With Substring Sort Operations
难度: hard
链接: https://leetcode.cn/problems/check-if-string-is-transformable-with-substring-sort-operations/
题目类型: 贪心、字符串、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1585. 检查字符串是否可以通过排序子字符串得到另一个字符串 - 给你两个字符串 s 和 t ，请你通过若干次以下操作将字符串 s 转化成字符串 t ： * 选择 s 中一个 非空 子字符串并将它包含的字符就地 升序 排序。 比方说，对下划线所示的子字符串进行操作可以由 "14234" 得到 "12344" 。 如果可以将字符串 s 变成 t ，返回 true 。否则，返回 false 。 一个 子字符串 定义为一个字符串中连续的若干字符。 示例 1： 输入：s = "84532", t = "34852" 输出：true 解释：你可以按以下操作将 s 转变为 t ： "84532" （从下标 2 到下标 3）-> "84352" "84352" （从下标 0 到下标 2） -> "34852" 示例 2： 输入：s = "34521", t = "23415" 输出：true 解释：你可以按以下操作将 s 转变为 t ： "34521" -> "23451" "23451" -> "23415" 示例 3： 输入：s = "12345", t = "12435" 输出：false 示例 4： 输入：s = "1", t = "2" 输出：false 提示： * s.length == t.length * 1 <= s.length <= 105 * s 和 t 都只包含数字字符，即 '0' 到 '9' 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，通过维护每个数字在字符串 s 中的位置，确保 t 中的每个数字在 s 中的位置是递增的。

算法步骤:
1. 初始化一个字典 `positions`，用于存储每个数字在字符串 s 中的位置。
2. 遍历字符串 s，填充 `positions` 字典。
3. 遍历字符串 t，检查 t 中的每个数字在 s 中的位置是否满足条件。
4. 如果 t 中的某个数字在 s 中的位置不满足条件，则返回 False。
5. 如果遍历完 t 后所有条件都满足，则返回 True。

关键点:
- 使用字典 `positions` 来记录每个数字在 s 中的位置。
- 在遍历 t 时，确保 t 中的每个数字在 s 中的位置是递增的。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 s 的长度。我们只需要遍历字符串 s 和 t 各一次。
空间复杂度: O(1)，因为字典 `positions` 的大小最多为 10（数字 0 到 9）。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_transform(s: str, t: str) -> bool:
    """
    函数式接口 - 检查字符串 s 是否可以通过排序子字符串得到字符串 t
    """
    if sorted(s) != sorted(t):
        return False

    positions = {str(i): [] for i in range(10)}
    for i, char in enumerate(s):
        positions[char].append(i)

    for char in t:
        if not positions[char]:
            return False
        pos = positions[char].pop(0)
        for smaller in range(int(char)):
            if positions[str(smaller)] and positions[str(smaller)][-1] < pos:
                return False

    return True


Solution = create_solution(can_transform)