# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100093
标题: Broken Board Dominoes
难度: hard
链接: https://leetcode.cn/problems/broken-board-dominoes/
题目类型: 位运算、图、数组、动态规划、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCP 04. 覆盖 - 你有一块棋盘，棋盘上有一些格子已经坏掉了。你还有无穷块大小为1 * 2的多米诺骨牌，你想把这些骨牌不重叠地覆盖在完好的格子上，请找出你最多能在棋盘上放多少块骨牌？这些骨牌可以横着或者竖着放。 输入：n, m代表棋盘的大小；broken是一个b * 2的二维数组，其中每个元素代表棋盘上每一个坏掉的格子的位置。 输出：一个整数，代表最多能在棋盘上放的骨牌数。 示例 1： 输入：n = 2, m = 3, broken = [[1, 0], [1, 1]] 输出：2 解释：我们最多可以放两块骨牌：[[0, 0], [0, 1]]以及[[0, 2], [1, 2]]。（见下图） [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/09/09/domino_example_1.jpg] 示例 2： 输入：n = 3, m = 3, broken = [] 输出：4 解释：下图是其中一种可行的摆放方式 [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/09/09/domino_example_2.jpg] 限制： 1. 1 <= n <= 8 2. 1 <= m <= 8 3. 0 <= b <= n * m
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和状态压缩来解决这个问题。我们将棋盘的每一行的状态用一个整数表示，然后使用动态规划来计算每种状态下的最大骨牌数。

算法步骤:
1. 初始化一个二维数组 dp，dp[i][state] 表示前 i 行在第 i 行状态为 state 时的最大骨牌数。
2. 枚举每一行的状态，并计算当前状态下的最大骨牌数。
3. 更新 dp 数组，最终结果保存在 dp[n][0] 中。

关键点:
- 使用状态压缩来表示每一行的状态。
- 动态规划转移方程需要考虑当前状态和前一行状态的兼容性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^(m*n) * n * m)
空间复杂度: O(2^m * n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def max_domino(n: int, m: int, broken: List[List[int]]) -> int:
    # 将 broken 数组转换为集合，方便快速查找
    broken_set = set(tuple(b) for b in broken)
    
    # 计算所有可能的状态数
    all_states = 1 << m
    
    # 初始化 dp 数组
    dp = [[-1] * all_states for _ in range(n + 1)]
    dp[0][0] = 0
    
    def is_valid(state: int, row: int) -> bool:
        """检查当前状态是否有效"""
        for col in range(m):
            if (state >> col) & 1 and (row, col) in broken_set:
                return False
        return True
    
    def count_bits(x: int) -> int:
        """计算二进制中 1 的个数"""
        count = 0
        while x:
            count += x & 1
            x >>= 1
        return count
    
    for row in range(1, n + 1):
        for cur_state in range(all_states):
            if not is_valid(cur_state, row - 1):
                continue
            for prev_state in range(all_states):
                if dp[row - 1][prev_state] == -1:
                    continue
                if cur_state & prev_state == 0:
                    dp[row][cur_state] = max(dp[row][cur_state], dp[row - 1][prev_state] + count_bits(cur_state) // 2)
    
    return max(dp[n])

Solution = create_solution(max_domino)