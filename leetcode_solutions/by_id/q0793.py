# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 793
标题: Swap Adjacent in LR String
难度: medium
链接: https://leetcode.cn/problems/swap-adjacent-in-lr-string/
题目类型: 双指针、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
777. 在 LR 字符串中交换相邻字符 - 在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个 "LX" 替换一个 "XL"，或者用一个 "XR" 替换一个 "RX"。现给定起始字符串 start 和结束字符串 result，请编写代码，当且仅当存在一系列移动操作使得 start 可以转换成 result 时， 返回 True。 示例 1： 输入：start = "RXXLRXRXL", result = "XRLXXRRLX" 输出：true 解释：通过以下步骤我们可以将 start 转化为 result： RXXLRXRXL -> XRXLRXRXL -> XRLXRXRXL -> XRLXXRRXL -> XRLXXRRLX 示例 2： 输入：start = "X", result = "L" 输出：false 提示： * 1 <= start.length <= 104 * start.length == result.length * start 和 result 都只包含 'L', 'R' 或 'X'。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用双指针分别遍历 start 和 end 字符串，跳过 'X' 字符，比较 'L' 和 'R' 的位置关系。

算法步骤:
1. 初始化两个指针 i 和 j 分别指向 start 和 end 字符串的起始位置。
2. 遍历字符串，跳过 'X' 字符，找到 'L' 或 'R'。
3. 比较当前字符的位置关系：
   - 如果 start 中的 'L' 在 end 中对应的 'L' 的右边，返回 False。
   - 如果 start 中的 'R' 在 end 中对应的 'R' 的左边，返回 False。
4. 如果遍历完所有字符且没有违反上述规则，返回 True。

关键点:
- 'L' 只能向左移动，'R' 只能向右移动。
- 'L' 和 'R' 的相对顺序不能改变。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串的长度。每个字符最多被访问两次。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def canTransform(start: str, end: str) -> bool:
    """
    函数式接口 - 判断 start 是否可以通过一系列移动操作转换为 end
    """
    if len(start) != len(end):
        return False

    i, j = 0, 0
    n = len(start)

    while i < n or j < n:
        # 跳过 start 中的 'X'
        while i < n and start[i] == 'X':
            i += 1
        # 跳过 end 中的 'X'
        while j < n and end[j] == 'X':
            j += 1

        # 如果其中一个指针已经到达末尾，另一个还没有，说明字符数量不匹配
        if i == n or j == n:
            break

        # 比较当前字符
        if start[i] != end[j]:
            return False

        # 'L' 只能向左移动
        if start[i] == 'L' and i < j:
            return False
        # 'R' 只能向右移动
        if start[i] == 'R' and i > j:
            return False

        i += 1
        j += 1

    # 确保所有字符都匹配
    return i == n and j == n


Solution = create_solution(canTransform)