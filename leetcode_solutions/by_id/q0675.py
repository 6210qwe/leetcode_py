# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 675
标题: Cut Off Trees for Golf Event
难度: hard
链接: https://leetcode.cn/problems/cut-off-trees-for-golf-event/
题目类型: 广度优先搜索、数组、矩阵、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
675. 为高尔夫比赛砍树 - 你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个 m x n 的矩阵表示， 在这个矩阵中： * 0 表示障碍，无法触碰 * 1 表示地面，可以行走 * 比 1 大的数 表示有树的单元格，可以行走，数值表示树的高度 每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。 你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 1（即变为地面）。 你将从 (0, 0) 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。 可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。 示例 1： [https://assets.leetcode.com/uploads/2020/11/26/trees1.jpg] 输入：forest = [[1,2,3],[0,0,4],[7,6,5]] 输出：6 解释：沿着上面的路径，你可以用 6 步，按从最矮到最高的顺序砍掉这些树。 示例 2： [https://assets.leetcode.com/uploads/2020/11/26/trees2.jpg] 输入：forest = [[1,2,3],[0,0,0],[7,6,5]] 输出：-1 解释：由于中间一行被障碍阻塞，无法访问最下面一行中的树。 示例 3： 输入：forest = [[2,3,4],[0,0,5],[8,7,6]] 输出：6 解释：可以按与示例 1 相同的路径来砍掉所有的树。 (0,0) 位置的树，可以直接砍去，不用算步数。 提示： * m == forest.length * n == forest[i].length * 1 <= m, n <= 50 * 0 <= forest[i][j] <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 对树按高度排序 + 多次 BFS 计算最短路径

算法步骤:
1. 遍历整个矩阵，将所有树（值 > 1）的坐标和高度收集到列表 trees 中
2. 按高度从小到大排序 trees
3. 定义 BFS 函数，从起点 (sx, sy) 到终点 (tx, ty) 计算最短步数：
   - 若起点等于终点，返回 0
   - 在矩阵范围内进行四方向 BFS，遇到 0（障碍）则不能通过
   - 若无法到达终点，返回 -1
4. 从起点 (0, 0) 依次走到每一棵树的位置：
   - 对于当前目标树 (x, y)，调用 BFS 计算步数 dist
   - 若 dist == -1，说明无法到达，返回 -1
   - 否则累加到答案，并将当前起点更新为 (x, y)
5. 最终返回累加的总步数

关键点:
- 每砍倒一棵树后，该格变为 1，不再是障碍，可以正常通过
- BFS 次数等于树的数量，矩阵最大 50x50，整体复杂度可接受
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(T * m * n) - T 为树的数量，m, n 为矩阵尺寸
空间复杂度: O(m * n) - BFS 队列与访问标记
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from collections import deque


def cut_off_tree(forest: List[List[int]]) -> int:
    """
    函数式接口 - 为高尔夫比赛砍树
    """
    if not forest or not forest[0]:
        return -1

    m, n = len(forest), len(forest[0])

    # 收集所有树的位置和高度
    trees = []
    for i in range(m):
        for j in range(n):
            if forest[i][j] > 1:
                trees.append((forest[i][j], i, j))

    # 按高度排序
    trees.sort()

    def bfs(sx: int, sy: int, tx: int, ty: int) -> int:
        """从 (sx, sy) 到 (tx, ty) 的最短路，不能经过值为 0 的格子"""
        if sx == tx and sy == ty:
            return 0

        visited = [[False] * n for _ in range(m)]
        q = deque()
        q.append((sx, sy, 0))
        visited[sx][sy] = True

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            x, y, d = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and forest[nx][ny] != 0:
                    if nx == tx and ny == ty:
                        return d + 1
                    visited[nx][ny] = True
                    q.append((nx, ny, d + 1))
        return -1

    sx = sy = 0
    total_steps = 0

    for _, tx, ty in trees:
        dist = bfs(sx, sy, tx, ty)
        if dist == -1:
            return -1
        total_steps += dist
        sx, sy = tx, ty

    return total_steps


Solution = create_solution(cut_off_tree)
