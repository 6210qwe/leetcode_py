# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 895
标题: Shortest Path to Get All Keys
难度: hard
链接: https://leetcode.cn/problems/shortest-path-to-get-all-keys/
题目类型: 位运算、广度优先搜索、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
864. 获取所有钥匙的最短路径 - 给定一个二维网格 grid ，其中： * '.' 代表一个空房间 * '#' 代表一堵墙 * '@' 是起点 * 小写字母代表钥匙 * 大写字母代表锁 我们从起点开始出发，一次移动是指向四个基本方向之一行走一个单位空间。我们不能在网格外面行走，也无法穿过一堵墙。如果途经一个钥匙，我们就把它捡起来。除非我们手里有对应的钥匙，否则无法通过锁。 假设 k 为 钥匙/锁 的个数，且满足 1 <= k <= 6，字母表中的前 k 个字母在网格中都有自己对应的一个小写和一个大写字母。换言之，每个锁有唯一对应的钥匙，每个钥匙也有唯一对应的锁。另外，代表钥匙和锁的字母互为大小写并按字母顺序排列。 返回获取所有钥匙所需要的移动的最少次数。如果无法获取所有钥匙，返回 -1 。 示例 1： [https://assets.leetcode.com/uploads/2021/07/23/lc-keys2.jpg] 输入：grid = ["@.a..","###.#","b.A.B"] 输出：8 解释：目标是获得所有钥匙，而不是打开所有锁。 示例 2： [https://assets.leetcode.com/uploads/2021/07/23/lc-key2.jpg] 输入：grid = ["@..aA","..B#.","....b"] 输出：6 示例 3: [https://assets.leetcode.com/uploads/2021/07/23/lc-keys3.jpg] 输入: grid = ["@Aa"] 输出: -1 提示： * m == grid.length * n == grid[i].length * 1 <= m, n <= 30 * grid[i][j] 只含有 '.', '#', '@', 'a'-'f' 以及 'A'-'F' * 钥匙的数目范围是 [1, 6] * 每个钥匙都对应一个 不同 的字母 * 每个钥匙正好打开一个对应的锁
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索（BFS）结合位运算来记录已收集的钥匙状态。

算法步骤:
1. 初始化 BFS 队列，将起点位置及其初始状态（无钥匙）加入队列。
2. 使用一个集合来记录已访问过的状态（位置和钥匙状态）。
3. 开始 BFS 遍历：
   - 从队列中取出当前节点。
   - 检查是否已经收集到所有钥匙，如果是则返回步数。
   - 否则，尝试向四个方向移动，更新位置和钥匙状态。
   - 如果新位置合法且未被访问过，则将其加入队列。
4. 如果 BFS 结束仍未找到所有钥匙，返回 -1。

关键点:
- 使用位运算来记录钥匙状态，节省空间。
- 使用集合来记录已访问的状态，避免重复计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * 2^k)，其中 m 和 n 分别是网格的行数和列数，k 是钥匙的数量。每个状态最多会被访问一次。
空间复杂度: O(m * n * 2^k)，用于存储 BFS 队列和已访问状态集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def shortestPathAllKeys(grid: List[str]) -> int:
    """
    函数式接口 - 返回获取所有钥匙所需的最少移动次数
    """
    m, n = len(grid), len(grid[0])
    start = None
    keys = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                start = (i, j)
            elif grid[i][j].islower():
                keys.add(grid[i][j])

    all_keys = (1 << len(keys)) - 1
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = [(start[0], start[1], 0, 0)]  # (x, y, keys, steps)
    visited = set([(start[0], start[1], 0)])

    while queue:
        x, y, state, steps = queue.pop(0)
        if state == all_keys:
            return steps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                cell = grid[nx][ny]
                if cell == '#' or (cell.isupper() and not (state & (1 << (ord(cell) - ord('A'))))):
                    continue
                new_state = state | (1 << (ord(cell) - ord('a'))) if cell.islower() else state
                if (nx, ny, new_state) not in visited:
                    visited.add((nx, ny, new_state))
                    queue.append((nx, ny, new_state, steps + 1))

    return -1

Solution = create_solution(shortestPathAllKeys)