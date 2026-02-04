# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1727
标题: Cat and Mouse II
难度: hard
链接: https://leetcode.cn/problems/cat-and-mouse-ii/
题目类型: 图、拓扑排序、记忆化搜索、数组、数学、动态规划、博弈、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1728. 猫和老鼠 II - 一只猫和一只老鼠在玩一个叫做猫和老鼠的游戏。 它们所处的环境设定是一个 rows x cols 的方格 grid ，其中每个格子可能是一堵墙、一块地板、一位玩家（猫或者老鼠）或者食物。 * 玩家由字符 'C' （代表猫）和 'M' （代表老鼠）表示。 * 地板由字符 '.' 表示，玩家可以通过这个格子。 * 墙用字符 '#' 表示，玩家不能通过这个格子。 * 食物用字符 'F' 表示，玩家可以通过这个格子。 * 字符 'C' ， 'M' 和 'F' 在 grid 中都只会出现一次。 猫和老鼠按照如下规则移动： * 老鼠 先移动 ，然后两名玩家轮流移动。 * 每一次操作时，猫和老鼠可以跳到上下左右四个方向之一的格子，他们不能跳过墙也不能跳出 grid 。 * catJump 和 mouseJump 是猫和老鼠分别跳一次能到达的最远距离，它们也可以跳小于最大距离的长度。 * 它们可以停留在原地。 * 老鼠可以跳跃过猫的位置。 游戏有 4 种方式会结束： * 如果猫跟老鼠处在相同的位置，那么猫获胜。 * 如果猫先到达食物，那么猫获胜。 * 如果老鼠先到达食物，那么老鼠获胜。 * 如果老鼠不能在 1000 次操作以内到达食物，那么猫获胜。 给你 rows x cols 的矩阵 grid 和两个整数 catJump 和 mouseJump ，双方都采取最优策略，如果老鼠获胜，那么请你返回 true ，否则返回 false 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/01/17/sample_111_1955.png] 输入：grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2 输出：true 解释：猫无法抓到老鼠，也没法比老鼠先到达食物。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/01/17/sample_2_1955.png] 输入：grid = ["M.C...F"], catJump = 1, mouseJump = 4 输出：true 示例 3： 输入：grid = ["M.C...F"], catJump = 1, mouseJump = 3 输出：false 示例 4： 输入：grid = ["C...#","...#F","....#","M...."], catJump = 2, mouseJump = 5 输出：false 示例 5： 输入：grid = [".M...","..#..","#..#.","C#.#.","...#F"], catJump = 3, mouseJump = 1 输出：true 提示： * rows == grid.length * cols = grid[i].length * 1 <= rows, cols <= 8 * grid[i][j] 只包含字符 'C' ，'M' ，'F' ，'.' 和 '#' 。 * grid 中只包含一个 'C' ，'M' 和 'F' 。 * 1 <= catJump, mouseJump <= 8
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用记忆化搜索来解决这个问题。我们使用一个三维数组 dp 来记录每种状态的结果，dp[turn][mouse_pos][cat_pos] 表示当前轮次 turn，老鼠位置为 mouse_pos，猫位置为 cat_pos 时的结果。

算法步骤:
1. 初始化 dp 数组，初始值为 None。
2. 定义一个递归函数 dfs(turn, mouse_pos, cat_pos) 来进行记忆化搜索。
3. 在递归函数中，首先检查当前状态是否已经计算过，如果是则直接返回结果。
4. 根据当前轮次判断是老鼠还是猫的回合，并枚举所有可能的移动。
5. 对于每个可能的移动，递归调用 dfs 函数，并根据返回结果更新当前状态的结果。
6. 返回最终结果。

关键点:
- 使用记忆化搜索来避免重复计算。
- 通过枚举所有可能的移动来确保找到最优解。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(rows * cols * (rows * cols) * (rows * cols))，其中 rows 和 cols 分别是网格的行数和列数。
空间复杂度: O(rows * cols * (rows * cols) * (rows * cols))，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def canMouseWin(grid: List[str], catJump: int, mouseJump: int) -> bool:
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # 找到初始位置
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'M':
                mouse_pos = (r, c)
            elif grid[r][c] == 'C':
                cat_pos = (r, c)
            elif grid[r][c] == 'F':
                food_pos = (r, c)
    
    # 记忆化搜索
    memo = {}
    
    def dfs(turn, mouse_pos, cat_pos):
        if (turn, mouse_pos, cat_pos) in memo:
            return memo[(turn, mouse_pos, cat_pos)]
        
        if turn >= 128:  # 最多 128 步
            return False
        
        if mouse_pos == cat_pos or cat_pos == food_pos:
            return False
        if mouse_pos == food_pos:
            return True
        
        if turn % 2 == 0:  # 老鼠的回合
            for dr, dc in directions:
                for jump in range(mouseJump + 1):
                    nr, nc = mouse_pos[0] + dr * jump, mouse_pos[1] + dc * jump
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                        if dfs(turn + 1, (nr, nc), cat_pos):
                            memo[(turn, mouse_pos, cat_pos)] = True
                            return True
                    else:
                        break
            memo[(turn, mouse_pos, cat_pos)] = False
            return False
        else:  # 猫的回合
            for dr, dc in directions:
                for jump in range(catJump + 1):
                    nr, nc = cat_pos[0] + dr * jump, cat_pos[1] + dc * jump
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                        if not dfs(turn + 1, mouse_pos, (nr, nc)):
                            memo[(turn, mouse_pos, cat_pos)] = False
                            return False
                    else:
                        break
            memo[(turn, mouse_pos, cat_pos)] = True
            return True
    
    return dfs(0, mouse_pos, cat_pos)

Solution = create_solution(canMouseWin)