# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1435
标题: XOR Queries of a Subarray
难度: medium
链接: https://leetcode.cn/problems/xor-queries-of-a-subarray/
题目类型: 位运算、数组、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1310. 子数组异或查询 - 有一个正整数数组 arr，现给你一个对应的查询数组 queries，其中 queries[i] = [Li, Ri]。 对于每个查询 i，请你计算从 Li 到 Ri 的 XOR 值（即 arr[Li] xor arr[Li+1] xor ... xor arr[Ri]）作为本次查询的结果。 并返回一个包含给定查询 queries 所有结果的数组。 示例 1： 输入：arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]] 输出：[2,7,14,8] 解释： 数组中元素的二进制表示形式是： 1 = 0001 3 = 0011 4 = 0100 8 = 1000 查询的 XOR 值为： [0,1] = 1 xor 3 = 2 [1,2] = 3 xor 4 = 7 [0,3] = 1 xor 3 xor 4 xor 8 = 14 [3,3] = 8 示例 2： 输入：arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]] 输出：[8,0,4,4] 提示： * 1 <= arr.length <= 3 * 10^4 * 1 <= arr[i] <= 10^9 * 1 <= queries.length <= 3 * 10^4 * queries[i].length == 2 * 0 <= queries[i][0] <= queries[i][1] < arr.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用前缀异或数组来快速计算子数组的异或值。

算法步骤:
1. 计算前缀异或数组 prefix_xor，其中 prefix_xor[i] 表示从 arr[0] 到 arr[i-1] 的异或值。
2. 对于每个查询 [L, R]，结果为 prefix_xor[L] ^ prefix_xor[R + 1]。

关键点:
- 使用前缀异或数组可以将每次查询的时间复杂度降低到 O(1)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + q)，其中 n 是数组 arr 的长度，q 是查询的数量。
空间复杂度: O(n)，用于存储前缀异或数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(arr: List[int], queries: List[List[int]]) -> List[int]:
    """
    函数式接口 - 计算子数组的异或值
    """
    # 计算前缀异或数组
    n = len(arr)
    prefix_xor = [0] * (n + 1)
    for i in range(n):
        prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

    # 处理每个查询
    results = []
    for L, R in queries:
        results.append(prefix_xor[L] ^ prefix_xor[R + 1])

    return results


Solution = create_solution(solution_function_name)