# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1839
标题: Decode XORed Array
难度: easy
链接: https://leetcode.cn/problems/decode-xored-array/
题目类型: 位运算、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1720. 解码异或后的数组 - 未知 整数数组 arr 由 n 个非负整数组成。 经编码后变为长度为 n - 1 的另一个整数数组 encoded ，其中 encoded[i] = arr[i] XOR arr[i + 1] 。例如，arr = [1,0,2,1] 经编码后得到 encoded = [1,2,3] 。 给你编码后的数组 encoded 和原数组 arr 的第一个元素 first（arr[0]）。 请解码返回原数组 arr 。可以证明答案存在并且是唯一的。 示例 1： 输入：encoded = [1,2,3], first = 1 输出：[1,0,2,1] 解释：若 arr = [1,0,2,1] ，那么 first = 1 且 encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3] 示例 2： 输入：encoded = [6,2,7,3], first = 4 输出：[4,2,0,7,4] 提示： * 2 <= n <= 104 * encoded.length == n - 1 * 0 <= encoded[i] <= 105 * 0 <= first <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过异或运算的性质来解码数组。

算法步骤:
1. 初始化结果数组 `arr`，将 `first` 作为第一个元素。
2. 遍历 `encoded` 数组，对于每个 `encoded[i]`，计算 `arr[i+1] = arr[i] XOR encoded[i]`，并将结果添加到 `arr` 中。

关键点:
- 异或运算的性质：a XOR b = c，则 a XOR c = b。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 `encoded` 数组的长度。
空间复杂度: O(n)，需要存储解码后的数组 `arr`。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def decode(encoded: List[int], first: int) -> List[int]:
    """
    函数式接口 - 解码异或后的数组
    """
    # 初始化结果数组
    arr = [first]
    
    # 遍历 encoded 数组，解码出原数组
    for enc in encoded:
        next_element = arr[-1] ^ enc
        arr.append(next_element)
    
    return arr


Solution = create_solution(decode)