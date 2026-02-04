# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3732
标题: Calculate Score After Performing Instructions
难度: medium
链接: https://leetcode.cn/problems/calculate-score-after-performing-instructions/
题目类型: 数组、哈希表、字符串、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3522. 执行指令后的得分 - 给你两个数组：instructions 和 values，数组的长度均为 n。 你需要根据以下规则模拟一个过程： * 从下标 i = 0 的第一个指令开始，初始得分为 0。 * 如果 instructions[i] 是 "add"： * 将 values[i] 加到你的得分中。 * 移动到下一个指令 (i + 1)。 * 如果 instructions[i] 是 "jump"： * 移动到下标为 (i + values[i]) 的指令，但不修改你的得分。 当以下任一情况发生时，过程会终止： * 越界（即 i < 0 或 i >= n），或 * 尝试再次执行已经执行过的指令。被重复访问的指令不会再次执行。 返回过程结束时的得分。 示例 1： 输入： instructions = ["jump","add","add","jump","add","jump"], values = [2,1,3,1,-2,-3] 输出： 1 解释： 从下标 0 开始模拟过程： * 下标 0：指令是 "jump"，移动到下标 0 + 2 = 2。 * 下标 2：指令是 "add"，将 values[2] = 3 加到得分中，移动到下标 3。得分变为 3。 * 下标 3：指令是 "jump"，移动到下标 3 + 1 = 4。 * 下标 4：指令是 "add"，将 values[4] = -2 加到得分中，移动到下标 5。得分变为 1。 * 下标 5：指令是 "jump"，移动到下标 5 + (-3) = 2。 * 下标 2：已经访问过。过程结束。 示例 2： 输入： instructions = ["jump","add","add"], values = [3,1,1] 输出： 0 解释： 从下标 0 开始模拟过程： * 下标 0：指令是 "jump"，移动到下标 0 + 3 = 3。 * 下标 3：越界。过程结束。 示例 3： 输入： instructions = ["jump"], values = [0] 输出： 0 解释： 从下标 0 开始模拟过程： * 下标 0：指令是 "jump"，移动到下标 0 + 0 = 0。 * 下标 0：已经访问过。过程结束。 提示： * n == instructions.length == values.length * 1 <= n <= 105 * instructions[i] 只能是 "add" 或 "jump"。 * -105 <= values[i] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个集合来记录已经访问过的指令，并使用一个变量来跟踪当前的得分。

算法步骤:
1. 初始化当前下标 i 为 0，得分 score 为 0，以及一个集合 visited 来记录已经访问过的指令。
2. 进入循环，直到 i 越界或 i 已经在 visited 中：
   - 如果 instructions[i] 是 "add"，将 values[i] 加到 score 中，并将 i 增加 1。
   - 如果 instructions[i] 是 "jump"，将 i 更新为 i + values[i]。
   - 将 i 添加到 visited 集合中。
3. 返回最终的得分。

关键点:
- 使用集合来记录已经访问过的指令，确保不会重复执行。
- 通过条件判断和更新下标来模拟指令的执行过程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 instructions 的长度。每个指令最多只会被执行一次。
空间复杂度: O(n)，最坏情况下所有指令都会被访问并存储在 visited 集合中。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def calculate_score_after_instructions(instructions: List[str], values: List[int]) -> int:
    """
    函数式接口 - 根据给定的指令和值计算最终得分
    """
    n = len(instructions)
    i = 0
    score = 0
    visited = set()

    while 0 <= i < n and i not in visited:
        if instructions[i] == "add":
            score += values[i]
            i += 1
        elif instructions[i] == "jump":
            i += values[i]
        
        visited.add(i)

    return score


Solution = create_solution(calculate_score_after_instructions)