# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2792
标题: Neighboring Bitwise XOR
难度: medium
链接: https://leetcode.cn/problems/neighboring-bitwise-xor/
题目类型: 位运算、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2683. 相邻值的按位异或 - 下标从 0 开始、长度为 n 的数组 derived 是由同样长度为 n 的原始 二进制数组 original 通过计算相邻值的 按位异或（⊕）派生而来。 特别地，对于范围 [0, n - 1] 内的每个下标 i ： * 如果 i = n - 1 ，那么 derived[i] = original[i] ⊕ original[0] * 否则 derived[i] = original[i] ⊕ original[i + 1] 给你一个数组 derived ，请判断是否存在一个能够派生得到 derived 的 有效原始二进制数组 original 。 如果存在满足要求的原始二进制数组，返回 true ；否则，返回 false 。 * 二进制数组是仅由 0 和 1 组成的数组。 示例 1： 输入：derived = [1,1,0] 输出：true 解释：能够派生得到 [1,1,0] 的有效原始二进制数组是 [0,1,0] ： derived[0] = original[0] ⊕ original[1] = 0 ⊕ 1 = 1 derived[1] = original[1] ⊕ original[2] = 1 ⊕ 0 = 1 derived[2] = original[2] ⊕ original[0] = 0 ⊕ 0 = 0 示例 2： 输入：derived = [1,1] 输出：true 解释：能够派生得到 [1,1] 的有效原始二进制数组是 [0,1] ： derived[0] = original[0] ⊕ original[1] = 1 derived[1] = original[1] ⊕ original[0] = 1 示例 3： 输入：derived = [1,0] 输出：false 解释：不存在能够派生得到 [1,0] 的有效原始二进制数组。 提示： * n == derived.length * 1 <= n <= 105 * derived 中的值不是 0 就是 1 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过异或操作的性质来判断是否可以找到一个有效的原始二进制数组。

算法步骤:
1. 初始化一个假设的原始数组 `original`，并将其第一个元素设为 0。
2. 通过遍历 `derived` 数组，逐步计算 `original` 数组的其他元素。
3. 最后检查 `original` 数组的最后一个元素与第一个元素的异或结果是否等于 `derived` 的最后一个元素。
4. 如果满足条件，则返回 `True`，否则返回 `False`。

关键点:
- 利用异或操作的性质：a ⊕ b = c 等价于 a ⊕ c = b。
- 通过逐步构建 `original` 数组来验证其有效性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 `derived` 数组的长度。我们只需要遍历一次 `derived` 数组。
空间复杂度: O(1)，除了输入和输出外，我们只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def can_form_array(derived: List[int]) -> bool:
    """
    判断是否存在一个能够派生得到 derived 的有效原始二进制数组 original。
    """
    n = len(derived)
    # 假设 original[0] = 0
    original = [0] * n
    for i in range(1, n):
        original[i] = original[i - 1] ^ derived[i - 1]
    
    # 检查最后一个元素是否满足条件
    return (original[n - 1] ^ original[0]) == derived[n - 1]


Solution = create_solution(can_form_array)