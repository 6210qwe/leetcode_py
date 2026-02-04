# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1835
标题: Decode XORed Permutation
难度: medium
链接: https://leetcode.cn/problems/decode-xored-permutation/
题目类型: 位运算、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1734. 解码异或后的排列 - 给你一个整数数组 perm ，它是前 n 个正整数的排列，且 n 是个 奇数 。 它被加密成另一个长度为 n - 1 的整数数组 encoded ，满足 encoded[i] = perm[i] XOR perm[i + 1] 。比方说，如果 perm = [1,3,2] ，那么 encoded = [2,1] 。 给你 encoded 数组，请你返回原始数组 perm 。题目保证答案存在且唯一。 示例 1： 输入：encoded = [3,1] 输出：[1,2,3] 解释：如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1] 示例 2： 输入：encoded = [6,5,4,6] 输出：[2,4,1,5,3] 提示： * 3 <= n < 105 * n 是奇数。 * encoded.length == n - 1
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过异或运算的性质来解码。

算法步骤:
1. 计算所有元素的异或结果 total_xor。
2. 通过 encoded 数组计算前缀异或结果 prefix_xor。
3. 利用 total_xor 和 prefix_xor 来逐步恢复 perm 数组。

关键点:
- 利用异或运算的性质：a ^ a = 0 和 a ^ 0 = a。
- 通过 total_xor 和 prefix_xor 可以逐步恢复 perm 数组。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(encoded: List[int]) -> List[int]:
    """
    函数式接口 - 解码异或后的排列
    """
    n = len(encoded) + 1
    total_xor = 0
    for i in range(1, n + 1):
        total_xor ^= i

    prefix_xor = 0
    for i in range(1, n, 2):
        prefix_xor ^= encoded[i]

    first_element = total_xor ^ prefix_xor
    perm = [first_element]
    for i in range(len(encoded)):
        perm.append(perm[-1] ^ encoded[i])

    return perm


Solution = create_solution(solution_function_name)