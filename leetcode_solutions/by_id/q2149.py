# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2149
标题: Remove Colored Pieces if Both Neighbors are the Same Color
难度: medium
链接: https://leetcode.cn/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
题目类型: 贪心、数学、字符串、博弈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2038. 如果相邻两个颜色均相同则删除当前颜色 - 总共有 n 个颜色片段排成一列，每个颜色片段要么是 'A' 要么是 'B' 。给你一个长度为 n 的字符串 colors ，其中 colors[i] 表示第 i 个颜色片段的颜色。 Alice 和 Bob 在玩一个游戏，他们 轮流 从这个字符串中删除颜色。Alice 先手 。 * 如果一个颜色片段为 'A' 且 相邻两个颜色 都是颜色 'A' ，那么 Alice 可以删除该颜色片段。Alice 不可以 删除任何颜色 'B' 片段。 * 如果一个颜色片段为 'B' 且 相邻两个颜色 都是颜色 'B' ，那么 Bob 可以删除该颜色片段。Bob 不可以 删除任何颜色 'A' 片段。 * Alice 和 Bob 不能 从字符串两端删除颜色片段。 * 如果其中一人无法继续操作，则该玩家 输 掉游戏且另一玩家 获胜 。 假设 Alice 和 Bob 都采用最优策略，如果 Alice 获胜，请返回 true，否则 Bob 获胜，返回 false。 示例 1： 输入：colors = "AAABABB" 输出：true 解释： AAABABB -> AABABB Alice 先操作。 她删除从左数第二个 'A' ，这也是唯一一个相邻颜色片段都是 'A' 的 'A' 。 现在轮到 Bob 操作。 Bob 无法执行任何操作，因为没有相邻位置都是 'B' 的颜色片段 'B' 。 因此，Alice 获胜，返回 true 。 示例 2： 输入：colors = "AA" 输出：false 解释： Alice 先操作。 只有 2 个 'A' 且它们都在字符串的两端，所以她无法执行任何操作。 因此，Bob 获胜，返回 false 。 示例 3： 输入：colors = "ABBBBBBBAAA" 输出：false 解释： ABBBBBBBAAA -> ABBBBBBBAA Alice 先操作。 她唯一的选择是删除从右数起第二个 'A' 。 ABBBBBBBAA -> ABBBBBBAA 接下来轮到 Bob 操作。 他有许多选择，他可以选择任何一个 'B' 删除。 然后轮到 Alice 操作，她无法删除任何片段。 所以 Bob 获胜，返回 false 。 提示： * 1 <= colors.length <= 105 * colors 只包含字母 'A' 和 'B'
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 统计连续子串中可以删除的 'A' 和 'B' 的数量。Alice 和 Bob 分别统计 'A' 和 'B' 的可删除次数，比较两者大小来决定胜负。

算法步骤:
1. 初始化两个计数器 `alice_count` 和 `bob_count`，分别记录 Alice 和 Bob 可以删除的次数。
2. 遍历字符串，找到连续的 'A' 和 'B' 子串。
3. 对于每个连续的 'A' 子串，计算其长度减去 2（因为两端不能删除），并累加到 `alice_count`。
4. 对于每个连续的 'B' 子串，计算其长度减去 2（因为两端不能删除），并累加到 `bob_count`。
5. 比较 `alice_count` 和 `bob_count`，如果 `alice_count` 大于 `bob_count`，则 Alice 获胜，否则 Bob 获胜。

关键点:
- 通过遍历一次字符串，统计连续子串的长度来计算可删除次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串的长度。我们只需要遍历一次字符串。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(colors: str) -> bool:
    """
    函数式接口 - 判断 Alice 是否能获胜
    """
    alice_count = 0
    bob_count = 0
    n = len(colors)
    
    i = 0
    while i < n:
        # 找到连续的 'A' 子串
        if colors[i] == 'A':
            start = i
            while i < n and colors[i] == 'A':
                i += 1
            length = i - start
            if length > 2:
                alice_count += length - 2
        # 找到连续的 'B' 子串
        elif colors[i] == 'B':
            start = i
            while i < n and colors[i] == 'B':
                i += 1
            length = i - start
            if length > 2:
                bob_count += length - 2
        else:
            i += 1
    
    return alice_count > bob_count


Solution = create_solution(solution_function_name)