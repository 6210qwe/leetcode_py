# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000223
标题: 守卫城堡
难度: hard
链接: https://leetcode.cn/problems/7rLGCR/
题目类型: 数组、动态规划、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 38. 守卫城堡 - 城堡守卫游戏的胜利条件为使恶魔无法从出生点到达城堡。游戏地图可视作 `2*N` 的方格图，记作字符串数组 `grid`，其中： - `"."` 表示恶魔可随意通行的平地； - `"#"` 表示恶魔不可通过的障碍物，玩家可通过在 **平地** 上设置障碍物，即将 `"."` 变为 `"#"` 以阻挡恶魔前进； - `"S"` 表示恶魔出生点，将有大量的恶魔该点生成，恶魔可向上/向下/向左/向右移动，且无法移动至地图外； - `"P"` 表示瞬移点，移动到 `"P"` 点的恶魔可被传送至任意一个 `"P"` 点，也可选择不传送； - `"C"` 表示城堡。 然而在游戏中用于建造障碍物的金钱是有限的，请返回玩家最少需要放置几个障碍物才能获得胜利。若无论怎样放置障碍物均无法获胜，请返回 `-1`。 **注意：** - 地图上可能有一个或多个出生点 - 地图上有且只有一个城堡 **示例 1** >输入：`grid = ["S.C.P#P.", ".....#.S"]` > >输出：`3` > >解释：至少需要放置三个障碍物 ![image.png](https://pic.leetcode.cn/1614828255-uuNdNJ-image.png) **示例 2：** >输入：`grid = ["SP#P..P#PC#.S", "..#P..P####.#"]` > >输出：`-1` > >解释：无论怎样修筑障碍物，均无法阻挡最左侧出生的恶魔到达城堡位置 ![image.png](https://pic.leetcode.cn/1614828208-oFlpVs-image.png) **示例 3：** >输入：`grid = ["SP#.C.#PS", "P.#...#.P"]` > >输出：`0` > >解释：无需放置障碍物即可获得胜利 ![image.png](https://pic.leetcode.cn/1614828242-oveClu-image.png) **示例 4：** >输入：`grid = ["CP.#.P.", "...S..S"]` > >输出：`4` > >解释：至少需要放置 4 个障碍物，示意图为放置方法之一 ![image.png](https://pic.leetcode.cn/1614828218-sIAYkb-image.png) **提示：** - `grid.length == 2` - `2 <= grid[0].length == grid[1].length <= 10^4` - `grid[i][j]` 仅包含字符 `"."`、`"#"`、`"C"`、`"P"`、`"S"`
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用广度优先搜索 (BFS) 来检查恶魔是否可以到达城堡，并使用二分查找来确定最少需要放置的障碍物数量。

算法步骤:
1. 初始化地图，找到所有恶魔出生点和城堡的位置。
2. 使用 BFS 检查恶魔是否可以到达城堡。
3. 使用二分查找来确定最少需要放置的障碍物数量。

关键点:
- 使用 BFS 检查恶魔是否可以到达城堡。
- 使用二分查找来优化障碍物数量的确定。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(N log N)，其中 N 是网格的宽度。BFS 的时间复杂度是 O(N)，二分查找的时间复杂度是 O(log N)。
空间复杂度: O(N)，用于存储 BFS 的队列和访问标记。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_obstacles_to_defend_castle(grid: List[str]) -> int:
    def can_reach_castle(obstacles: int) -> bool:
        # 创建一个新的地图，添加障碍物
        new_grid = [list(row) for row in grid]
        placed = 0
        for i in range(2):
            for j in range(n):
                if new_grid[i][j] == '.' and placed < obstacles:
                    new_grid[i][j] = '#'
                    placed += 1
        
        # 初始化 BFS
        queue = []
        visited = set()
        for i in range(2):
            for j in range(n):
                if new_grid[i][j] == 'S':
                    queue.append((i, j))
                    visited.add((i, j))
        
        while queue:
            x, y = queue.pop(0)
            if new_grid[x][y] == 'C':
                return True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 2 and 0 <= ny < n and (nx, ny) not in visited and new_grid[nx][ny] != '#':
                    if new_grid[nx][ny] == 'P':
                        for px, py in portals:
                            if (px, py) not in visited:
                                queue.append((px, py))
                                visited.add((px, py))
                    else:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
        
        return False
    
    n = len(grid[0])
    portals = [(i, j) for i in range(2) for j in range(n) if grid[i][j] == 'P']
    
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if can_reach_castle(mid):
            left = mid + 1
        else:
            right = mid
    
    return left if left < n else -1


Solution = create_solution(min_obstacles_to_defend_castle)