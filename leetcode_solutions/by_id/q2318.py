# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2318
标题: Maximum Points in an Archery Competition
难度: medium
链接: https://leetcode.cn/problems/maximum-points-in-an-archery-competition/
题目类型: 位运算、数组、回溯、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2212. 射箭比赛中的最大得分 - Alice 和 Bob 是一场射箭比赛中的对手。比赛规则如下： 1. Alice 先射 numArrows 支箭，然后 Bob 也射 numArrows 支箭。 2. 分数按下述规则计算： 1. 箭靶有若干整数计分区域，范围从 0 到 11 （含 0 和 11）。 2. 箭靶上每个区域都对应一个得分 k（范围是 0 到 11），Alice 和 Bob 分别在得分 k 区域射中 ak 和 bk 支箭。如果 ak >= bk ，那么 Alice 得 k 分。如果 ak < bk ，则 Bob 得 k 分 3. 如果 ak == bk == 0 ，那么无人得到 k 分。 * 例如，Alice 和 Bob 都向计分为 11 的区域射 2 支箭，那么 Alice 得 11 分。如果 Alice 向计分为 11 的区域射 0 支箭，但 Bob 向同一个区域射 2 支箭，那么 Bob 得 11 分。 给你整数 numArrows 和一个长度为 12 的整数数组 aliceArrows ，该数组表示 Alice 射中 0 到 11 每个计分区域的箭数量。现在，Bob 想要尽可能 最大化 他所能获得的总分。 返回数组 bobArrows ，该数组表示 Bob 射中 0 到 11 每个 计分区域的箭数量。且 bobArrows 的总和应当等于 numArrows 。 如果存在多种方法都可以使 Bob 获得最大总分，返回其中 任意一种 即可。 示例 1： [https://pic.leetcode.cn/1647744752-kQKrXw-image.png] 输入：numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0] 输出：[0,0,0,0,1,1,0,0,1,2,3,1] 解释：上表显示了比赛得分情况。 Bob 获得总分 4 + 5 + 8 + 9 + 10 + 11 = 47 。 可以证明 Bob 无法获得比 47 更高的分数。 示例 2： [https://pic.leetcode.cn/1647744785-cMHzaC-image.png] 输入：numArrows = 3, aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,2] 输出：[0,0,0,0,0,0,0,0,1,1,1,0] 解释：上表显示了比赛得分情况。 Bob 获得总分 8 + 9 + 10 = 27 。 可以证明 Bob 无法获得比 27 更高的分数。 提示： * 1 <= numArrows <= 105 * aliceArrows.length == bobArrows.length == 12 * 0 <= aliceArrows[i], bobArrows[i] <= numArrows * sum(aliceArrows[i]) == numArrows
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义一个二维数组 dp，其中 dp[i][j] 表示前 i 个区域使用 j 支箭能获得的最大分数。通过递推公式更新 dp 数组，并记录路径。

算法步骤:
1. 初始化 dp 数组，dp[i][j] 表示前 i 个区域使用 j 支箭能获得的最大分数。
2. 通过递推公式更新 dp 数组：
   - 如果不选择当前区域，则 dp[i][j] = dp[i-1][j]
   - 如果选择当前区域，则 dp[i][j] = dp[i-1][j - (aliceArrows[i] + 1)] + i
3. 通过 dp 数组回溯路径，找到最优解。

关键点:
- 动态规划的状态转移方程
- 回溯路径找到最优解
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(12 * numArrows) = O(numArrows)
空间复杂度: O(12 * numArrows) = O(numArrows)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def maximum_bob_points(num_arrows: int, alice_arrows: List[int]) -> List[int]:
    # 定义 dp 数组
    dp = [[0] * (num_arrows + 1) for _ in range(12)]
    path = [[0] * (num_arrows + 1) for _ in range(12)]

    # 动态规划填充 dp 数组
    for i in range(1, 12):
        for j in range(1, num_arrows + 1):
            if j >= alice_arrows[i] + 1:
                if dp[i - 1][j] < dp[i - 1][j - (alice_arrows[i] + 1)] + i:
                    dp[i][j] = dp[i - 1][j - (alice_arrows[i] + 1)] + i
                    path[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    # 回溯路径找到最优解
    bob_arrows = [0] * 12
    remaining_arrows = num_arrows
    for i in range(11, 0, -1):
        if path[i][remaining_arrows] == 1:
            bob_arrows[i] = alice_arrows[i] + 1
            remaining_arrows -= alice_arrows[i] + 1

    # 将剩余的箭分配到任意区域
    if remaining_arrows > 0:
        bob_arrows[0] = remaining_arrows

    return bob_arrows

Solution = create_solution(maximum_bob_points)