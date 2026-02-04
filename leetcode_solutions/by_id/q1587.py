# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1587
标题: Parallel Courses II
难度: hard
链接: https://leetcode.cn/problems/parallel-courses-ii/
题目类型: 位运算、图、动态规划、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1494. 并行课程 II - 给你一个整数 n 表示某所大学里课程的数目，编号为 1 到 n ，数组 relations 中， relations[i] = [xi, yi] 表示一个先修课的关系，也就是课程 xi 必须在课程 yi 之前上。同时你还有一个整数 k 。 在一个学期中，你 最多 可以同时上 k 门课，前提是这些课的先修课在之前的学期里已经上过了。 请你返回上完所有课最少需要多少个学期。题目保证一定存在一种上完所有课的方式。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/06/27/leetcode_parallel_courses_1.png] 输入：n = 4, relations = [[2,1],[3,1],[1,4]], k = 2 输出：3 解释：上图展示了题目输入的图。在第一个学期中，我们可以上课程 2 和课程 3 。然后第二个学期上课程 1 ，第三个学期上课程 4 。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/06/27/leetcode_parallel_courses_2.png] 输入：n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2 输出：4 解释：上图展示了题目输入的图。一个最优方案是：第一学期上课程 2 和 3，第二学期上课程 4 ，第三学期上课程 1 ，第四学期上课程 5 。 示例 3： 输入：n = 11, relations = [], k = 2 输出：6 提示： * 1 <= n <= 15 * 1 <= k <= n * 0 <= relations.length <= n * (n-1) / 2 * relations[i].length == 2 * 1 <= xi, yi <= n * xi != yi * 所有先修关系都是不同的，也就是说 relations[i] != relations[j] 。 * 题目输入的图是个有向无环图。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和状态压缩来解决这个问题。通过位掩码表示课程的状态，并使用 DP 数组来记录每个状态下所需的最少学期数。

算法步骤:
1. 初始化邻接表和入度数组。
2. 使用位掩码表示每种可能的课程组合状态。
3. 使用动态规划数组 dp 来记录每个状态下所需的最少学期数。
4. 对于每个状态，找到可以在这个状态下学习的课程，并更新 DP 数组。
5. 返回 dp[(1 << n) - 1]，即所有课程都完成时所需的最少学期数。

关键点:
- 使用位掩码来表示课程的状态。
- 动态规划数组 dp 用于记录每个状态下所需的最少学期数。
- 通过枚举子集来找到可以在这个状态下学习的课程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n * n^2)，其中 n 是课程的数量。我们需要枚举所有可能的状态（2^n），并且对于每个状态，我们需要检查所有课程（n）并更新 DP 数组。
空间复杂度: O(2^n)，动态规划数组 dp 的大小。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def minNumberOfSemesters(n: int, relations: List[List[int]], k: int) -> int:
    # 构建邻接表和入度数组
    adj_list = [[] for _ in range(n)]
    in_degree = [0] * n
    for prev, next in relations:
        adj_list[prev - 1].append(next - 1)
        in_degree[next - 1] += 1
    
    # 动态规划数组，dp[mask] 表示状态 mask 下所需的最少学期数
    dp = [float('inf')] * (1 << n)
    dp[0] = 0  # 空集合所需学期数为 0
    
    # 计算每个状态下的最少学期数
    for mask in range(1 << n):
        if dp[mask] == float('inf'):
            continue
        # 找到当前状态下可以学习的课程
        available_courses = []
        for i in range(n):
            if (mask & (1 << i)) == 0 and in_degree[i] == 0:
                available_courses.append(i)
        
        # 枚举子集，选择最多 k 门课程
        for i in range(1, 1 << len(available_courses)):
            if bin(i).count('1') > k:
                continue
            new_mask = mask
            for j in range(len(available_courses)):
                if i & (1 << j):
                    new_mask |= (1 << available_courses[j])
                    for next_course in adj_list[available_courses[j]]:
                        in_degree[next_course] -= 1
            dp[new_mask] = min(dp[new_mask], dp[mask] + 1)
            for j in range(len(available_courses)):
                if i & (1 << j):
                    for next_course in adj_list[available_courses[j]]:
                        in_degree[next_course] += 1
    
    return dp[(1 << n) - 1]

Solution = create_solution(minNumberOfSemesters)