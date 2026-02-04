# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 949
标题: Cat and Mouse
难度: hard
链接: https://leetcode.cn/problems/cat-and-mouse/
题目类型: 图、拓扑排序、记忆化搜索、数学、动态规划、博弈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
913. 猫和老鼠 - 两位玩家分别扮演猫和老鼠，在一张 无向 图上进行游戏，两人轮流行动。 图的形式是：graph[a] 是一个列表，由满足 ab 是图中的一条边的所有节点 b 组成。 老鼠从节点 1 开始，第一个出发；猫从节点 2 开始，第二个出发。在节点 0 处有一个洞。 在每个玩家的行动中，他们 必须 沿着图中与所在当前位置连通的一条边移动。例如，如果老鼠在节点 1 ，那么它必须移动到 graph[1] 中的任一节点。 此外，猫无法移动到洞中（节点 0）。 然后，游戏在出现以下三种情形之一时结束： * 如果猫和老鼠出现在同一个节点，猫获胜。 * 如果老鼠到达洞中，老鼠获胜。 * 如果某一位置重复出现（即，玩家的位置和移动顺序都与上一次行动相同），游戏平局。 给你一张图 graph ，并假设两位玩家都都以最佳状态参与游戏： * 如果老鼠获胜，则返回 1； * 如果猫获胜，则返回 2； * 如果平局，则返回 0 。 示例 1： [https://assets.leetcode.com/uploads/2020/11/17/cat1.jpg] 输入：graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]] 输出：0 示例 2： [https://assets.leetcode.com/uploads/2020/11/17/cat2.jpg] 输入：graph = [[1,3],[0],[3],[0,2]] 输出：1 提示： * 3 <= graph.length <= 50 * 1 <= graph[i].length < graph.length * 0 <= graph[i][j] < graph.length * graph[i][j] != i * graph[i] 互不相同 * 猫和老鼠在游戏中总是可以移动
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用记忆化搜索来解决这个问题。我们使用一个三维数组 `dp` 来记录每种状态下的结果，其中 `dp[turns][mouse_pos][cat_pos]` 表示当前轮次为 `turns`，老鼠在 `mouse_pos` 位置，猫在 `cat_pos` 位置时的结果。

算法步骤:
1. 初始化 `dp` 数组，并设置基础情况。
2. 使用递归函数 `search` 来搜索所有可能的状态。
3. 在递归函数中，根据当前轮次和玩家位置，判断是否达到终止条件。
4. 如果没有达到终止条件，继续递归搜索下一轮次的状态。
5. 根据递归结果更新 `dp` 数组。

关键点:
- 使用记忆化搜索来避免重复计算。
- 通过递归函数来模拟游戏过程。
- 通过 `dp` 数组来记录每种状态下的结果。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^3 * 2n)，其中 n 是图的节点数。因为每个状态 (turns, mouse_pos, cat_pos) 最多被计算一次，而 turns 的最大值为 2n。
空间复杂度: O(n^3 * 2n)，用于存储 `dp` 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def catMouseGame(graph: List[List[int]]) -> int:
    n = len(graph)
    DRAW, MOUSE, CAT = 0, 1, 2
    dp = [[[None for _ in range(n)] for _ in range(n)] for _ in range(2 * n)]
    
    def search(turns, mouse_pos, cat_pos):
        if turns == 2 * n:
            return DRAW
        if dp[turns][mouse_pos][cat_pos] is not None:
            return dp[turns][mouse_pos][cat_pos]
        
        if mouse_pos == 0:
            dp[turns][mouse_pos][cat_pos] = MOUSE
            return MOUSE
        if mouse_pos == cat_pos:
            dp[turns][mouse_pos][cat_pos] = CAT
            return CAT
        
        player = MOUSE if turns % 2 == 0 else CAT
        default_result = DRAW
        if player == MOUSE:
            result = CAT
            for next_pos in graph[mouse_pos]:
                next_result = search(turns + 1, next_pos, cat_pos)
                if next_result == MOUSE:
                    result = MOUSE
                    break
                elif next_result == DRAW:
                    default_result = DRAW
        else:
            result = MOUSE
            for next_pos in graph[cat_pos]:
                if next_pos == 0:
                    continue
                next_result = search(turns + 1, mouse_pos, next_pos)
                if next_result == CAT:
                    result = CAT
                    break
                elif next_result == DRAW:
                    default_result = DRAW
        
        dp[turns][mouse_pos][cat_pos] = result if result != DRAW else default_result
        return dp[turns][mouse_pos][cat_pos]
    
    return search(0, 1, 2)

Solution = create_solution(catMouseGame)