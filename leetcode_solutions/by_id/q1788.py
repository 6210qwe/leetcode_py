# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1788
标题: Stone Game VI
难度: medium
链接: https://leetcode.cn/problems/stone-game-vi/
题目类型: 贪心、数组、数学、博弈、排序、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1686. 石子游戏 VI - Alice 和 Bob 轮流玩一个游戏，Alice 先手。 一堆石子里总共有 n 个石子，轮到某个玩家时，他可以 移出 一个石子并得到这个石子的价值。Alice 和 Bob 对石子价值有 不一样的的评判标准 。双方都知道对方的评判标准。 给你两个长度为 n 的整数数组 aliceValues 和 bobValues 。aliceValues[i] 和 bobValues[i] 分别表示 Alice 和 Bob 认为第 i 个石子的价值。 所有石子都被取完后，得分较高的人为胜者。如果两个玩家得分相同，那么为平局。两位玩家都会采用 最优策略 进行游戏。 请你推断游戏的结果，用如下的方式表示： * 如果 Alice 赢，返回 1 。 * 如果 Bob 赢，返回 -1 。 * 如果游戏平局，返回 0 。 示例 1： 输入：aliceValues = [1,3], bobValues = [2,1] 输出：1 解释： 如果 Alice 拿石子 1 （下标从 0开始），那么 Alice 可以得到 3 分。 Bob 只能选择石子 0 ，得到 2 分。 Alice 获胜。 示例 2： 输入：aliceValues = [1,2], bobValues = [3,1] 输出：0 解释： Alice 拿石子 0 ， Bob 拿石子 1 ，他们得分都为 1 分。 打平。 示例 3： 输入：aliceValues = [2,4,3], bobValues = [1,6,7] 输出：-1 解释： 不管 Alice 怎么操作，Bob 都可以得到比 Alice 更高的得分。 比方说，Alice 拿石子 1 ，Bob 拿石子 2 ， Alice 拿石子 0 ，Alice 会得到 6 分而 Bob 得分为 7 分。 Bob 会获胜。 提示： * n == aliceValues.length == bobValues.length * 1 <= n <= 105 * 1 <= aliceValues[i], bobValues[i] <= 100
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过计算每个石子对 Alice 和 Bob 的总价值，并按总价值降序排序。Alice 和 Bob 交替选择石子，Alice 选择的石子对她有利，Bob 选择的石子对他有利。

算法步骤:
1. 计算每个石子对 Alice 和 Bob 的总价值。
2. 按总价值降序排序。
3. Alice 和 Bob 交替选择石子，分别累加他们的得分。
4. 比较 Alice 和 Bob 的得分，返回结果。

关键点:
- 通过总价值降序排序，确保 Alice 和 Bob 选择最优石子。
- 交替选择石子，确保双方都采用最优策略。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n) - 排序操作的时间复杂度。
空间复杂度: O(n) - 存储石子的总价值和索引。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def stoneGameVI(aliceValues: List[int], bobValues: List[int]) -> int:
    n = len(aliceValues)
    total_values = [(aliceValues[i] + bobValues[i], i) for i in range(n)]
    total_values.sort(reverse=True)
    
    alice_score = 0
    bob_score = 0
    
    for i in range(n):
        if i % 2 == 0:
            alice_score += aliceValues[total_values[i][1]]
        else:
            bob_score += bobValues[total_values[i][1]]
    
    if alice_score > bob_score:
        return 1
    elif alice_score < bob_score:
        return -1
    else:
        return 0

Solution = create_solution(stoneGameVI)