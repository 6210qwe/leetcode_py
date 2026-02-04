# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 753
标题: Open the Lock
难度: medium
链接: https://leetcode.cn/problems/open-the-lock/
题目类型: 广度优先搜索、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
752. 打开转盘锁 - 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。 字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。 示例 1: 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202" 输出：6 解释： 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的， 因为当拨动到 "0102" 时这个锁就会被锁定。 示例 2: 输入: deadends = ["8888"], target = "0009" 输出：1 解释：把最后一位反向旋转一次即可 "0000" -> "0009"。 示例 3: 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888" 输出：-1 解释：无法旋转到目标数字且不被锁定。 提示： * 1 <= deadends.length <= 500 * deadends[i].length == 4 * target.length == 4 * target 不在 deadends 之中 * target 和 deadends[i] 仅由若干位数字组成
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索 (BFS) 来找到从初始状态 "0000" 到目标状态 target 的最短路径。

算法步骤:
1. 初始化队列 queue 和集合 visited，将初始状态 "0000" 加入队列，并将其标记为已访问。
2. 将 deadends 中的所有状态加入 visited，以避免访问这些状态。
3. 开始 BFS 循环：
   - 从队列中取出当前状态。
   - 如果当前状态等于目标状态 target，则返回当前步数。
   - 对于当前状态的每一位数字，生成其上拨和下拨后的所有可能状态。
   - 如果这些新状态未被访问过，则将其加入队列并标记为已访问。
4. 如果队列为空且未找到目标状态，则返回 -1。

关键点:
- 使用 BFS 可以确保找到最短路径。
- 通过将 deadends 中的状态加入 visited，可以避免访问这些状态。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(10^4 * 4 * 2) = O(1)，因为每个状态最多有 8 种变化（4 位数字，每位数字有 2 种变化）。
空间复杂度: O(10^4) = O(1)，因为最多有 10^4 个状态需要存储。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def open_lock(deadends: List[str], target: str) -> int:
    from collections import deque

    if "0000" in deadends:
        return -1

    def get_neighbors(state: str):
        neighbors = []
        for i in range(4):
            digit = int(state[i])
            for delta in [-1, 1]:
                new_digit = (digit + delta) % 10
                new_state = state[:i] + str(new_digit) + state[i+1:]
                neighbors.append(new_state)
            new_digit = (digit - 1) % 10
            new_state = state[:i] + str(new_digit) + state[i+1:]
            neighbors.append(new_state)
        return neighbors

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


Solution = create_solution(open_lock)