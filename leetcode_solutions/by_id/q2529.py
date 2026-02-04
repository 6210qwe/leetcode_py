# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2529
标题: Range Product Queries of Powers
难度: medium
链接: https://leetcode.cn/problems/range-product-queries-of-powers/
题目类型: 位运算、数组、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2438. 二的幂数组中查询范围内的乘积 - 给你一个正整数 n ，你需要找到一个下标从 0 开始的数组 powers ，它包含 最少 数目的 2 的幂，且它们的和为 n 。powers 数组是 非递减 顺序的。根据前面描述，构造 powers 数组的方法是唯一的。 同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [lefti, righti] ，其中 queries[i] 表示请你求出满足 lefti <= j <= righti 的所有 powers[j] 的乘积。 请你返回一个数组 answers ，长度与 queries 的长度相同，其中 answers[i]是第 i 个查询的答案。由于查询的结果可能非常大，请你将每个 answers[i] 都对 109 + 7 取余 。 示例 1： 输入：n = 15, queries = [[0,1],[2,2],[0,3]] 输出：[2,4,64] 解释： 对于 n = 15 ，得到 powers = [1,2,4,8] 。没法得到元素数目更少的数组。 第 1 个查询的答案：powers[0] * powers[1] = 1 * 2 = 2 。 第 2 个查询的答案：powers[2] = 4 。 第 3 个查询的答案：powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64 。 每个答案对 109 + 7 取余得到的结果都相同，所以返回 [2,4,64] 。 示例 2： 输入：n = 2, queries = [[0,0]] 输出：[2] 解释： 对于 n = 2, powers = [2] 。 唯一一个查询的答案是 powers[0] = 2 。答案对 109 + 7 取余后结果相同，所以返回 [2] 。 提示： * 1 <= n <= 109 * 1 <= queries.length <= 105 * 0 <= starti <= endi < powers.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用位运算来确定 n 的二进制表示中的每一位，并构建 powers 数组。然后使用前缀积来快速计算查询结果。

算法步骤:
1. 将 n 转换为二进制表示，构建 powers 数组。
2. 计算 powers 数组的前缀积。
3. 对于每个查询，使用前缀积快速计算结果并取模。

关键点:
- 使用位运算高效地构建 powers 数组。
- 使用前缀积来加速查询。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n + q)，其中 n 是输入的整数，q 是查询的数量。
空间复杂度: O(log n)，用于存储 powers 数组和前缀积数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(n: int, queries: List[List[int]]) -> List[int]:
    """
    函数式接口 - 实现最优解法
    """
    MOD = 10**9 + 7
    powers = []
    
    # 构建 powers 数组
    for i in range(31):
        if (n >> i) & 1:
            powers.append(1 << i)
    
    # 计算前缀积
    prefix_product = [1]
    for power in powers:
        prefix_product.append((prefix_product[-1] * power) % MOD)
    
    # 处理查询
    results = []
    for left, right in queries:
        result = (prefix_product[right + 1] * pow(prefix_product[left], MOD - 2, MOD)) % MOD
        results.append(result)
    
    return results


Solution = create_solution(solution_function_name)