# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2700
标题: Substring XOR Queries
难度: medium
链接: https://leetcode.cn/problems/substring-xor-queries/
题目类型: 位运算、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2564. 子字符串异或查询 - 给你一个 二进制字符串 s 和一个整数数组 queries ，其中 queries[i] = [firsti, secondi] 。 对于第 i 个查询，找到 s 的 最短子字符串 ，它对应的 十进制值 val 与 firsti 按位异或 得到 secondi ，换言之，val ^ firsti == secondi 。 第 i 个查询的答案是子字符串 [lefti, righti] 的两个端点（下标从 0 开始），如果不存在这样的子字符串，则答案为 [-1, -1] 。如果有多个答案，请你选择 lefti 最小的一个。 请你返回一个数组 ans ，其中 ans[i] = [lefti, righti] 是第 i 个查询的答案。 子字符串 是一个字符串中一段连续非空的字符序列。 示例 1： 输入：s = "101101", queries = [[0,5],[1,2]] 输出：[[0,2],[2,3]] 解释：第一个查询，端点为 [0,2] 的子字符串为 "101" ，对应十进制数字 5 ，且 5 ^ 0 = 5 ，所以第一个查询的答案为 [0,2]。第二个查询中，端点为 [2,3] 的子字符串为 "11" ，对应十进制数字 3 ，且 3 ^ 1 = 2 。所以第二个查询的答案为 [2,3] 。 示例 2： 输入：s = "0101", queries = [[12,8]] 输出：[[-1,-1]] 解释：这个例子中，没有符合查询的答案，所以返回 [-1,-1] 。 示例 3： 输入：s = "1", queries = [[4,5]] 输出：[[0,0]] 解释：这个例子中，端点为 [0,0] 的子字符串对应的十进制值为 1 ，且 1 ^ 4 = 5 。所以答案为 [0,0] 。 提示： * 1 <= s.length <= 104 * s[i] 要么是 '0' ，要么是 '1' 。 * 1 <= queries.length <= 105 * 0 <= firsti, secondi <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用预处理和哈希表来快速查找每个查询的结果。

算法步骤:
1. 预处理所有可能的子字符串，并记录它们的起始位置。
2. 对于每个查询，计算目标值 target = firsti ^ secondi。
3. 在预处理的哈希表中查找目标值，找到最短的子字符串。

关键点:
- 预处理时，只需要考虑长度不超过 30 的子字符串，因为 2^30 > 10^9。
- 使用哈希表存储每个值的最短子字符串的起始位置。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * 30 + m)，其中 n 是字符串 s 的长度，m 是 queries 的长度。
空间复杂度: O(n * 30)，用于存储预处理结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(s: str, queries: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 实现最优解法
    """
    # 预处理所有可能的子字符串，并记录它们的起始位置
    max_len = 30
    value_to_index = {}
    
    for i in range(len(s)):
        if s[i] == '0':
            if 0 not in value_to_index:
                value_to_index[0] = (i, i)
            continue
        
        current_value = 0
        for j in range(i, min(i + max_len, len(s))):
            current_value = (current_value << 1) | (int(s[j]))
            if current_value not in value_to_index:
                value_to_index[current_value] = (i, j)
    
    # 处理每个查询
    result = []
    for first, second in queries:
        target = first ^ second
        if target in value_to_index:
            result.append(list(value_to_index[target]))
        else:
            result.append([-1, -1])
    
    return result


Solution = create_solution(solution_function_name)