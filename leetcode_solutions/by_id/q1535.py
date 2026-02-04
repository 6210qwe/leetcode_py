# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1535
标题: Build Array Where You Can Find The Maximum Exactly K Comparisons
难度: hard
链接: https://leetcode.cn/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/
题目类型: 动态规划、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1420. 生成数组 - 给定三个整数 n、m 和 k 。考虑使用下图描述的算法找出正整数数组中最大的元素。 [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/04/19/e.png] 请你构建一个具有以下属性的数组 arr ： * arr 中包含确切的 n 个整数。 * 1 <= arr[i] <= m 其中 (0 <= i < n) 。 * 将上面提到的算法应用于 arr 之后，search_cost 的值等于 k 。 返回在满足上述条件的情况下构建数组 arr 的 方法数量 ，由于答案可能会很大，所以 必须 对 10^9 + 7 取余。 示例 1： 输入：n = 2, m = 3, k = 1 输出：6 解释：可能的数组分别为 [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3] 示例 2： 输入：n = 5, m = 2, k = 3 输出：0 解释：没有数组可以满足上述条件 示例 3： 输入：n = 9, m = 1, k = 1 输出：1 解释：唯一可能的数组是 [1, 1, 1, 1, 1, 1, 1, 1, 1] 提示： * 1 <= n <= 50 * 1 <= m <= 100 * 0 <= k <= n
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。定义 dp[i][j][k] 表示长度为 i 的数组，最大值为 j，且 search_cost 为 k 的方案数。

算法步骤:
1. 初始化 dp 数组，dp[0][j][0] = 1，表示空数组的 search_cost 为 0。
2. 遍历长度 i 从 1 到 n，遍历最大值 j 从 1 到 m，遍历 search_cost k 从 0 到 K。
3. 对于每个状态 dp[i][j][k]，有两种情况：
   - 当前位置的值小于 j，那么 dp[i][j][k] += dp[i-1][j][k] * j。
   - 当前位置的值等于 j，那么 dp[i][j][k] += sum(dp[i-1][x][k-1]) for x in range(1, j)。
4. 最终结果是 sum(dp[n][j][K]) for j in range(1, m+1)。

关键点:
- 动态规划的状态转移方程。
- 优化空间复杂度，使用滚动数组。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m * k * m)
空间复杂度: O(n * m * k)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(n: int, m: int, k: int) -> int:
    """
    函数式接口 - 计算满足条件的数组数量
    """
    MOD = 10**9 + 7
    dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    
    # 初始化
    for j in range(1, m + 1):
        dp[0][j][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for cost in range(k + 1):
                # 当前位置的值小于 j
                dp[i][j][cost] += dp[i - 1][j][cost] * j
                dp[i][j][cost] %= MOD
                
                # 当前位置的值等于 j
                if cost > 0:
                    for x in range(1, j):
                        dp[i][j][cost] += dp[i - 1][x][cost - 1]
                        dp[i][j][cost] %= MOD
    
    return sum(dp[n][j][k] for j in range(1, m + 1)) % MOD


Solution = create_solution(solution_function_name)