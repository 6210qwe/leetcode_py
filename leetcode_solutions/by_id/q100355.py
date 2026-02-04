# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100355
标题: Master Mind LCCI
难度: easy
链接: https://leetcode.cn/problems/master-mind-lcci/
题目类型: 哈希表、字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
面试题 16.15. 珠玑妙算 - 珠玑妙算游戏（the game of master mind）的玩法如下。 计算机有4个槽，每个槽放一个球，颜色可能是红色（R）、黄色（Y）、绿色（G）或蓝色（B）。例如，计算机可能有RGGB 4种（槽1为红色，槽2、3为绿色，槽4为蓝色）。作为用户，你试图猜出颜色组合。打个比方，你可能会猜YRGB。要是猜对某个槽的颜色，则算一次“猜中”；要是只猜对颜色但槽位猜错了，则算一次“伪猜中”。注意，“猜中”不能算入“伪猜中”。 给定一种颜色组合solution和一个猜测guess，编写一个方法，返回猜中和伪猜中的次数answer，其中answer[0]为猜中的次数，answer[1]为伪猜中的次数。 示例： 输入： solution="RGBY",guess="GGRR" 输出： [1,1] 解释： 猜中1次，伪猜中1次。 提示： * len(solution) = len(guess) = 4 * solution和guess仅包含"R","G","B","Y"这4种字符
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表来记录每种颜色的数量，并分别计算猜中和伪猜中的次数。

算法步骤:
1. 初始化两个计数器 `hits` 和 `pseudo_hits`。
2. 遍历 `solution` 和 `guess`，如果对应位置的颜色相同，则 `hits` 加一。
3. 使用两个哈希表分别记录 `solution` 和 `guess` 中每种颜色的数量。
4. 遍历哈希表，计算伪猜中的次数，即 `min(solution_count[color], guess_count[color]) - hits`。

关键点:
- 使用哈希表记录颜色数量，避免重复计算。
- 先计算猜中的次数，再计算伪猜中的次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串的长度，因为我们需要遍历字符串两次。
空间复杂度: O(1)，因为哈希表的大小是固定的（最多包含4种颜色）。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def master_mind(solution: str, guess: str) -> List[int]:
    """
    函数式接口 - 返回猜中和伪猜中的次数
    """
    hits = 0
    pseudo_hits = 0
    solution_count = {}
    guess_count = {}

    # 计算猜中的次数
    for i in range(len(solution)):
        if solution[i] == guess[i]:
            hits += 1
        else:
            solution_count[solution[i]] = solution_count.get(solution[i], 0) + 1
            guess_count[guess[i]] = guess_count.get(guess[i], 0) + 1

    # 计算伪猜中的次数
    for color in solution_count:
        if color in guess_count:
            pseudo_hits += min(solution_count[color], guess_count[color])

    return [hits, pseudo_hits - hits]


Solution = create_solution(master_mind)