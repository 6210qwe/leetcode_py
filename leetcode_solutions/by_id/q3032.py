# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3032
标题: Maximize Value of Function in a Ball Passing Game
难度: hard
链接: https://leetcode.cn/problems/maximize-value-of-function-in-a-ball-passing-game/
题目类型: 位运算、数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2836. 在传球游戏中最大化函数值 - 给你一个长度为 n 下标从 0 开始的整数数组 receiver 和一个整数 k 。 总共有 n 名玩家，玩家 编号 互不相同，且为 [0, n - 1] 中的整数。这些玩家玩一个传球游戏，receiver[i] 表示编号为 i 的玩家会传球给编号为 receiver[i] 的玩家。玩家可以传球给自己，也就是说 receiver[i] 可能等于 i 。 你需要从 n 名玩家中选择一名玩家作为游戏开始时唯一手中有球的玩家，球会被传 恰好 k 次。 如果选择编号为 x 的玩家作为开始玩家，定义函数 f(x) 表示从编号为 x 的玩家开始，k 次传球内所有接触过球玩家的编号之 和 ，如果有玩家多次触球，则 累加多次 。换句话说， f(x) = x + receiver[x] + receiver[receiver[x]] + ... + receiver(k)[x] 。 你的任务时选择开始玩家 x ，目的是 最大化 f(x) 。 请你返回函数的 最大值 。 注意：receiver 可能含有重复元素。 示例 1： 传递次数 传球者编号 接球者编号 x + 所有接球者编号 2 1 2 1 3 2 1 0 3 3 0 2 5 4 2 1 6 输入：receiver = [2,0,1], k = 4 输出：6 解释：上表展示了从编号为 x = 2 开始的游戏过程。 从表中可知，f(2) 等于 6 。 6 是能得到最大的函数值。 所以输出为 6 。 示例 2： 传递次数 传球者编号 接球者编号 x + 所有接球者编号 4 1 4 3 7 2 3 2 9 3 2 1 10 输入：receiver = [1,1,1,2,3], k = 3 输出：10 解释：上表展示了从编号为 x = 4 开始的游戏过程。 从表中可知，f(4) 等于 10 。 10 是能得到最大的函数值。 所以输出为 10 。 提示： * 1 <= receiver.length == n <= 105 * 0 <= receiver[i] <= n - 1 * 1 <= k <= 1010
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用倍增法（Binary Lifting）来快速计算 k 次传球后的结果。

算法步骤:
1. 构建倍增数组 `parent`，其中 `parent[j][i]` 表示从节点 i 出发经过 2^j 次传球后到达的节点。
2. 计算每个节点的前缀和 `prefix_sum`，用于快速计算 k 次传球后的总和。
3. 对于每个起始节点，使用倍增法计算 k 次传球后的总和，并更新最大值。

关键点:
- 倍增法可以在 O(log k) 时间内计算 k 次传球后的结果。
- 使用前缀和可以快速计算路径上的总和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log k)
空间复杂度: O(n log k)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def maximize_value(receiver: List[int], k: int) -> int:
    n = len(receiver)
    log_k = k.bit_length()  # 计算 log k
    parent = [[-1] * n for _ in range(log_k)]
    prefix_sum = [[0] * n for _ in range(log_k)]

    # 初始化 parent 和 prefix_sum
    for i in range(n):
        parent[0][i] = receiver[i]
        prefix_sum[0][i] = i + receiver[i]

    # 构建倍增数组
    for j in range(1, log_k):
        for i in range(n):
            if parent[j - 1][i] != -1:
                parent[j][i] = parent[j - 1][parent[j - 1][i]]
                prefix_sum[j][i] = prefix_sum[j - 1][i] + prefix_sum[j - 1][parent[j - 1][i]]

    def get_sum(node: int, steps: int) -> int:
        total = node
        for j in range(log_k):
            if (steps >> j) & 1:
                total += prefix_sum[j][node]
                node = parent[j][node]
        return total

    max_value = 0
    for i in range(n):
        max_value = max(max_value, get_sum(i, k))

    return max_value


Solution = create_solution(maximize_value)