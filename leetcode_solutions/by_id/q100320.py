# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 100320
标题: 撞色搭配
难度: medium
链接: https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/
题目类型: 位运算、数组
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 177. 撞色搭配 - 整数数组 sockets 记录了一个袜子礼盒的颜色分布情况，其中 sockets[i] 表示该袜子的颜色编号。礼盒中除了一款撞色搭配的袜子，每种颜色的袜子均有两只。请设计一个程序，在时间复杂度 O(n)，空间复杂度O(1) 内找到这双撞色搭配袜子的两个颜色编号。 示例 1： 输入：sockets = [4, 5, 2, 4, 6, 6] 输出：[2,5] 或 [5,2] 示例 2： 输入：sockets = [1, 2, 4, 1, 4, 3, 12, 3] 输出：[2,12] 或 [12,2] 提示： * 2 <= sockets.length <= 10000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用异或运算找到两个只出现一次的数字。通过将所有数字异或得到的结果，可以找到这两个数字不同的那一位，然后根据这一位将所有数字分成两组，分别对这两组进行异或操作，最终得到两个只出现一次的数字。

算法步骤:
1. 将所有数字进行异或操作，得到结果 xor。
2. 找到 xor 中任意为 1 的位，记为 diff_bit。
3. 根据 diff_bit 将所有数字分成两组，一组在该位上为 0，另一组在该位上为 1。
4. 对两组分别进行异或操作，得到两个只出现一次的数字。

关键点:
- 异或运算的性质：a ^ a = 0，a ^ 0 = a。
- 通过异或运算找到两个只出现一次的数字。
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


def find_single_numbers(sockets: List[int]) -> List[int]:
    """
    函数式接口 - 找到两个只出现一次的数字
    """
    # Step 1: XOR all numbers to get the XOR of the two single numbers
    xor = 0
    for num in sockets:
        xor ^= num
    
    # Step 2: Find a bit that is different between the two single numbers
    diff_bit = xor & -xor
    
    # Step 3: Divide the numbers into two groups based on the diff_bit
    num1, num2 = 0, 0
    for num in sockets:
        if num & diff_bit:
            num1 ^= num
        else:
            num2 ^= num
    
    return [num1, num2]


Solution = create_solution(find_single_numbers)