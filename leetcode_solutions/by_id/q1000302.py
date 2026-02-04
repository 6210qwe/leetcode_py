# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000302
标题: 打开转盘锁
难度: medium
链接: https://leetcode.cn/problems/zlDJc7/
题目类型: 广度优先搜索、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 109. 打开转盘锁 - 一个密码锁由 4 个环形拨轮组成，每个拨轮都有 10 个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。 字符串 target 代表可以解锁的数字，请给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。 示例 1： 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202" 输出：6 解释： 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，因为当拨动到 "0102" 时这个锁就会被锁定。 示例 2： 输入: deadends = ["8888"], target = "0009" 输出：1 解释： 把最后一位反向旋转一次即可 "0000" -> "0009"。 示例 3： 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888" 输出：-1 解释： 无法旋转到目标数字且不被锁定。 示例 4： 输入: deadends = ["0000"], target = "8888" 输出：-1 提示： * 1 <= deadends.length <= 500 * deadends[i].length == 4 * target.length == 4 * target 不在 deadends 之中 * target 和 deadends[i] 仅由若干位数字组成 注意：本题与主站 752 题相同： https://leetcode.cn/problems/open-the-lock/ [https://leetcode.cn/problems/open-the-lock/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）来找到从初始状态 "0000" 到目标状态 target 的最短路径。使用集合来记录已经访问过的状态和死亡数字。

算法步骤:
1. 初始化队列和集合，将初始状态 "0000" 加入队列，并将所有死亡数字加入集合。
2. 开始广度优先搜索：
   - 从队列中取出当前状态。
   - 如果当前状态为目标状态，返回当前步数。
   - 否则，生成所有可能的下一个状态，并将未访问过的状态加入队列和集合。
3. 如果队列为空且未找到目标状态，返回 -1。

关键点:
- 使用集合来记录已经访问过的状态和死亡数字，避免重复计算。
- 生成下一个状态时，考虑每一位数字的两种旋转方式。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(10^4 * 8) = O(10^4)。最坏情况下，我们需要遍历所有可能的状态（10^4 种），每种状态有 8 种可能的下一个状态。
空间复杂度: O(10^4)。最坏情况下，我们需要存储所有可能的状态。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(deadends: List[str], target: str) -> int:
    """
    函数式接口 - 打开转盘锁
    """
    if "0000" in deadends:
        return -1

    def get_neighbors(state: str) -> List[str]:
        neighbors = []
        for i in range(4):
            digit = int(state[i])
            for move in [-1, 1]:
                new_digit = (digit + move) % 10
                new_state = state[:i] + str(new_digit) + state[i+1:]
                neighbors.append(new_state)
        return neighbors

    from collections import deque
    queue = deque([("0000", 0)])
    visited = set(deadends)

    while queue:
        current, steps = queue.popleft()
        if current == target:
            return steps
        if current in visited:
            continue
        visited.add(current)
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                queue.append((neighbor, steps + 1))

    return -1


Solution = create_solution(solution_function_name)